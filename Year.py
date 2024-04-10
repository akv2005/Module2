while 2 < 4:
    year_ = int(input('Введите год    '))
    if year_ % 4 == 0 and year_ % 100 != 0 or year_ % 400 == 0:
        print(year_, ' - Год высокосный')
    else:
        print(year_, 'Год невысокосный')