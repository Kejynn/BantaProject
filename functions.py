a = int(input("Первое число:"))
b = int(input("Второе число:"))
c = int(input("Третье число:"))

def minimum (x, y, z):
    return min(x, y, z)

print("Минимальное число:", (minimum(a, b ,c)))

a = int(input("Первое число:"))

def dlina(x):
    stroka = str(x)
    print("Длина первого числа:", (len(str(x))))

print(dlina(a))


N = int(input("Введите число:"))

def summa(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum
print("Сумма чисел:",(summa(N)))

N = int(input("Введите число:"))

def factorial(n):
    proizv = 1
    for i in range(2, n+1):
        proizv = proizv * i
    return proizv

print("Факториал:",(factorial(N)))







