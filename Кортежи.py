#a = (1,2,3,4,5)
#print(a)



#a = 1,2,3,4,5
#print(3 in a , 7 in a)


#a = 1,2,3,4,5
#print(len(a))


#a = 1,3,45,6
#b = 2,55,77
#print(a+b)


#a = 1,3,45,6
#b = 2,55,77
#c = (a+b)
#print(c*3)

#a = 1,3,45,6
#b = 2,55,77
#print(a[2])


#a = 1,3,45,6,[19,29]
#a[4].append(195)
#print(a)


#a = 1,3,45,6
#a = list(a)
##a.append(33)
#a.append(29)
#a.insert(0,22)
#a = tuple(a)
#print(a,type(a))
#for i in a:
 #   print(a)
    
    
#a = 10
#b = 22
#c = a + b
#for i in range(c):
#    print (f"сумма всех элементов в файле for")
#    print(len(c))


tupl = (1,2,3,4,5,6,7,8,9)
num = int(input("Введите число"))
if num in tupl:
    index = tupl.index(num)
    a = tupl[index]
    b = tupl[index +1]
    print(a + b)
else: print(tupl)






