"""
Требуется написать программу, определяющую, является ли четырехзначное натуральное число N палиндромом, т.е. числом,
которое одинаково читается слева направо и справа налево.

Программа получает на вход целое положительное четырехзначное число N и должна вывести YES, если число N является
палиндромом, и NO - если не палиндром.
"""
n = input()
print(["NO", "YES"][n == n[::-1]])
