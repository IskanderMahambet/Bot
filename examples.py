file = open('shop.txt','r',encoding='utf-8')
least_product=99999
leat_line=[]
for line in file:
    list_values = line.split(',')
    if int(list_values[4]) < int(least_product):
        least_product = int(list_values[4])
        least_line = list_values
    
print('Название товара: ',least_line[1])
print('Кол-во товара: ',least_line[4])

