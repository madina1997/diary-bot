from collections import namedtuple


Question = namedtuple('Question', ['question', 'answers'])


class BaseQuiz:

    def __init__(self, id, questions, lang, is_selfesteem_high, is_positive, question_number=0, answers=None, created_at=None):
        self.id = id
        self.questions = questions
        self.lang = lang
        self.question_number = question_number
        self.answers = [] if answers is None else answers
        self.created_at = created_at
        #ASS
        self.is_selfesteem_high = is_selfesteem_high
        self.is_positive = is_positive

    def get_question(self):
        raise NotImplementedError

    def save_answer(self, answer):
        self.answers.append(answer)
        self.question_number += 1
        # raise NotImplementedError

    def get_result(self):
        raise NotImplementedError

    @property
    def result(self):
        return sum(self.answers)

    @property
    def is_completed(self):
        return self.question_number == self.questions_count

    @property
    def questions_count(self):
        raise NotImplementedError

class AMIREADY_QUIZ(BaseQuiz):

    RESULTS = {
        'ru': ['Аееее, ты готов к курсу! Нажми /track_positivity', 'К сожалению, ты не готов к курсу :( Давай ты попробуешь в след.раз!'],
        'en': ['Yeaaaah, you are ready! Press /track_positivity TO START THE COURSE', 'Unfortunately, you are not ready for the course']
    }

    type_ = 'amiready'


    # def save_answer(self, answer):
    #     self.answers.append(answer)
    #     self.question_number += 1

    def get_answers(self):
        return self.answers

    def get_question(self):
        z =  Question(
            "{}".format(
                self.questions[self.lang]['questions']),
            self.questions[self.lang]['answers'])
        return z

    def get_result(self, score):
        if score <= 0:
            description = self.RESULTS[self.lang][1]
        elif self.result >0:
            description = self.RESULTS[self.lang][0]
        return '{}:\n{}\n{}'.format(
            'Результат' if self.lang == 'ru' else 'Result',
            score, description)



class HARSQuiz(BaseQuiz):

    RESULTS = {
        'ru': ['Очень низкая самооценка. Нажмите на /amiready, чтобы оценить свою готовность к изменениям', 'Низкая самооценка. Нажмите на /amiready, чтобы оценить свою готовность к изменениям', 'Здоровая самооценка. Ты молодец!'],
        'en': ['Very low self-esteem. Press on /amiready to evaluate if you are ready for changes.', 'Low self-esteem. Press on /amiready to evaluate if you are ready for changes.', 'Healthy self-esteem. You are great!']}

    type_ = 'hars'

    def get_question(self):
        return Question(
            "\u2753({}/{}) {}".format(
                (self.question_number + 1), self.questions_count,
                self.questions[self.lang]['questions'][self.question_number]),
            self.questions[self.lang]['answers'])

    def get_answers_weight(self):
        return self.questions[self.lang]['answers_weight'][self.question_number]

    def get_result(self):
        if not self.is_completed:
            raise ValueError("Can't calculate result for incomplete test")
        if self.result <= 15:
            description = self.RESULTS[self.lang][0]
        elif self.result <= 18:
            description = self.RESULTS[self.lang][1]
        else:
            description = self.RESULTS[self.lang][2]
        return '{}:\n{}/{}\n{}'.format(
            'Результат' if self.lang == 'ru' else 'Result',
            self.result, self.questions_count * 4, description)

    @property
    def questions_count(self):
        return len(self.questions[self.lang]['questions'])

class POSITIVE_DATALOG_Quiz(BaseQuiz):
    type_ = 'positivity'

class MADRSQuiz(BaseQuiz):

    RESULTS = {
        'en': ['normal 👍', 'mild depression 😐', 'moderate depression 😔', 'severe depression 😨'],
        'ru': ['норма 👍', 'слабая депрессия 😐', 'умеренная депрессия 😔', 'тяжелая депрессия 😨']}

    type_ = 'madrs'

    def get_question(self):
        return Question(
            "\u2753({}/{}) {}".format(
                (self.question_number + 1), self.questions_count,
                self.questions[self.lang][self.question_number]['question']),
            self.questions[self.lang][self.question_number]['answers'])

    def get_result(self):
        if not self.is_completed:
            raise ValueError("Can't calculate result for incomplete test")
        if self.result <= 6:
            description = self.RESULTS[self.lang][0]
        elif self.result <= 19:
            description = self.RESULTS[self.lang][1]
        elif self.result <= 34:
            description = self.RESULTS[self.lang][2]
        else:
            description = self.RESULTS[self.lang][3]
        return '{}:\n{}/{}\n{}'.format(
            'Результат' if self.lang == 'ru' else 'Result',
            self.result, self.questions_count * 6, description)

    @property
    def questions_count(self):
        return len(self.questions[self.lang])
