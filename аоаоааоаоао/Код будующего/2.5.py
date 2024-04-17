#list1 = ["Четыре" , "Восемь" , "Двенадцать" , "Сорок"]
#max_list1 = max(list1,key=len)
#print(max_list1)

#a = int(input("Введите число:"))
#print(a*2)

def doble(num):
    return num*2
number = doble(8)
print(number)


doble = lambda num: num * 2
