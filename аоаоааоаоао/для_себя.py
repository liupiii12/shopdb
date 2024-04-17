#Login = "myCompany"
#Password = "07120907777"
#Login_input = input("Введите логин:")
#Password_input = input("Введите пароль:")
#if Login_input != Login or Password_input != Password:
#    print("Неверный логин и пароль")
#elif  Login_input == Login and Password_input != Password:
#    print("Неверный пароль")
#elif Password_input == Password and Login_input != Login:
#    print("Неверный логин")
#else:
#    print("Доступ разрещён")
#    print("Всем привет и если вы вошли сюда значит вы знакомы со мной лично иначе вы бы сюда не попали.Так вот это пока бета версия моего сайта и догин с паролем я вскоре изменю и исправлю недачёты")
#
#
#
#
#class Myclass:
#    def __init__(self,name,age,ip):
#        self.name = name
#        self.age = age
#        self.ip = ip
#people = Myclass('Саша' , '18' , '1123213')
#print(f'Имя: {people.name}')
#
#
#class Stimyl:
#    def __init__(self, name,age):
#        self.name = name
#        self.age = age
#        print(f'Привет меня зовут {self.name}')
#        print(f'Мой возраст {self.age}')
#
#class inst(Stimyl):
#    def __init(self,name,age):
#        super().__init__(name,age)
#    def wolk(self):
#        print(f'Человек {self.name} сейчас идёт')
#people = inst(name='Марк' , age= 19)
#peopp = Stimyl(name='Макисм' , age=22)
#people.intruduce()
#peopp.intruduce()
##
#
#class People:
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#    def intruduce(self):
#        print(f'Привет, меня зовут {self.name} , мой возраст {self.age}')
#    def programmer(self):
#        print(f'{self.name} сейчас пишет сайт')
#        
#class it(People):
#    def __init__(self, name, age):
#        super().__init__(name, age)
#    def walk(self):
#        print(f'{self.name} после программирования идёт на прогулку!')
#class ph(it):
#    def __init__(self, name, age):
#        super().__init__(name, age) 
#    def site(self):
#        print(f'Привет меня зовут {self.name}, мой возраст {self.age}')
#        print(f'{self.name} занимается фронтент разработкой сайта')
#    def otd(self):
#        print(f'{self.name} отдыхвет с друзьями после рабочего дня')
#       
#human = it(name = 'Mаксим', age = 14)
#human.intruduce()
#human.programmer()
#human.walk()
#rb = ph(name= 'Федя', age = 27)
#rb.intruduce
#rb.site()
#rb.otd()
#
#
#
from tkinter import*

window = Tk()
window.title('Моё приложение')
window.geometry('1920x1080')

def check():
    lg = 'Mw'
    ps = 'Top'
    r = 1
    if lg != login.get() or ps != pass1.get() or r != robot.get():
        pr = Label(text='Вы не прошли верификацию!'  , font=('Arial' , 30))
        pr.place(x=600, y=200)
    else:
        wh = Label(text='Вы успешно верифицировались!' ,  font=('Arial' , 30))
        wh.place(x=600, y=200)
        window = Tk()
    window.title('Моё приложение')
    window.geometry('1920x1080')
    def check():
        print(name.get(), selected.get(), age.get(), check_state.get())
        label.configure(text= f'        Спасибо')
        label = Label(text = 'Расскажите о себе' , font = ('Arial' , 20) , fg = 'black')
        label.place(x = 200, y = 10)
        about = Message(text = '''Мы рады приветствовать вас в нашей анкете дружбы!
        Пожалуйста, отвечайте на вопросы честно, вся информация останется между нами''',
        font = ('Arial' , 14),width= 680)
        about.place(x = 5 , y = 70)
        name =Entry(width= 30)
        name.place(x = 70 , y = 155)
        lable_name = Label(text = 'ФИО', font = ('Arial' , 15))
        lable_name.place(x = 5, y = 150)
        selected = IntVar()
        rad1 = Radiobutton(text='Мужской', value=1,variable= selected)# выбирает один из вариантов
        rad2 = Radiobutton(text='Женский', value=2,variable= selected)
        rad1.place(x = 10 , y = 200)
        rad2.place(x = 100 , y = 200)
        label_age = Label(text = 'Сколько вам лет?' , font =('Arial' , 15 ))
        label_age.place(x = 5 , y = 250)
        age = Spinbox(from_=0,to=100, width=20)# Спинбокс это метод что бы выбирать возвраст
        age.place(x = 10, y = 300)
        check_state = IntVar()
        check_btn = Checkbutton(text= 'Занимаетесь ли вы прогромированием?', variable= check_state)# чекбатн выбираем несколько вариантов
        check_btn.place(x = 10, y = 350)
        btn = Button(text='Отправить', font= ('Arial' , 10), command= check) # Один раз ткнуть
        btn.place(x=10, y = 400)
    

label = Label(text='Вход', font=('Arial', 25))
label.place(x=900, y=25)

login = Entry(width=100)
login.place(x=190, y=155)
lable_login = Label(text='Введите логин:', font=('Arial', 15))
lable_login.place(x=5, y=150)

pass1 = Entry(width=99)
pass1.place(x=210, y=205)
lable_pass1 = Label(text='Введите пароль:', font=('Arial', 15))
lable_pass1.place(x=5, y=200)

robot = IntVar()
rob1 = Radiobutton(text='Я не робот', value=1, variable=robot)
rob2 = Radiobutton(text='Я робот', value=2, variable=robot)
rob1.place(x=5, y=260)
rob2.place(x=150, y=260)

btn = Button(text='Отправить', font=('Arial', 10), command=check)
btn.place(x=10, y=400)

window.mainloop()
    

        
    