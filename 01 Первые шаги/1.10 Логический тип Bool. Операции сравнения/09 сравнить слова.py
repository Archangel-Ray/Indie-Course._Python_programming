"""
На вход поступают два слова.

Программа должна вывести True, если хотя бы одно слово равно слову "awesome".

Сделать задачу необходимо без использования условного оператора.
"""
awesome = "awesome"
word1, word2 = (input() for _ in range(2))
print(word1 == awesome or word2 == awesome)
