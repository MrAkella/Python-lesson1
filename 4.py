num = int(input('Введите целое положительное число - '))
if num < 0:
    print('Введено некорректное число! Попробуйте еще раз.')
    num = int(input('Введите целое положительное число - '))
max = 0
check = num
while check > 0:
    check = num % 10
    if check > max:
        max = check
    num = int(num / 10)
print('Самая большая цифра в вашем числе -', max)
