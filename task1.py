
x = int(input('Введите число:\n'))
hours = x//3600
minutes = (x-hour*3600)//60
seconds = (x-minutes*3600) % 60
print(hours, minutes, seconds)

