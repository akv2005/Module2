weight_ = float(input('Введите вес    '))
if weight_ <= 2:
    print('Стоимость посылки: 50 рублей')
if 2 < weight_ <= 10:
    print('Стоимость посылки: ', 50 + 20 * int(weight_ - 2))
if weight_ > 10:
    print('Стоимость посылки: 200 рублей')
