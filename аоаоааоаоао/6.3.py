#from tkinter import*
#window = Tk()
#window.geometry('300x400+550+200')
#for i in range(2): window.columnconfigure(index=i, weight=1)
#for j in range(2): window.rowconfigure(index=j,weight=1)
#btn1 = Button(text= 'Кнопка 1' ,font= ('Arial' , 15))
#btn1.grid(row = 0, column=0)
#btn2 = Button(text= 'Кнопка 2' ,font= ('Arial' , 15))
#btn2.grid(row = 0, column=1)
#btn3 = Button(text= 'Кнопка 3' ,font= ('Arial' , 15))
#btn3.grid(row = 1, column=0,columnspan=2)# четвёртая строка 7 столбец
#window.mainloop()




from tkinter import*
from random import choice


class Game:
    def __init__(self):
        self.win = 0
        self.lose = 0
        self.draw = 0
        self.moves = ['Камень' , 'Ножницы' , 'Бумага']
        
    def move_result(self, user_choice):
        comp_choice = choice(self.moves)
        if user_choice ==comp_choice:
            self.draw +=1
            return f'Ход игрока: {user_choice}\nХод компьютера: {comp_choice}\nНичья'
        elif (user_choice == 'Камень' and comp_choice == 'Ножницы') or (user_choice== 'Ножницы' and comp_choice == 'Бумага') or (user_choice == 'Бумага' and comp_choice == 'Камень'):
            self.win +=1
            return f'Ход игрока: {user_choice}\nХод компьютера: {comp_choice}\nПобеда'
        else:
            self.lose +=1
            return f'Ход игрока: {user_choice}\nХод компьютера: {comp_choice}\nПоражение'
    def show_info(self):
        return f'Победы: {self.win}\nПроигрыши: {self.lose}\nНичья: {self.draw}'
    
class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x300+550+200')
        self.window.title('Камень Ножницы Бумага')
        self.game = Game()
        self.startUI(self.window)
        self.window.mainloop()
    def startUI(self,window):
            for i in range(3): window.columnconfigure(index=i, weight=1)
            for j in range(3): window.rowconfigure(index=j,weight=1)
            self.btn1 = Button(window,text= 'Камень' ,font= ('Arial' , 15),
                               command=lambda: self.btn_click('Камень'))
            self.btn1.grid(row = 2, column=0)
            self.btn1 = Button(window,text= 'Ножницы' ,font= ('Arial' , 15),
                               command=lambda: self.btn_click('Ножницы'))
            self.btn1.grid(row = 2, column=1)
            self.btn1 = Button(window,text= 'Бумага' ,font= ('Arial' , 15),
                               command=lambda: self.btn_click('Бумага'))
            self.btn1.grid(row = 2, column=2)
            self.label = Button(window, text= 'Начало игры!', font=('Arial' , 20))
            self.label.grid(row = 1 , column= 0, columnspan=3)
            self.label2 =Label(window, text= self.game.show_info(), font=('Arial' , 13),justify='left')
            self.label2.grid(row = 0 , column= 0, columnspan=3)
    def btn_click(self, user_choice):
            self.label['text']= self.game.move_result(user_choice)
            self.label2['text'] = self.game.show_info()
app = GUI()
        
        
    
