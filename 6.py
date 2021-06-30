a = int(input('Введите результат первого дня: '))
b = int(input('Введите минимальный желаемый результат: '))
day = 1
result = a
while True:
    day += 1
    result = result * 1.1
    if result >= b:
        break
print('Для достижения результата потребуется', day, 'дней.')