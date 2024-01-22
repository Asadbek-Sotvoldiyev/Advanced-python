import random
import time

names = ['Asadbek', 'Murodjon', 'Hasanboy', 'Ilyosbek', 'Asrorbek', 'Yahyobek', 'Abdulaziz', 'Farruxbek']
majors = ['IT', 'Filologiya', 'Tarix', 'Jismoniy Tarbiya', 'Iqtisod', 'Meditsina', "Boshlang'ich"]

def people_list(people_num):
    result = []
    
    for i in range(people_num):
        person = {
            "id":i,
            "name":random.choice(names),
            "majors":random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(people_num):
    for i in range(people_num):
        person = {
            "id":i,
            "name":random.choice(names),
            "majors":random.choice(majors)
        }
        yield person
    
    
time1 = time.time()
people_list(10000000)
time2 = time.time()

print("List tezligi: {} ga teng".format(time2-time1))

time3 = time.time()
people_generator(10000000)
time4 = time.time()

print("Generator tezligi: {} ga teng".format(time4-time3))

# result:
# List tezligi: 5.233255624771118 ga teng
# Generator tezligi: 0.0 ga teng