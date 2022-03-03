def kard():
    while True:
        try:
            num = int(input('Введите номер карты из 12 цифр: '))
            if len(str(num)) != 12:
                print('Неверный ввод! Повторите попытку!')
            else:
                break
        except ValueError:
            print('Неверный ввод! Введите цифры!')
    rez = []
    for i in str(num):
        rez.append(int(i))
    for j in range(8):
        rez[j] = '*'
    for h in rez:
        ' '.join(str(h))
        print(h, end=' ')

def polindrom():
    while True:
        slovo = input('Введиете слово: ')
        if slovo.isalpha():
            break
    if slovo == slovo[::-1]:
        print('Слово - полиндром!')
    else:
        print('Слово не полиндром(')