"""
В вашем распоряжении список numbers. Ваша задача удалить из этого списка числа 3, 5, 7 и 9.

 В качестве ответа необходимо вывести измененный список numbers
"""
numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432,
           43, 32, 422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]
for x in [3, 5, 7, 9]:
    numbers.remove(x)
print(numbers)
