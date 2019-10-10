AMIREADY_QUESTIONS = {
    "ru": {
        "questions": "Что-нибудь еще?",
        "answers": ["Еще одно", "Всё"],
        "low": {
            "plus": "Напиши одно достоинство твоей низкой самооценки",
            "minus": "Напиши один недостаток твоей низкой самооценки"
        },
        "high": {
            "plus": "Напиши одно достоинство твоей будущей здоровой самооценки",
            "minus": "Напиши один недостаток твоей будущей здоровой самооценки"
        }
    },
    "en": {
        "questions": "Something else?",
        "answers": ["One more", "That's all"],
        "low": {
            "plus": "Write one advantage of your low self-esteem",
            "minus": "Write one disadvantage of your low self-esteem"
        },
        "high": {
            "plus": "Write one advantage of the new positive core belief",
            "minus": "Write one disadvantage of the new positive core belief"
        }
    }
}
HARS_QUESTIONS = {
    "ru": {
        "answers": ["Полностью согласен", "Согласен", "Не согласен", "Полностью не согласен"],
        "questions": [
            "В целом, я доволен/-на собой",
            "Порой я думаю, что я никчемный/-ая",
            "Я считаю, что у меня много хороших качеств",
            "Я способен/-на выполнять задания так же хорошо, как и окружающие меня люди",
            "Мне кажется, мне нечем гордиться",
            "Я часто чувствую себя бесполезным/-ной",
            "Я достойный человек. Как минимум, наравне с окружающими меня людьми.",
            "Мне хочется, чтобы меня больше уважали",
            "Я склонен/-на думать, что я неудачник/-ца",
            "Я отношусь к себе позитивно"
        ],
        "answers_weight": [
            [3, 2, 1, 0],
            [0, 1, 2, 3],
            [3, 2, 1, 0],
            [3, 2, 1, 0],
            [0, 1, 2, 3],
            [0, 1, 2, 3],
            [3, 2, 1, 0],
            [0, 1, 2, 3],
            [0, 1, 2, 3],
            [3, 2, 1, 0]
        ]
        # answers_weight[question_number][answers[i]]
    },
    "en": {
        "answers": ["Strongly agree", "Agree", "Disagree", "Strongly disagree"],
        "questions": [
            "On the whole, I am satisfied with myself",
            "At times I think I am no good at all",
            "I feel that I have a number of good qualities",
            "I am able to do things as well as most other people",
            "I feel I do not have much to be proud of",
            "I certainly feel useless at times",
            "I feel that I am a person of worth, at least on an equal plane with others",
            "I wish I could have more respect for myself",
            "All in all, I am inclined to feel that I am a failure",
            "I take a positive attitude towards myself"
        ],
        "answers_num": [
            "3, 2, 1, 0",
            "0, 1, 2, 3",
            "3, 2, 1, 0",
            "3, 2, 1, 0",
            "0, 1, 2, 3",
            "0, 1, 2, 3",
            "3, 2, 1, 0",
            "0, 1, 2, 3",
            "0, 1, 2, 3",
            "3, 2, 1, 0"
        ]
    }
}

# print(HARS_QUESTIONS["ru"]['answers_weight'][0][0])

MADRS_QUESTIONS = {
    "ru": [
        {
            "question": "Объективные (видимые) признаки подавленности. Проявления угнетенности, уныния, отчаяния (более выраженных, чем при обычном временном снижении настроения) в речи, в мимике и позе. Оцениваются в соответствии с глубиной снижения настроения.",
            "answers": ["0 = отсутствие", "1 =", "2 = выглядит подавленным, но настроение легко улучшается", "3 =", "4 = выглядит подавленным и несчастным большую часть времени", "5 =", "6 = выглядит крайне подавленным и угнетенным все время"]
        },
        {
            "question": "Субъективные признаки подавленности. Сообщение пациента о депрессивном настроении независимо от того, насколько оно проявляется внешними признаками. Включает упадок духа, угнетенность или чувство беспомощности и безнадежности. Оценивается в соответствии с интенсивностью, продолжительностью и степенью того, насколько, по описанию пациента, сниженное настроение связано с внешними событиями.",
            "answers": ["0 = эпизодическая подавленность, связанная с внешними обстоятельствами", "1 =", "2 = печальное или подавленное настроение, легко поддающееся улучшению", "3 =", "4 = глубокое чувство угнетенности или уныния; настроение еще подвержено влиянию внешних событий", "5 =", "6 = постоянное и неизменное чувство подавленности, отчаяния или угнетенности"]
        },
        {
            "question": "Внутреннее напряжение. Чувство болезненного дискомфорта, смятения, раздражения, психического напряжения, доходящего до паники, сильного страха или душевной боли.",
            "answers": ["0 = спокойное состояние; только чувство внутреннего напряжения", "1 =", "2 = эпизодическое чувство раздражения или болезненного дискомфорта", "3 =", "4 = постоянное чувство внутреннего напряжения, периодическая паника, преодолеваемая больным с большим трудом", "5 =", "6 = неослабевающий крайне выраженный страх или душевная боль; непреодолимая паника"]
        },
        {
            "question": "Недостаточный сон. Уменьшение продолжительности или глубины сна в сравнении с привычными для пациента характеристиками сна.",
            "answers": ["0 = обычный сон", "1 =", "2 = незначительно затрудненное засыпание или несколько укороченный, поверхностный или прерывистый сон", "3 =", "4 = укороченный сон, не менее 2 часов", "5 =", "6 = менее 2-3 часов сна"]
        },
        {
            "question": "Снижение аппетита Утрата аппетита. Оценивается в соответствии со степенью утраты желания поесть или усилий заставить себя принять пищу.",
            "answers": ["0 = нормальный или повышенный аппетит", "1 =", "2 = несколько сниженный аппетит", "3 =", "4 = отсутствие аппетита; пища не имеет вкуса", "5 =", "6 = необходимость принуждения для приема пищи"]
        },
        {
            "question": "Нарушение концентрации внимания. Трудности собраться с мыслями вплоть до утраты способности сконцентрироваться. Оценивается в соответствии с интенсивностью, частотой и степенью утраты способности концентрировать внимание.",
            "answers": ["0 = нет нарушений концентрации", "1 =", "2 = эпизодически трудно собраться с мыслями", "3 =", "4 = затруднения концентрации и длительного сосредоточения со снижением способности читать или поддерживать разговор", "5 =", "6 = утрата способности читать или участвовать в разговоре без значительных усилий"]
        },
        {
            "question": "Апатия. Затруднения начать какую-либо деятельность или замедленность начала и выполнения повседневной деятельности.",
            "answers": ["0 = отсутствие затруднения начать какую-либо деятельность; отсутствие замедленности", "1 =", "2 = затруднения начать какую-либо деятельность", "3 =", "4 = затруднения начать простую повседневную деятельность, выполнение которых требует дополнительных усилий", "5 =", "6 = полная апатия; неспособность выполнить что-либо без посторонней помощи"]
        },
        {
            "question": "Утрата способности чувствовать. Субъективное ощущение снижения интереса к окружающему или деятельности, обычно доставляющим удовольствие. Снижение способности адекватно эмоционально реагировать на внешние события или людей",
            "answers": ["0 = нормальный интерес к окружающему и людям", "1 =", "2 = снижение способности получать удовольствие от того, что обычно интересно", "3 =", "4 = утрата интереса к окружающему; утрата чувств к друзьям и знакомым", "5 =", "6 = ощущение эмоционального паралича, утраты способности испытывать гнев, печаль или удовольствие, полной или даже болезненной утраты чувств к близким и друзьям"]
        },
        {
            "question": "Пессимистические мысли. Идеи собственной вины, малоценности, самоуничижения, греховности или раскаяния",
            "answers": ["0 = отсутствие пессимистических мыслей", "1 =", "2 = эпизодические идеи неудачливости в жизни, самоуничижения или малоценности", "3 =", "4 = постоянное самообвинение или конкретные, но еще рациональные, идеи виновности или греховности; нарастающая пессимистическая оценка будущего", "5 =", "6 = бредовые идеи полного краха, раскаяния или неискупимого греха; абсурдное и непоколебимое самообвинение"]
        },
        {
            "question": "Суицидальные мысли. Чувство, что жить больше не стоит, что естественная смерть – желаемый исход; суицидальные мысли и приготовления к самоубийству.",
            "answers": ["0 = жизнь приносит удовольствие или воспринимается такой, какая она есть", "1 =", "2 = усталость от жизни; эпизодические мысли о самоубийстве", "3 =", "4 = возможно лучше умереть; суицидальные мысли становятся привычными, а самоубийство рассматривается как возможный способ решения проблем при отсутствии конкретных суицидальных планов или намерений", "5 =", "6 = конкретное планирование совершения самоубийства при первой возможности; активные приготовления к самоубийству"]
        }
    ],
    "en": [
        {
            "question": "Apparent Sadness. Representing despondency, gloom and despair, (more than just ordinary transient low spirits) reflected in speech, facial expression, and posture. Rate by depth and inability to brighten up",
            "answers": ["0 = No sadness", "1 =", "2 = Looks dispirited but does brighten up without difficulty", "3 =", "4 = Appears sad and unhappy most of the time", "5 =", "6 = Looks miserable all the time. Extremely despondent"]
        },
        {
            "question": "Reported Sadness. Representing reports of depressed mood, regardless of whether it is reflected in appearance or not. Includes low spirits, despondency or the feeling of being beyond help and without hope. Rate according to intensity, duration and the extent to which the mood is reported to be influenced by events",
            "answers": ["0 = Occasional sadness in keeping with the circumstances", "1 =", "2 = Sad or low but brightens up without difficulty", "3 =", "4 = Pervasive feelings of sadness or gloominess. The mood is still influenced by external circumstances", "5 =", "6 = Continuous or unvarying sadness, misery or despondency"]
        },
        {
            "question": "Inner Tension. Representing feelings of ill-defined discomfort, edginess, inner turmoil, mental tension mounting to either panic, dread or anguish. Rate according to intensity, frequency, duration and the extent of reassurance called for",
            "answers": ["0 = Placid. Only fleeting inner tension", "1 =", "2 = Occasional feelings of edginess and ill-defined discomfort", "3 =", "4 = Continuous feelings of inner tension or intermittent panic which the patient can only master with some difficulty", "5 =", "6 = Unrelenting dread or anguish. Overwhelming panic"]
        },
        {
            "question": "Reduced Sleep. Representing the experience of reduced duration or depth of sleep compared to the subject’s own normal pattern when well",
            "answers": ["0 = Sleeps as usual", "1 =", "2 = Slight difficulty dropping off to sleep or slightly reduced, light or fitful sleep", "3 =", "4 = Sleep reduced or broken by at least two hours", "5 =", "6 = Less than two or three hours sleep"]
        },
        {
            "question": "Reduced Appetite. Representing the feeling of a loss of appetite compared with when well. Rate by loss of desire for food or the need to force oneself to eat",
            "answers": ["0 = Normal or increased appetite", "1 =", "2 = Slightly reduced appetite", "3 =", "4 = No appetite. Food is tasteless", "5 =", "6 = Needs persuasion to eat at all"]
        },
        {
            "question": "Concentration Difficulties. Representing difficulties in collecting one’s thoughts mounting to incapacitating lack of concentration. Rate according to intensity, frequency, and degree of incapacity produced",
            "answers": ["0 = No difficulties in concentrating", "1 =", "2 = Occasional difficulties in collecting one’s thoughts", "3 =", "4 = Difficulties in concentrating and sustaining thought which reduces ability to read or hold a conversation", "5 =", "6 = Unable to read or converse without great difficulty"]
        },
        {
            "question": "Lassitude. Representing a difficulty getting started or slowness initiating and performing everyday activities",
            "answers": ["0 = Hardly any difficulties in getting started. No sluggishness", "1 =", "2 = Difficulties in starting activities", "3 =", "4 = Difficulties in starting simple routine activities, which are carried out with effort", "5 =", "6 = Complete lassitude. Unable to do anything without help"]
        },
        {
            "question": "Inability to Feel. Representing the subjective experience of reduced interest in the surroundings, or activities that normally give pleasure.The ability to react with adequate emotion to circumstances or people is reduced",
            "answers": ["0 = Normal interest in the surroundings and in other people", "1 = ", "2 = Reduced ability to enjoy usual interests", "3 =", "4 = Loss of interest in the surroundings. Loss of feelings for friends and acquaintances", "5 =", "6 = The experience of being emotionally paralyzed, inability to feel anger, grief or pleasure and a complete or even painful failure to feel for close relatives and friends"]
        },
        {
            "question": "Pessimistic Thoughts. Representing thoughts of guilt, inferiority, self-reproach, sinfulness, remorse and ruin",
            "answers": ["0 = No pessimistic thoughts", "1 =", "2 = Fluctuating ideas of failure, self-reproach or self-depreciation", "3 =", "4 = Persistent self-accusations, or definite but still rational ideas of guilt or sin. Increasingly pessimistic about the future", "5 =", "6 = Delusions of ruin, remorse and unredeemable sin. Self-accusations which are absurd and unshakable"]
        },
        {
            "question": "Suicidal Thoughts. Representing the feeling that life is not worth living, that a natural death would be welcome, suicidal thoughts, and preparations for suicide. Suicidal attempts should not in themselves influence the rating",
            "answers": ["0 = Enjoys life or takes it as it comes", "1 =", "2 = Weary of life. Only fleeting suicidal thoughts", "3 =", "4 = Probably better off dead. Suicidal thoughts are common, and suicide is considered as a possible solution, but without specific plans or intention", "5 =", "6 = Explicit plans for suicide when there is an opportunity. Active preparations for suicide"]
        }
    ]
}
