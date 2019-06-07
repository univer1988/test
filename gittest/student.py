
class Student:
    def __init__(self,name,major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def education_level(self):
        if self.gpa >= 4:
            return 'Goood'
        else:
            return ('False')


class menu:
    def salat(self):
        print('salat')
    def chicken(self):
        print('chicken')
    def special(self):
        print('special')