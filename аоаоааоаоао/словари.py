#english_dict = {
#    "apple" : "яблоко" ,
#    "milk" : "молоко"}
#word = input("Введите число на англизком")
#if word in english_dict:
#    print(f"Перевод слова {word} на русский язык: {english_dict[word]}")
##else:
#    print("Такого слова нет в словаре")
    
    
    
    
    
#english_dict = {
#    "apple" : "яблоко" ,
#    "milk" : "молоко"}
#word = input("Введите английское слово:")
#print(f"Перевод слова {word} на русский язык: {english_dict.get(word)}")


#english_dict = {
#    "apple" : "яблоко" ,
#    "milk" : "молоко"}
#english_dict.update({"cat" : "кошка" , "turtle" : "черепаха"})
#del english_dict[""]#

#print(english_dict)



#english_dict = {
#    "apple" : "яблоко" ,
#    "milk" : "молоко"}
#english_dict.popitem()
#english_dict["reraly"] = ["очень"] 
#english_dict["reraly"].append("да")
#print(english_dict)

#english_dict = {
#    "apple" : "яблоко" ,
#    "milk" : "молоко"}
#for i in english_dict.items():
#    print(i)
#print(len(english_dict))




catalog = {"Title1" : "Author1" , "Title2" : "Oleg"}
while True:
    print("Список возможных действий")
    print("1 - Добавить новую книгу")
    print("2 - Поиск книги по названию")
    print("3 - Удаление книги по названию")
    print("4 - Показать информацию обо всех книгах")
    print("0 - Закончить работу")
    user_choice = int(input("Выберете действие:"))
    if user_choice == 0:
        print("До свидания ")
        break
    elif user_choice == 1:
        title = input("Название книги:")
        while title in catalog:
            title = input("Название книги:")
        autor = input("Введите имя автора:")
        catalog[title] = autor
    elif user_choice == 2:
        title = input("Название книги:")
        if title in catalog:
            print("Информация о книге:")
            print(f"Название: {title}")
            print(f"Автор: {catalog[title]}")
        else:
            print("Книга не найдена")
    elif user_choice == 3:
        title = input("Название книги:")
        if title in catalog:
            del catalog[title]
            print("Книга удалена из каталога")
        else:
            print("Книга не найдена")
    elif user_choice == 4:
        print("Информация о книгах в каталоге:")
        for title in catalog:
            print(f"Название {title} , Автор: {catalog[title]}")
    else:
        print("Неверное действие. Попробуйте ещё раз")
    print("-------------------------")
        