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











