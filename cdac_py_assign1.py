
# '''
# 1.Create a class 'Student' with rollno, studentName, course 
# ,dictionary of marks(subjectName -> marks [5]).
# Provide following functionalities
# A. initializer
# B. override __str__ method
# C. accept student data
# D. Print student data for given id.
# E. Print Student who has failed in any subject.
# Write menu driven program to test above functionalities.
# ( accept records of 5 students and store
# those in list )

# '''

import time

class Student:

    
    def __init__(self,rollno,name,course,marks):
        self.rollno = int(rollno)
        self.name = name
        self.course = course
        self.marks = marks
    

    def __str__(self):
        return f' Name of student : {self.name}\n rollno : {self.rollno}\
            \n course : {self.course}\nMarks of student are as follows\
            \n{info_marks(self.marks)}'


object_list =[]



def accept():
    roll = int(input('enter roll no: '))
    name = input('enter  name : ')
    course = input('enter course name: ')
    marks = {}
    marks['Data Structures'] = int(input('enter marks of Data Structures: '))
    marks['Operating Systems'] = int(input('enter marks of Operating Systems: '))
    marks['Comiler Design'] = int(input('enter marks of Comiler Design: '))
    marks['Computer Architecture'] = int(input('enter marks of Computer Architecture: '))
    object_list.append(Student(roll,name,course,marks))


def info_marks(values):
    return '\n'.join([f' {key} = {value}' for key, value in values.items()])

def search_by_roll():
    roll = int(input("Enter the roll no you want to look up : "))
    if len(object_list) == 0:
        return 'No such rollno'
    for i in range(len(object_list)):
        # print(object_list[i])
        if object_list[i].rollno == roll:
            return object_list[i]
    else:
        return 'No such roll no'


def failed():
    if len(object_list) == 0:
        print('no such roll no available')
    else:    
        for i in range(len(object_list)):
            for k,v in object_list[i].marks.items():
                if v < 36:
                    print(f'{object_list[i].name} failed in {k}')




def menu():
    print('-------A simple menu driven program--------')
    print('1: accept student data')
    print('2: print student data for a given roll no ')
    print('3: print students failed with respect to subject')
    print('0: Exit')
#tried dictionary for switch case

# def switch(i):
#     switcher = {
#         # 1:'als',
#         # 2:'sdw'
#         1:accept(),
#         2:search_by_roll(),
#         3:failed()
#     }
#     return switcher.get(i,'invalid entry')

ch=None
while ch !=0:
    time.sleep(1)
    menu()
    time.sleep(1)
    ch = int(input('enter your choice : '))
    if ch == 1:
        accept()
        time.sleep(1)
        print('----success----')
    elif ch == 2:
        print(search_by_roll())
        time.sleep(1)
    elif ch == 3:
        failed()
        time.sleep(1.5)
    else:
        break

print('program end')
    
                
# s1 = Student(25,'raj','cs',{'ds':56,'os':28,'algo':65})
# print(s1)
# def info_marks(value):
#     return '\n'.join([f'{key} = {value}' for key, value in marks.items()])
# marks = {'ds':56,'os':28,'algo':65}
# print(f"marks \n{info_marks(marks)}")
