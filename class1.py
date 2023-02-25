class Student:
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def set_age(self,age):
        self.age = age
    def get_age(self):
        print("Age is set to ",self.age)

    def display_student_details(self): 
        print("Name:", self.name) 
        print("Place:", self.place) 
        print("Age:", self.age)
    
