from random import randint
print("Введите кол-во цифр")
num = int(input())
sumpolojitelnyh = 0
sumotricatelnyh = 0
spisok = []
for i in range(num):
    rnd = randint(-100, 100)
    if rnd == 0:
        while rnd == 0:
            rnd = randint(-100, 100)
    if rnd > 0:
        sumpolojitelnyh = sumpolojitelnyh + rnd
    elif rnd < 0:
        sumotricatelnyh = sumotricatelnyh + rnd
    spisok.append(rnd)
print("Сумма положительных чисел равна: ", sumpolojitelnyh)
print("Сумма отрицательных чисел равна: ", sumotricatelnyh)
print("Список всех чисел: ", spisok)
