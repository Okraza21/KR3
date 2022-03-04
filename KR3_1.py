class Tomato:
    states = {0: 'Расток', 1: 'Зелёный', 2: 'Жёлтый', 3: 'Красный'}
    def __init__(self, a):
        self._index = a
        self._state = 0
    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        if self._state == 3:
            print('Томат созрел')
        else:
            print('Томат ещё не созрел')


class TomatoBush:
    def __init__(self, kol_tomat):
        self.tomatoes = [Tomato(i) for i in range(0, kol_tomat)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    def work(self):
        print('Садовник в процессе')
        self._plant.grow_all()
        print("Садовник закончил работу")
    def harvest(self):
        print('Не все плоды созрели!')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Все плоды созрели')
    @staticmethod
    def knowledge_base():
        print('''Начальной стадией помидора является - расток.
Характерными чертами первой стадии является зелёный плод. 
На второй стадии плод желтеет.
Третья стадия является заключительной. Плод имеет красный цвет и его можно употреблять в пищу.''')

if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.work()
    gardener.harvest()











