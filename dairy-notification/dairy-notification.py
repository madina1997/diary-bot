from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
import telegram
import requests
import psycopg2
import datetime

# 2) фича которая спрашивает те вопросы из Таблицы типа
# «Что хорошего ты почувствовал, почему и блабла»,
# и записывает это в базу данных

# scan questions from the table or .txt file
# ask (input)
# write it down to the database

emotions = ['радость', 'спокойствие', 'восхищение', 'интерес', 'удивление', 'страх', 'печаль', 'скука', 'гнев']


def notify():
    bot = telegram.Bot(token='912555954: AAFwUF3HYdEVLYDLdo1h95BzxbfGSKdpHXQ')
    try:
        connection = psycopg2.connect(user="",
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="dairy")
        cursor = connection.cursor()
        postgres_select_query = """SELECT * FROM users"""
        cursor.execute(postgres_select_query)
        rows = cursor.fetchall()
        connection.commit()
        for row in rows:
            bot.send_message(chat_id=int(row[0]), text='Не забудь сделать сегодня запись :)')
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()


def start(bot, update):
    chat_id = update.message.chat_id
    try:
        connection = psycopg2.connect(user="",
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="dairy")
        cursor = connection.cursor()
        postgres_insert_query = """INSERT INTO users (chat_id) VALUES (%s) ON CONFLICT DO NOTHING"""
        record_to_insert = (str(chat_id),)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
    bot.send_message(chat_id=chat_id,
                     text='Привет!
Я, бот-дневник, хочу помочь тебе разобраться в себе. Каждый раз, когда ты испытываешь какую-то эмоцию, ты можешь поделиться со мной о ней и ее причине, написав на /record <твоя сегодняшняя эмоция> <причина этой эмоции>. Если ты будешь всегда пробовать анализировать свои эмоции и записывать причину их появления, то вскоре можно будет их проанализировать и, например, понять, что тебя больше всего в жизни мотивирует :) Это, например, может очень хорошо помочь в выборе профессии! Пожалуйста выбирай из данного списка эмоций: радость, спокойствие, восхищение, интерес, удивление, страх, печаль, скука, гнев.')


def save(bot, update, args):
    currentDT = str(datetime.datetime.now())
    chat_id = update.message.chat_id
    if len(args) == 0:
        bot.send_message(chat_id=chat_id,
                         text='Используй команду /record <твоя сегодняшняя эмоция> <причина этой эмоции>. Пожалуйста выбирай из данного списка эмоций: радость, спокойствие, восхищение, интерес, удивление, страх, печаль, скука, гнев.')
    else:
        emotion = args[0]
        reason = ''
        for word in args[1:]:
            reason += word + ' '
        if reason == '' or emotion not in emotions:
            bot.send_message(chat_id=chat_id,
                             text='Используй команду /record <твоя сегодняшняя эмоция> <причина этой эмоции>. Пожалуйста выбирай из данного списка эмоций: радость, спокойствие, восхищение, интерес, удивление, страх, печаль, скука, гнев.')
        else:
            try:
                connection = psycopg2.connect(user="",
                                              password="",
                                              host="127.0.0.1",
                                              port="5432",
                                              database="dairy")
                cursor = connection.cursor()
                query = """SELECT * FROM emotions"""
                cursor.execute(query)
                connection.commit()
                count = cursor.rowcount

                query = """INSERT INTO emotions(entry_id, chat_id, datetimestamp, emotion, reason) VALUES (%s, %s, %s, %s, %s)"""
                record_to_insert = (count + 1, str(chat_id), currentDT, emotion, reason)
                cursor.execute(query, record_to_insert)
                connection.commit()
                count = cursor.rowcount

            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL", error)
            finally:
                if (connection):
                    cursor.close()
                    connection.close()
            bot.send_message(chat_id=chat_id, text='Я сохранил вашу запись')


def get_reasons(bot, update, args):
    chat_id = update.message.chat_id
    if len(args) == 0:
        bot.send_message(chat_id=chat_id,
                         text='Используй команду /reasons <эмоция>. Пожалуйста выбирай из данного списка эмоций: радость, спокойствие, восхищение, интерес, удивление, страх, печаль, скука, гнев.')
    else:
        emotion = args[0]
        if emotion not in emotions:
            bot.send_message(chat_id=chat_id,
                             text='Используй команду /reasons <эмоция>. Пожалуйста выбирай из данного списка эмоций: радость, спокойствие, восхищение, интерес, удивление, страх, печаль, скука, гнев.')
        else:
            try:
                connection = psycopg2.connect(user="",
                                              password="",
                                              host="127.0.0.1",
                                              port="5432",
                                              database="dairy")
                cursor = connection.cursor()
                postgres_select_query = """SELECT reason FROM emotions WHERE chat_id=(%s) AND emotion=(%s)"""
                condition = (str(chat_id), emotion)
                cursor.execute(postgres_select_query, condition)
                rows = cursor.fetchall()
                connection.commit()
                cnt = 1
                out = ''
                for row in rows:
                    out = out + str(cnt) + '. ' + row[0] + '\n'
                    cnt += 1

            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL", error)

            finally:
                if (connection):
                    cursor.close()
                    connection.close()

    if out == '':
        bot.send_message(chat_id=chat_id, text='У меня нет записей по данной эмоции')
    else:
        bot.send_message(chat_id=chat_id, text=out)

def main():
    updater = Updater('912555954: AAFwUF3HYdEVLYDLdo1h95BzxbfGSKdpHXQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', start))
    dp.add_handler(MessageHandler(Filters.text, start))
    dp.add_handler(CommandHandler('record', save, pass_args=True))
    dp.add_handler(CommandHandler('reasons', get_reasons, pass_args=True))
    # dp.add_handler(CюommandHandler('stats', get_emotion_statistics))
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()


