"""
Программа принимает на вход одно натуральное число. Ваша задачи найти сколько раз встречается цифра 7 в этом числе
"""
number = int(input())
counter = 0
while number > 0:
    if number % 10 == 7:
        counter += 1
    number //= 10
print(counter)
