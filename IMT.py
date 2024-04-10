w_ = float(input('Введите вес в кг:    '))
l_ = float(input('Введите рост в см:    '))

def imt():
    print('Индекс массы тела: ',w_ /(l_/100) ** 2 )

imt()