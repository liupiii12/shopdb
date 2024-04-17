class Car: # классы называем с заглавной буквы
# передаём характеристики экземпляров этого класса в качестве значений по умолчанию
    brand = 'Ford' # марка
    model = 'Ural' # модель
    color = 'blue' # цвет
    speed = 0 # Якорость
    def set_power_engine(self):
        print('Ура метод set_power_engine работает')
my_car_1 = Car() # создаём объект по образу и подобию класса Car
my_car_2 = Car ()


my_car_1.set_power_engine()