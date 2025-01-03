"""
У нас в наличии рюкзак, вместимость которого составляет n литров, и наша задача забить его до предела максимально
возможно. Нам поступают вещи, объем которых измеряется также в литрах, и мы должны их складывать в наш рюкзак
без возможности пропуска. Как только суммарный объем новой добавляемой вещи превысит вместимость рюкзака,
ваша программа должна вывести слово "Довольно!" и затем на отдельных строчках суммарный объем вещей,
которые мы смогли упаковать в рюкзак, и их количество

Входные данные
Число n – вместимость рюкзака. Далее идут произвольное количество строк – объем очередного предмета.

Выходные данные
Строка "Довольно!" и затем два числа – суммарный объем упакованных товаров и их количество.
Каждое значение выводится в отдельной строке.
"""
n = int(input())
filling = count = 0
while n >= (filling + (next_thing := int(input()))):
    filling += next_thing
    count += 1
print("Довольно!", filling, count, sep="\n")
