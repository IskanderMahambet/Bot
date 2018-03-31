#music_tools=['Скрипка','Барабан','Гитара','Пианино','Орган']
#music_tools.append('Домбыра')
#music_tools.remove('Орган')
#print(music_tools[:10])




#s = input()
#print(s[: :-1])



numbers= input('Введите числа через пробел:')
list_of_num = numbers.split(' ')
sum_num = 0
for num in list_of_num :
    sum_num+=int(num)

print(sum_num)
