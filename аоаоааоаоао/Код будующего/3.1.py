class Car:
    def __init__(self,color,model,speed=0):
        self.color = color #public
        self._speed = speed #protected
        self.__model = model # private
    def show_info(self):
        print(f'цвет: {self.color}')
        print(f'скорость: {self._speed}')
        print(f'модель: {self.__model}')
my_car = Car(color='Синий',speed = 10,model='Урал')
my_car.show_info()
#print(my_car.color)
#print(my_car._speed)
#print(my_car._Car__model)
        
        