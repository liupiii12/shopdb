#skaf = [[{"book1":["abcd","efgh"], "book2":["ghgh" , "ssffg"]}]
#        [{"book3" :["wef"]} , "pen"],
#       [["shoes" , "bots"]]]
#print(skaf[0][0])


N = int(input())
data = []
for i in range(N):
    line = input('Введите имя , балл1  , балл2 ,балл3').split()
subj_1, subj_1, subj_3 = 0, 0, 0
for line in data:
    summa = int(line[1]) + int(line[2]) + int(line[3])
    print(f'Сумма балов ученика {line[0]}: {summa}')
    subj_1 += int(line[1])
    subj_2 += int(line[2])
    subj_3 += int(line[3])
print(f'Средний балл по первому предмету: {subj_1/N}')
print(f'Средний балл по второму предмету: {subj_2/N}')
print(f'Средний балл по третьему предмету: {subj_3/N}')
    
    