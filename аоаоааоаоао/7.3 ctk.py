from customtkinter import*
window = CTk()
window.title('Моё окно')
window.geometry('400x300+550+200')
def clicker():
    global count_clicks
    count_clicks += 1
    label2.configure(text = f'Количество нажатий {count_clicks}')

window.columnconfigure(index=(0),weight=1)
window.rowconfigure(index=(0,1,2,3), weight=1)
label = CTkLabel(window,text='Нажми и увеличь счёт ', text_color='green',fg_color= 'white',  corner_radius=5)
label.grid(row = 0, column = 0)
label.cget('font').configure(size=20)

count_clicks = 0
label2 = CTkLabel(window,text=f'Количествр нажатий {count_clicks}', text_color='green',fg_color= 'white', corner_radius=5)
label2.grid(row = 1, column = 0)
label2.cget('font').configure(size=20)


button = CTkButton(window, text='Кнопка', fg_color='blue', command=clicker )
button.grid(row= 2, column = 0, padx=20,pady=20,sticky='we')

checkbox_1 = CTkCheckBox(window,text='Вариант 1')
checkbox_1.grid(row = 3, column = 0)

checkbox_frame = CTkFrame(window)
checkbox_frame.grid(row = 3, column = 0)
checkbox_frame.grid_columnconfigure((0), weight=1)
checkbox_frame.grid_rowconfigure((0,1), weight=1)
checkbox_1 = CTkCheckBox(checkbox_frame, text = 'Вариант 1')
checkbox_1.grid(row=0, column= 0)
checkbox_2 = CTkCheckBox(checkbox_frame, text = 'Вариант 2')
checkbox_2.grid(row=1, column= 0)
window.mainloop()
