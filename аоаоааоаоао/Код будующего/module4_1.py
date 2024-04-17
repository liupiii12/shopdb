import json
#Этап 1
#human = {
#    'name':'Дима',
#    'age':28,
#    'city':'Москва'
#}

#human_json = json.dumps(human, ensure_ascii=False)#Превращает объект питона в json
#print(human_json)

#Этап 2
#human = {
#    'name':'Дима',
#    'age':28,
#    'city':'Москва'
#}

#file = open('human.json' , 'w', encoding='utf-8')
#json.dump(human,file,ensure_ascii=False, indent=4)

#Этап 3
#
# human = {
#    'name':'Дима',
#    'age':28,
#    'city':'Москва'
#}

#human_json = json.dumps(human, ensure_ascii=False)#Превращает объект питона в json
#print(json.loads(human_json))

#Этап4
#file = open('human.json', encoding='utf-8')
#human_data = json.load(file)
#print(human_data)

#Задача

file = open('example.json', encoding='utf-8')
example_data = json.load(file)
if example_data['isFullTime'] == True and example_data['progLanguages'] >=2 and example_data['adress']['city'] == 'Санкт-Петербург':
    print('Проходит на 1 этап')
else:
    print('Не проходит на 1 этап')
