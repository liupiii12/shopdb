class BaseHuman:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def intruduce(self):
        print(f'Привет, меня зовут {self.name}')
        print(f'Мой возвраст: {self.age}')
    def walk(self):
        print(f'{self.name} идёт на прогулку.')
        
        
class Programmer(BaseHuman):
    def __init__(self, name, age, language):
        super().__init__(name,age)
        self.language = language
    def coding(self):
        print(f'Программист {self.name} сейчас пишет код!')
        
        
class BackendProgrammer(Programmer):
    pass
        


human = BaseHuman(name = 'Ваня', age= '77')
proger = Programmer(name= 'Персик', age= '16', language= 'C++')
backproger = BackendProgrammer(name = 'Магамед' , age=24 , language= 'C++')
human.intruduce()
proger.intruduce()
#.coding()
human.coding()
#print(human.__dict__)
#print(proger.__dict__)
#print(backproger.__dict__)
#backproger.walk


#print(issubclass(BackendProgrammer , Programmer))
#print(Programmer.__base__)
#print(BaseHuman.__base__)
