"""
А вот цифра «5» жителям этого дома очень понравилась. Они считают, что каждого, кто увидит за день десять пятерок,
ждет большая удача. Давайте порадуем этих суеверных людей. Вам будет поступать на вход список чисел, и
ваша задача - дополнить его таким образом, чтобы в нем оказалось десять цифр «5». Добавлять их нужно в конец списка.
Если во входной списке уже было десять «5»-рок, то ничего добавлять не нужно.
Цифры «4» и «7» по-прежнему нужно удалять.
В качестве ответа выведите на экран полученный список.
"""
list_of_numbers = list(map(int, input().split()))
output_list = list()
number_of_five = [5] * 10
for num in list_of_numbers:
    if num in [4, 7]:
        continue
    if num == 5:
        if num in number_of_five:
            number_of_five.remove(5)
    output_list.append(num)
output_list.extend(number_of_five)
print(output_list)
