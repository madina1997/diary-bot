from datetime import datetime
import logging
import os

import telegram.bot
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram.ext import messagequeue as mq
from telegram.utils.request import Request
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest

from storage import QuizStorage, ChatStorage, DatalogStorage
from export import get_quizes_plot, get_csv
import texts
import re
import time
from threading import Thread
from datetime import timedelta


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def help(bot, update):
    print(update.message.chat_id)
    lang = chat_storage.get_or_create(update.message.chat_id)['language']
    bot.send_message(text=texts.INTRO[lang], chat_id=update.message.chat_id)


def start(bot, update):
    # Select language
    langs_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton('English {}'.format(b'\xF0\x9F\x87\xAC\xF0\x9F\x87\xA7'.decode()), callback_data='en'),
        InlineKeyboardButton('Русский {}'.format(b'\xF0\x9F\x87\xB7\xF0\x9F\x87\xBA'.decode()), callback_data='ru')]])
    bot.send_message(
        text='Choose your language / Выберите язык', reply_markup=langs_markup, chat_id=update.message.chat_id)


def process_lang(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        text="{}\n{}".format(query.message.text, query.data), chat_id=query.message.chat_id,
        message_id=query.message.message_id)
    chat = chat_storage.get_or_create(query.message.chat_id)
    chat['language'] = query.data
    chat_storage.save(chat)
    send_frequency_question(bot, query.message.chat_id)


def send_frequency_question(bot, chat_id):
    lang = chat_storage.get_or_create(chat_id)['language']
    frequency_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(texts.FREQUENCY_NONE[lang], callback_data='none'),
        InlineKeyboardButton(texts.FREQUENCY_DAILY[lang], callback_data='daily'),
        InlineKeyboardButton(texts.FREQUENCY_WEEKLY[lang], callback_data='weekly')]])
    bot.send_message(text=texts.FREQUENCY_QUESTION[lang], reply_markup=frequency_markup, chat_id=chat_id)


def process_frequency(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        text="{}\n{}".format(query.message.text, query.data), chat_id=query.message.chat_id,
        message_id=query.message.message_id)
    chat = chat_storage.get_or_create(query.message.chat_id)
    chat['frequency'] = query.data
    chat_storage.save(chat)
    send_intro(bot, query.message.chat_id)


def send_intro(bot, chat_id):
    lang = chat_storage.get_or_create(chat_id)['language']
    bot.send_message(text=texts.INTRO[lang], chat_id=chat_id)


def send_hars_question(question, answer_weight, bot, chat_id):
    keyboard = []
    for j, answer in zip(answer_weight, question.answers): #go through each number in answers_weight for every question
        keyboard.append([InlineKeyboardButton(answer, callback_data=j)])
    # keyboard = [[InlineKeyboardButton(answer, callback_data=i)] for i, answer in enumerate(question.answers)]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(text=question.question, reply_markup=reply_markup, chat_id=chat_id)


def hars_quiz(bot, update):
    quiz = quiz_storage.create_quiz(update.message.chat_id, 'hars')
    question = quiz.get_question()
    lang = chat_storage.get_or_create(update.message.chat_id)['language']
    bot.send_message(text=texts.HARS_INTRO[lang], chat_id=update.message.chat_id)
    answer_weight = quiz.get_answers_weight()
    send_hars_question(question, answer_weight, bot, update.message.chat_id)

# ВОТ ТУТ БУДЕТ ФУНКЦИЯ НА ОЦЕНКУ ГОТОВНОСТИ
# def send_amiready_question(question, bot, chat_id):
#     bot.send_message(text=question, chat_id=chat_id)


# def send_amiready_keyboard(question, bot, chat_id):
#     keyboard = [[InlineKeyboardButton(answer, callback_data = i)] for i, answer in enumerate(question.answers)]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     question_text = '{}\n'.format(question.question)
#     bot.send_message(text=question_text, reply_markup=reply_markup, chat_id=chat_id)

def amiready_quiz(bot, update):
    quiz = quiz_storage.create_quiz(update.message.chat_id, 'amiready')
    # selfesteem, sign = quiz.process_answer(selfesteem, sign) #here i have changed the selfesteem and sign for a new one
    lang = chat_storage.get_or_create(update.message.chat_id)['language']
    bot.send_message(text=texts.AMIREADY_INTRO[lang], chat_id=update.message.chat_id)
    # question = quiz.get_direction()
    bot.send_message(text=quiz.questions[lang]["low"]["plus"], chat_id=update.message.chat_id)


def process_answer(bot, update):
    #ASS added quiz_answer to send individual weights for every question:
    query = update.callback_query
    quiz = quiz_storage.get_latest_quiz(query.message.chat_id)
    quiz_storage.save_answer(quiz, int(query.data))
    if quiz.type_ == 'hars':
        bot.edit_message_text(
            text="{}\n{}".format(query.message.text, query.data), chat_id=query.message.chat_id,
            message_id=query.message.message_id)
        if quiz.is_completed: #ASS have added and hars
            bot.send_message(chat_id=query.message.chat_id, text="🏁\n{}".format(quiz.get_result()))
        else:
            question = quiz.get_question()
            answer_weight = quiz.get_answers_weight()
            send_hars_question(question, answer_weight, bot, query.message.chat_id)
    elif quiz.type_ == 'amiready':
        n = int(query.data)
        quiz.process_direction(n)
        question = quiz.get_direction()
        send_amiready_question(question, bot, query.message.chat_id)


def process_message(bot, update):
    # bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    quiz = quiz_storage.get_latest_quiz(update.message.chat_id)
    lang = chat_storage.get_or_create(update.message.chat_id)['language']
    if quiz.type_ == 'amiready':
        # update.message.reply_text(update.message.text)
        message = update.message.text.split(",")
        quiz_storage.save_answer(quiz, len(message))
        if quiz.question_number == 1:
            bot.send_message(text = quiz.questions[lang]["low"]["minus"], chat_id=update.message.chat_id)
        if quiz.question_number == 2:
            bot.send_message(text = quiz.questions[lang]["high"]["plus"], chat_id=update.message.chat_id)
        if quiz.question_number == 3:
            bot.send_message(text = quiz.questions[lang]["high"]["minus"], chat_id=update.message.chat_id)
        if quiz.question_number == 4:
            ans = quiz.answers
            score = ans[1] -ans[0] + ans[2] - ans[3]
            # update.message.reply_text(quiz.answers)
            update.message.reply_text("Your score is " + str(score))
            bot.send_message(chat_id=update.message.chat_id, text="🏁\n{}".format(quiz.get_result(score)))
    if quiz.type_ == 'positivity':
        message = update.message.text
        quiz_storage.save_answer(quiz, len(message))
        if quiz.question_number == 1:
            datalog_storage.save_goodevent(update.message.chat_id, good_event=message)
            bot.send_message(chat_id=update.message.chat_id, text=texts.POSITIVE_LOG[lang][1])
        if quiz.question_number ==2:
            datalog_storage.save_emotion(update.message.chat_id, emotion=message)
            bot.send_message(chat_id=update.message.chat_id, text=texts.POSITIVE_LOG[lang][2])
        if quiz.question_number == 3:
            datalog_storage.save_meaning(update.message.chat_id, meaning=message)
            bot.send_message(chat_id=update.message.chat_id, text="You are done!")




def periodic_notifiction_callback(bot, job):
    for chat in chat_storage.get_chats():
        if chat['frequency'] == 'none':
            continue
        created_at = datetime.strptime(chat['created_at'], '%Y-%m-%d %H-%M-%S')
        now = datetime.now()
        if created_at.hour != now.hour:
            continue
        if (chat['frequency'] == 'weekly') and (now.weekday() != created_at.weekday()):
            continue
        try:
            bot.send_message(chat_id=chat['id'], text=texts.PERIODIC_NOTIFICATION[chat['language']])
        except BadRequest:
            pass

fp = open("cbttips.txt")
data = fp.read()
tips_library =re.split("_", data)


def send_one_tip(bot, update):
    restriction = len(tips_library)
    chat = chat_storage.get_or_create(update.message.chat_id)
    num = chat['tips_id']
    if num<restriction:
        bot.send_message(chat_id=update.message.chat_id, text = tips_library[num])
        chat['tips_id'] += 1
        chat_storage.save(chat)
    else:
        chat['tips_id'] = 0
        num = chat['tips_id']
        chat_storage.save(chat)
        bot.send_message(chat_id=update.message.chat_id, text = tips_library[num])




def daily_tips(bot, update):
    for chat in chat_storage.get_chats():
        try:
            bot.send_message(chat_id=chat['id'], text=texts.PERIODIC_TIPS[chat['language']])
        except BadRequest:
            pass

def export(bot, update):
    keyboard = [[InlineKeyboardButton('PNG', callback_data='png'), InlineKeyboardButton('CSV', callback_data='csv')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    lang = chat_storage.get_or_create(update.message.chat_id)['language']
    bot.send_message(text=texts.EXPORT[lang], reply_markup=reply_markup, chat_id=update.message.chat_id)


def process_export(bot, update):
    query = update.callback_query
    bot.edit_message_text(
        text="{} {}".format(query.message.text, query.data), chat_id=query.message.chat_id,
        message_id=query.message.message_id)
    if query.data == 'png':
        quizes = quiz_storage.get_completed_quizes(query.message.chat_id, order='DESC')
        plot = get_quizes_plot(quizes)
        bot.send_photo(chat_id=query.message.chat_id, photo=plot)
    if query.data == 'csv':
        quizes = quiz_storage.get_completed_quizes(query.message.chat_id, limit=999)
        csv_buf = get_csv(quizes)
        bot.send_document(chat_id=query.message.chat_id, document=csv_buf, filename='m00d.csv')

def positivity_quiz(bot, update):
    quiz = quiz_storage.create_quiz(update.message.chat_id, 'positivity')
    lang = chat_storage.get_or_create(update.message.chat_id)['language']
    bot.send_message(text=texts.POSITIVELOG_INTRO[lang], chat_id=update.message.chat_id)
    bot.send_message(text=texts.POSITIVE_LOG[lang][0], chat_id=update.message.chat_id)
    datalog = datalog_storage.create(update.message.chat_id)


class MQBot(telegram.bot.Bot):

    """ A subclass of Bot which delegates send method handling to MQ """

    def __init__(self, *args, is_queued_def=True, mqueue=None, **kwargs):
        super(MQBot, self).__init__(*args, **kwargs)
        self._is_messages_queued_default = is_queued_def
        self._msg_queue = mqueue or mq.MessageQueue()

    def __del__(self):
        self._msg_queue.stop()
        super(MQBot, self).__del__()

    @mq.queuedmessage
    def send_message(self, *args, **kwargs):
        return super(MQBot, self).send_message(*args, **kwargs)

    @mq.queuedmessage
    def edit_message_text(self, *args, **kwargs):
        return super().edit_message_text(*args, **kwargs)


if __name__ == '__main__':
    quiz_storage = QuizStorage(os.environ.get('DB_NAME'))
    chat_storage = ChatStorage(os.environ.get('DB_NAME'))
    datalog_storage = DatalogStorage(os.environ.get('DB_NAME'))

    q = mq.MessageQueue(all_burst_limit=30, all_time_limit_ms=3000)
    request = Request(con_pool_size=8)
    m00dbot = MQBot(os.environ.get('TG_TOKEN'), request=request, mqueue=q)
    updater = Updater(bot=m00dbot)
    dispatcher = updater.dispatcher
    updater.job_queue.run_repeating(periodic_notifiction_callback, interval=3600, first=0)
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(CallbackQueryHandler(process_lang, pattern='(en|ru)'))
    updater.dispatcher.add_handler(CallbackQueryHandler(process_frequency, pattern='(none|daily|weekly)'))
    start_hars_quiz_handler = CommandHandler('selfesteem', hars_quiz)
    dispatcher.add_handler(start_hars_quiz_handler)

    start_readiness_eval_handler = CommandHandler('amiready', amiready_quiz)
    dispatcher.add_handler(start_readiness_eval_handler)

    updater.job_queue.run_repeating(daily_tips, timedelta(minutes=1))
    start_tips = CommandHandler('tips', send_one_tip)
    dispatcher.add_handler(start_tips)

    track_positivity_handler = CommandHandler('positiveEvent', positivity_quiz)
    dispatcher.add_handler(track_positivity_handler)

    handle_messages = MessageHandler(Filters.text, process_message)
    dispatcher.add_handler(handle_messages)
    updater.dispatcher.add_handler(CallbackQueryHandler(process_answer, pattern='\d+'))  # noqa
    export_handler = CommandHandler('export', export)
    dispatcher.add_handler(export_handler)
    updater.dispatcher.add_handler(CallbackQueryHandler(process_export, pattern='(png|csv)'))
    updater.start_polling()
