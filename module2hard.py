def shifr():
    number = int(input("Введите число от 3 до 20:"))
    if number < 3 or number > 20:
        print('Ошибка')
        return
    otvet = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                otvet += str(i) + str(j)
    return otvet
print(shifr())