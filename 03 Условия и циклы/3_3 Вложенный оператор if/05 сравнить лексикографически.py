"""
Маленький Петя очень любит подарки. Его мама подарила ему на день рождения две строки равной длины,
состоящие из больших и маленьких букв латинского алфавита. Теперь Петя хочет сравнить эти строки
лексикографически. При этом регистр букв значения не имеет, то есть большая буква считается
эквивалентной соответствующей маленькой букве. Помогите Пете выполнить сравнение.

Входные данные
В каждой из первых двух строк записано по одной подаренной строке.
Длина строк находится в пределах от 1 до 100 включительно.
Гарантируется, что строки имеют одинаковую длину, а также
состоят из больших и маленьких букв латинского алфавита.

Выходные данные
Если первая строка меньше второй, выведите «-1».
Если вторая строка меньше первой, выведите «1».
Если строки равны, выведите «0».
Учтите, что регистр букв не учитывается при сравнении.
"""
first, second = input().lower(), input().lower()
if first == second:
    print(0)
else:
    if first > second:
        print(1)
    else:
        print(-1)
