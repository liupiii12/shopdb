#Полиморфиз
#Задание 1
#class Rectangl:
#    def __init__(self, length,width):
#        self._length = length
#        self._width = width
#    def get_area(self):
#        return self._length * self._width
#    
#    
#class Triangl:
#    def __init__(self, base,height):
#        self._base = base
#        self._height = height
#    def get_area(self):
#        return (self._base * self._height) / 2
#
#rect1 = Rectangl(1,4)
#rect2 = Rectangl(8,10)
#trian1 = Triangl(6,9)
#trian2 = Triangl(3,5)

#figures = [rect1, rect2, trian1, trian2]
#for fig in figures:
#    print(f'Площадь фигуры {fig.get_area()}')
        
#Задание 2
class Rectangl:
    def __init__(self, length,width):
        self._length = length
        self._width = width
    def get_area(self):
        return self._length * self._width
    def get_perimeter(self):
        return (self._length + self._width) *2
    
    
class Triangl:
    def __init__(self, side1 , side2 , side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
    def get_area(self):
        p = (self._side1+ self._side2+ self._side3)/2
        return (p*(p-self._side1)*(p-self._side2)*(p-self._side3))**0.5
    def get_perimeter(self):
        return self._side1 + self._side2 + self._side3
    
rect1 = Rectangl(1,4)
rect2 = Rectangl(8,10)
trian1 = Triangl(6,9,5)
trian2 = Triangl(3,5,4)

figures = [rect1, rect2, trian1, trian2]
for fig in figures:
    print(f'Площадь фигуры {fig.get_area()}')
    print(f'Переметер фигуры {fig.get_area()}')
    
#Задание 3

class Figure:
    def get_area(self):
        raise NotImplementedError('get_perimeter() нужно переоперделить в дочернем классе')
        
    
    def get_perimeter(self):
        raise NotImplementedError('get_perimeter() нужно переоперделить в дочернем классе')
    
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        
circle = Circle(8)
print(circle.get_area())
print(circle.get_perimeter())
        


        
        


        
        