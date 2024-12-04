"""
На момент написания текста из РФ можно было вывозить не более 10000$ или эквивалент в другой валюте. При превышении
этой суммы необходимо составлять декларацию.

Давайте представим, что сумму выше 10000 долларов таможня забирает себе и вам останется только 10000$.

Давайте напишем такую программу, которая будет принимать целое положительное число - сумма в долларах. Если она
не превышает 10000$, то выводим текст Сумма <значение> не превышает лимит, проходите

Если сумма превышает 10000$ выводим текст Ого! <значение>! Куда вам столько? Мы заберем <разница>

И конечно же нужно использовать сами знаете кого, иначе ваше решение не пройдет
"""
if (pocket := int(input())) <= (limit := 10000):
    print(f"Сумма {pocket} не превышает лимит, проходите")
else:
    print(f"Ого! {pocket}! Куда вам столько? Мы заберем {pocket - limit}")
