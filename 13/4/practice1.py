class student:
    school='dabestan'
    def __init__(self,stId,name,family,grade):
        self.stId = stId
        self.name = name
        self.family = family
        self.grade = grade
    #instance method  showing name, family & grade
    def showname(self):
        return f'Name : {self.name} Family : {self.family} Grade : {self.grade}'

    def __str__(self):
        return f'STid is : {self.stId} Name is : {self.name} Family : {self.family} grade : {self.grade}'
    

    def __eq__(self,obj2):
        return self.stId == obj2.stId and self.name == obj2.name and self.family == obj2.family and self.grade == obj2.grade

    def __hash__(self):
        return hash(self.stId) + hash(self.name) + hash(self.family)+ hash(self.grade)
         


    @staticmethod
    def show_courses(grade):
        courses={
            1:['math', 'olom', 'zist'],
            2:['farsi', 'English', 'Arabi'],
            3:['farsi', 'English', 'Arabi','math', 'olom', 'zist'],
            4:['kargah','computer','programing'],
            5:['kargah','computer','programing','farsi', 'English', 'Arabi'],
            6:['honar','akasi','motaleat','tarikh']

        }

        #print dict
        if grade == 1:
            print(courses[1])
        elif grade ==2:
            print(courses[2])
        elif grade ==3:
            print(courses[3])
        elif grade ==4:
            print(courses[4])
        elif grade ==5:
            print(courses[5])
        elif grade ==6:
            print(courses[6])




    @classmethod
    def classmethod(cls,newschool):
        cls.school = newschool



#-------------------------------main program---------------------------------------------------------------


st1= student(1, 'Alireza', 'Hosseini', 3)
st2= student(2, 'Fateme', 'Kazemi', 4)
st3= student(3, 'Mohammad', 'Rezaei', 2)
st4= student(4, 'Zahra', 'Sadeghi', 6)
st5= student(5, 'Hossein', 'Karimi', 1)
st6= student(6, 'Alireza', 'Hosseini', 3)
st7= student(7, 'Fateme', 'Kazemi', 4)
st8= student(8, 'Mohammad', 'Rezaei', 2)
st9= student(9, 'Zahra', 'Sadeghi', 6)
st10= student(10, 'Hossein', 'Karimi', 1)


students={st1,st2,st3,st4,st5,st6,st7,st8,st9,st10}
print(100*'_')

for p in students:
    print(p)

print(100*'_')
#استفاده از تابع show_courses
student.show_courses(1)
student.show_courses(2)
student.show_courses(3)
student.show_courses(4)
student.show_courses(5)
student.show_courses(6)

print(100*'_')
#استفاده از تابع classmethod
st9.classmethod('Fersodi')
print(st9.school)

print(100*'_')