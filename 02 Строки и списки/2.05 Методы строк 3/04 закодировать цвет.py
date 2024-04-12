"""
Ваша задача закодировать три поступающих оттенка в RGB код
Входные данные

Программе поступают последовательно три числа: значения оттенка красного, потом зеленого и затем синего цветов.
    Данные числа варьируются от 0 до 255 включительно

Выходные данные
    Ваша задача закодировать оттенки цветов согласно RGB модели.
    Не забывайте, что на каждый цвет всегда должно отводиться два разряда. Символы букв в шестнадцатеричной системе
    необходимо записывать в верхнем регистре.

Примечание: для перевода в 16-ую систему вы можете воспользоваться функцией hex, она возвращает строку
            перевода в 16ую систему, впереди которой находятся два служебных знака 0x
"""
print("#", end="")
for num in input(), input(), input():
    print(hex(int(num))[2:].upper().rjust(2, "0"), end="")
