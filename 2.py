input = int(input('Введите необходимое время - '))
sec = input % 60
min = int(input / 60)
h = int(min / 60)
min = min % 60
print('Необходимое время -', h, ':', min, ':', sec)
