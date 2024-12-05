"""
Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том,
являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами.

Программа должна выводить YES, когда клетки одного цвета, NO - разного. Гарантируется, что значение колонок это
латинские буквы abcdefgh, а строки это символы цифр от 1-8
"""
white_cells = list()
black_cells = list()
for row in "aceg":
    for column in "12345678":
        if len(white_cells) != len(black_cells):
            white_cells.append(row + column)
        else:
            black_cells.append(row + column)

for row in "bdfh":
    for column in "12345678":
        if len(white_cells) != len(black_cells):
            black_cells.append(row + column)
        else:
            white_cells.append(row + column)

first_cell = input()
second_cell = input()
if first_cell in white_cells and second_cell in white_cells or first_cell in black_cells and second_cell in black_cells:
    print("YES")
else:
    print("NO")
