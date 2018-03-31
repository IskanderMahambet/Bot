file = open('shop.txt','r',encoding='utf-8')
num=0
for line in file:
    list_values = line.split(',')
    num=num+1
    print('Номер: ',num)
    print('Штрих код: ',list_values[0])
    print('Название: ',list_values[1])
    print('Цена: ',list_values[2])
    print('Срок годности: ',list_values[3])
    print('Кол-во товара: ',list_values[4])


