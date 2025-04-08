"""
Напишите самостоятельно программу, которая работает по этому сценарию:
https://pikabu.ru/story/kakoy_yazyik_programmirovaniya_stoit_uchit_pervyim_10747957
и помогает пользователю определиться с языком программирования.
"""

questions = [
    "Delphi",
    [
        "ты тупой?",
        [
            [
                "ты инженер?",
                [
                    [
                        "у тебя есть ноги?",
                        [
                            "C",
                            [
                                "а они тебе нужны?",
                                [
                                    "C++",
                                    "Java",
                                ]
                            ]
                        ]
                    ],
                    [
                        "тебе больше 50?",
                        [
                            "MatLab",
                            "Fortran",
                        ]
                    ]
                ]
            ],
            [
                "очень?",
                [
                    [
                        "ты насмотрелся уроков ХАУДИ ХО?",
                        [
                            [
                                "тебе нравиться Винда?",
                                [
                                    [
                                        "ты этот?",
                                        [
                                            "Perl",
                                            "Swift",
                                        ]
                                    ],
                                    "C#"
                                ],
                            ],
                            "Python"
                        ],
                    ],
                    [
                        "у тебя есть друзья?",
                        [
                            "PHP",
                            [
                                "они тоже тупые?",
                                [
                                    "Ruby",
                                    "JavaScript",
                                ]
                            ],
                        ]
                    ],
                ]
            ]
        ]
    ]
]

print(f"{"выбираем первый язык программирования":-^62}")
print("Хочешь много зарабатывать?")
while isinstance(questions, list):
    questions = questions[input("да или нет? - ") == "да"]
    if isinstance(questions, list):
        print(questions[0])
        questions = questions[1]
    else:
        print("|" + "_" * 60 + "|")
        print(f"|{"твой язык":-^60}|")
        print(f"|{questions:-^60}|")
        print("|" + "_" * 60 + "|")
