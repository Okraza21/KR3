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

# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)



# class Tomato:
#     states = {'Зелёный': 1, 'Жёлтый': 2, 'Красный': 3}
#     def __init__(self, a=input('Введите цвет томата "Зелёный", "Жёлтый", "Красный": ')):
#         self._index = a
#         self._state = Tomato.states['Зелёный']
#     def grow(self):
#         return Tomato.states[self._index]
#
#     def is_ripe(self):
#         if Tomato.grow(self) == 3:
#             print('Томат созрел')
#         else:
#             print('Томат ещё не созрел')
# tomat = Tomato()
# tomat.is_ripe()


class Tomato:
    states = {'Зелёный': 1, 'Жёлтый': 2, 'Красный': 3}
    def __init__(self, a=input('Какого цвета томат? : "Зелёный", "Жёлтый", "Красный"\nВвод: ')):
        self._index = a
        self._state = Tomato.states['Зелёный']
    def grow(self):
        return Tomato.states[self._index]

    def is_ripe(self):
        if Tomato.grow(self) == 3:
            print('Томат созрел')
        else:
            print('Томат ещё не созрел')
tomat = Tomato()
tomat.is_ripe()

# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая

class TomatoBush:
    def __init__(self, kol_tomat):
        self.kol_tomat = kol_tomat











