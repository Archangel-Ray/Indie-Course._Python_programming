n = int(input("Введите число: "))  # число
the_next_index = 1  # индекс
list_of_answers = list()  # список ответов

while the_next_index * the_next_index <= n:  # перебор чисел от 1 до √n
    if n % the_next_index == 0:  # Если индекс является делителем числа
        list_of_answers.append(the_next_index)  # добавить индекс в ответы
        if the_next_index != n // the_next_index:  # нахождение парного делителя
            list_of_answers.append(n // the_next_index)  # добавить парный делитель
    the_next_index += 1  # Переход к следующему индексу

list_of_answers.sort()  # сортировка ответов
print(*list_of_answers)  # отображение ответов
print(len(list_of_answers))
