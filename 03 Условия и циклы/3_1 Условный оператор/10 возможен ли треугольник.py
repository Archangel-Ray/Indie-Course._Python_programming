"""
Даны три натуральных числа a, b, c записанные в отдельных строках. Ваша задача определить, существует ли треугольник
с такими сторонами.

Для этого вспоминаем теорему о существовании треугольника. Она утверждает, что треугольник существует, если сумма любых
двух сторон больше оставшейся третьей.

Выведите строку YES, если условие теоремы выполняется, иначе выведите строку NO.
"""
numbers_list = list()
for _ in range(3):
    numbers_list.append(int(input()))
highest_value = max(numbers_list)
sum_of_smaller_values = sum(numbers_list) - highest_value
print("YES" if highest_value < sum_of_smaller_values else "NO")
