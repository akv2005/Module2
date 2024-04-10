import random

xx = random.randrange(1, 100)
while(xx<100):
    nn = int(input('Введите чило от 1 до 100 '))
    if xx < nn:
        print('Ваше число больше')
    if xx > nn:
        print('Ваше число меньше')
    if xx == nn:
        print('Угадали', xx)
        break