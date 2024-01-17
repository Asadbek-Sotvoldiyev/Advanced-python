from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'group'])

new_tuple = Student('Asadbek', 20, 'FN7')
new_tuple = new_tuple._replace(age = 30)
print(new_tuple)

