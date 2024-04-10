nn =int(input('Введите мах число:    '))
prime_numbers = []
i = 1
while i < nn+1:
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    else:
        prime_numbers.append(i)
    i += 1
print('Пролстые числа: ', prime_numbers)
