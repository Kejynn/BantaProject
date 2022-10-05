# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint
print("Введите количество цифр")
num = int(input())
summa_pol = 0
summa_otr = 0
spisok = []
for i in range(num):
    rnd = randint(-100, 100)
    if rnd == 0:
        while rnd == 0:
            rnd = randint(-100, 100)
    if rnd > 0:
        summa_pol = summa_pol + rnd
    elif rnd < 0:
        summa_otr = summa_otr + rnd
    spisok.append(rnd)
print("Сумма положительных чисел: ", summa_pol)
print("Сумма отрицательных чисел: ", summa_otr)
print("Весь список чисел: ", spisok)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
