from datetime import date

class Person:
    def __init__(self,name,location,date_of_birth,gender):
        self.name = name
        self.location = location
        self.date_of_birth = date_of_birth
        self.gender = gender

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age-=1
        return age


asadbek = Person('Asadbek Sotvoldiyev','Fergana',date(2004,12,1),'Male')
print('Age: ',asadbek.calculate_age())
# Result: Age: 19
