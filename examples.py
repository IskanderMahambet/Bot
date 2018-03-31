person_info={'ВИКТОР':'+77777777777',
             'НУРБОЛ':'+77072344565',
             'ИСКАНДЕР':'+77024162892'}
name=input()
name=name.upper()
if name in person_info:
    print(person_info[name])
else:
    print('Такого имени нет')


