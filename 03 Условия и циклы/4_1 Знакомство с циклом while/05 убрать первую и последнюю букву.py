"""
На вход программе поступает слово. Вам необходимо воспроизвести процесс, в котором каждый раз у этого слово будет
пропадать первая и последняя буква. Этот процесс необходимо закончить, когда в слове останется только одна буква
или слово станет пустой строкой. При этом результат каждого этапа нужно выводить
"""
word = input()
while len(word) > 0:
    print(word)
    word = word[1:-1]
