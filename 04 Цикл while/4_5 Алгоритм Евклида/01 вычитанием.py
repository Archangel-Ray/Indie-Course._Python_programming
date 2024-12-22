"""
Даны два натуральных числа A и B. Требуется найти их наибольший общий делитель (НОД) методом вычитания
"""
list_of_data = list()
for x in range(2):
    list_of_data.append(int(input("нужно целое число: ")))
while list_of_data[0] != list_of_data[1]:
    if list_of_data[0] < list_of_data[1]:
        list_of_data[1] = list_of_data[1] - list_of_data[0]
    else:
        list_of_data[0] = list_of_data[0] - list_of_data[1]
print(list_of_data[0])
