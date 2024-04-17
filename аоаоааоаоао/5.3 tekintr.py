#from tkinter import *# вызываем все функции ткинтер
#window = Tk()#класс
#window.title('Добро пожаловать!')# метод который даёт название приложению
#window.geometry('300x400+550+200') # Задаём размер 
#Label = Label(text='Hello', font =('Arial', 20),fg = 'white', bg = 'darkgoldenrod1' ) # Это то что будет в нашем окне text это текст font это шрифт
#Label.place(x = 0, y = 0)#Метод помещает написанное из лэйбл на каком-то месте

#window.mainloop()# команда для запуска приложения ОБЕЗАТЕЛЬНО В КОНЦЕ




from tkinter import*
window =Tk()
window.title('Анкета')
window.geometry('700x500+550+200')
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






window.mainloop()

