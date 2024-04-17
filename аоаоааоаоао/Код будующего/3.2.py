#class Car:
#    def __new__(self,color,model,speed):
#        print(f'Работает метод __new__() для класса {cls}')
#        return super().__new__(cls)     
#        self.color = color
#        self.model = model
#        self.speed = speed
#my_car = Car('Белый', 'Camry', '100')
#print(my_car.__dict__)



#class Captain:
#    __cap = None
#    def __new__(cls, *arg, **kwargs):
#        if cls.__cap is None:
#            cls.__cap = super().__new__(cls)
#        return cls.__cap
#    
#    
#    
#    def __init__(self,name,age,height,weight):
#        self.name = name
#        self.age = age
#        self.height = height
#        self.weight = weight
#cap = Captain(name = 'Чёрная борода', age = 186, height = 210, weight = 100)
#new_cap = Captain(name = 'Джек Воробей', age = 120 , height = 250, weight = 120)

#print(cap)
#print(new_cap)

#print(cap.__dict__)
#print(new_cap.__dict__)


#def __str__(self):
#        return f'Модель машины - {self.model}'   --- ЭТО НУЖНО ЧТОБЫ В КОНСОЛЬ ВЫВЕЛОСЬ ЗНАЧЕНИЕ КОТОРОЕ НАМ НАДО






#class Car:
#    def __init__(self, model):
#        self.model = model
#    def __str__(self):
#        return f'Модель машины - {self.model}'
#    def __repr__(self):
#        return f'Car({self.model})'
#        
#my_car = Car('Део Матиз')
#print(my_car)
#print(repr(my_car))



class MoneyBox:
    def __init__(self, money = 0):
        self.__money = money
    def __repr__(self):
        return f'{self.__money}'
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return MoneyBox(self.__money + other)
        else:
            print('Некоректное сложение')
    def __radd__(self, other):
        return self.__add__(other)
box = MoneyBox(10)
box = box + 10
box += 10
box += 10.52
box += '10'
print(box)

        
        

        


    
    

    