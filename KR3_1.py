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
# последней стадии созревания
class Tomato:
    states = {1: 'Зелёный', 2: 'Жёлтый', 3: 'Красный'}
    def __init__(self, a):
        self._index = a
        self._state = Tomato.states[1]
    def grow(self):
        return Tomato.states[self._index]

    def is_ripe(self):
        if Tomato.grow(self) == 'Красный':
            print('Томат созрел')
        else:
            print('Томат ещё не созрел')
tomat1 = Tomato(1)
tomat2 = Tomato(2)
tomat3 = Tomato(3)
tomat1.is_ripe()
tomat2.is_ripe()
tomat3.is_ripe()

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
        self.tomatoes = [tomat1, tomat2, tomat3]
    def grow_all(self):
        if tomat1 != 3:
            tomat1 += 1
    def all_are_ripe(self):
        if TomatoBush.grow_all(self) == 3:
            return True
    def give_away_all(self):
        pass












