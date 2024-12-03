"""
Ваша программа получает на вход строку, содержащую имя, отчество и фамилию человека

Вам необходимо вывести фамилию и инициалы, как в примерах ниже
"""
first_name, patronymic, last_name = input().split()
print(f"{last_name} {first_name[0]}.{patronymic[0]}.")
