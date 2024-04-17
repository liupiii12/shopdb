#Задача 1
# num = int(input('Введите число:'))
#if num>0:
#    print('Данное число положительное')
#else:
#    print('Данное число отрицательное')

#Задача 2
#str = '1,2,3,4,5,6,767,8'
#print(f'Длинна данной строки {len(str)} посдедний элемент строки {str[8]}')


#Задача 3
#str1 = (input('Введите любое слово:'))
#str2 = (input('Введите любое слово:'))
#if str1[0] == str2[0]:
#    print(f'Ваши первые буквы слов совподают')
#else:
#    print(f'Ваше первые буквы слов не совподают')
    
#Задача 4
#str1 = (input('Введите любое слово:'))
#str2 = (input('Введите любое слово:'))
#str1 = tuple(str1)
#str2 = tuple(str2)
#print(f'Тип данной первой переменной {type(str1)}, тип данной второй переменной {type(str2)}')

#Задача 5
#slovo = input('Введите слово:')
#slovo = tuple(slovo)
#last_bukva = slovo[-1]
#if last_bukva == 'ь':
#    predposledn = slovo[-2]
#    print(f'Ваше слово заканчивается на мягкий знак, предпоследня буква {predposledn}')
#else:
#    print(f'Последния буква в вашем слове {last_bukva}')

#Задача 6
#hislo = input('Введите число:')
#hislo = list(hislo)
#perv = hislo[0]
#posl = hislo[-1]
#print(f'Первая цифра вашего числа - {perv} последняя - {posl}')#


#Задача 7
#hislo = input('Введите число:')
#hislo = (hislo)
#perv = int(hislo[0])
#posl = int(hislo[-1])
#summa = perv + posl
#print(f'Сумма первого и последего числа вашего слова = {summa}')


#num1 = input('Введите число')
#print(len(num1))



#num1 = input('Введите первое число:')
#num2 = input('Введите второе число:')
#perv1 = int(num1[0])
#perv2 = int(num2[0])
#if perv1 == perv2:
#    print(f'Первые числа ваших чисел совподают')
#else:
#    print(f'Первые числа ваших чисел не совподают')



#list1 = [1, 2, 3, 4, 5, 6]
#srez = list1[:3]
#print(srez)



#str1 = 'abcde'
#list1 = list(str1)
#print(list1)


#str1 = input('Введите символ:')
#predposl = str1[-2]
#str2 = 'a'
#if str1>str2:
#    print(f'Предпоследний символ {predposl}')



#num1 = int(input('Введите первое число:'))
#num2 = int(input('Введите второе число:'))
#if num1 % num2 == 0:
#    print(f'{num1} делится на {num2} без остатка!')
#else:
#    print(f'{num1} делится на {num2} с остатком!')


#sp1 = [1,2,3,4,5,6]
#srez = sp1[2:5]
#print(srez)

#dict1 = {
#    'year' : '2025',
#	'month': '12',
#	'day'  : '31',
#}
#for i in dict1.values():
   # print(i)



#for i in range(1,101):
#    print(i)


#for i in range(-100,1):
#    print(i)


#for i in range(100,1):
#   print(i)

#list1 = [1,2,3,4,5,6]
#list1.reverse()
#srez = list1[:2]
#srez.reverse()
#print(srez)


#str1 = 'abcdeabc'
#str1 = list(str1)
#srez = str1[:5]
#print(srez)


#summa = 0
#for i in range(1,101):
#    summa += i
#print(summa)

#num1 = int(input('Введите целое число:'))
#num2 = int(input('Введите второе целое число:'))
#ost = num1 % num2
#print(f'Остаток вашего деления {ost}')


#list1 = [1,2,3,4,5,6]
#srez = list1[::2]
#print(srez)


#list1 = [1,2,3,4,5]
#summa = sum(list1)
#print(summa)


#list1 = [1,2,3,4,5]
#summa = sum(num**2 for num in list1)
#print(summa)


#list1 = [1,2,-3,4,-5]
#summa = sum(num for num in list1 if num>0)
#print(summa)


#list1 = [-1, 2, -3, 4, 5, 11]
#summa = sum(num for num in list1 if 10>num>0)
#print(summa)


#str1 = 'abcde'
#for i in str1:
#    print(i)





#slv1 = {
#	'a': 1,
#	'b': 2,
#	'c': 3, 
#	'd': 4,
#}
#summa = sum(slv1.values())
#print(summa)   


#slv1 = {
	#'b': 2,
	#'c': 3, 
	#'d': 4,
#}
#summa = sum(num**2 for num in slv1.values())
#print(summa)	'a': 1,


#str1 = 'abcde'
#str1 = list(str1)
#print(str1)


#str1 = 'abcde'
#for i in str1:
#   print(i)
   
   
##str1 = 12345
#summa = sum(int(sum1) for sum1 in str(str1))
#print(summa)


#tuple1 = (1, 2, 3, 4, 5)
#summa = sum(tuple1)
#print(summa)


#numbers = [1, 2, 3, 4, 5, 6]
#sl = [num *1.1 for num in numbers]
#print(sl)


