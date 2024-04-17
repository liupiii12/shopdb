Login = "myCompany"
Password = "07120907777"
Login_input = input("Введите логин:")
Password_input = input("Введите пароль:")
if Login_input != Login or Password_input != Password:
    print("Неверный логин и пароль")
elif  Login_input == Login and Password_input != Password:
    print("Неверный пароль")
elif Password_input == Password and Login_input != Login:
    print("Неверный логин")
else:
    print("Доступ разрещён")
    print("Всем привет и если вы вошли сюда значит вы знакомы со мной лично иначе вы бы сюда не попали.Так вот это пока бета версия моего сайта и догин с паролем я вскоре изменю и исправлю недачёты")
