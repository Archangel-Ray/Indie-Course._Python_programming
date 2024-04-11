"""
Программа принимает на вход три символа через пробел в одну строку.
Необходимо вывести код каждого символа при помощи функции ord в определенном формате.
"""
letters = input().split()
for letter in letters:
    print(f"Simvol code {letter} is {ord(letter)}.")
