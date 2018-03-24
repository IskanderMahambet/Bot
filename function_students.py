
students = [['Арыстан',2],
            ['Искандер',5],
            ['Виктор ',4],
            ['Рахат',3],
            ['Владислав',4]]

def get_list_students():
    return students


def get_student_by_num(a):
    if a>len(students) or a<1:
        return'Студента с данным номерон не существует'
    else:
        return students[a-1]
    
def get_aver_students_mark():
    aver=0
    for student in students:
        aver+=student[1]
    return aver / len(students)

print(round(get_aver_students_mark())) #round-то код для округления
    
