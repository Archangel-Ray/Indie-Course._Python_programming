"""
Дано натуральное число N. Определить, является ли оно простым. Натуральное число N называется простым, если у него есть
только два делителя: единица и само число N.

В качестве ответа выведите "Yes", если число простое, "No" - в противном случае.
"""
n = int(input())
i = 1
natural_divisors = list()
if n == 1:
    print("No")
else:
    while i * i <= n:
        if n % i == 0:
            natural_divisors.append(i)
            if i != n // i:
                natural_divisors.append(n // i)
        i += 1
    if len(natural_divisors) > 2:
        print("No")
    else:
        print("Yes")
