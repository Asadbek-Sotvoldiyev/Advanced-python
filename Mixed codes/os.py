import time
import os

def clock():
    start_time = round(time.time())
    
    while True:
        if(round(time.time())-start_time)%5==0:
            yield '5 second'
        else:
            yield 0
       
def query():
    for i in os.walk('C:\\'):
        yield i[0]

def main():
    data = query()
    alarm = clock()
    
    while True:
        d = next(data)
        a = next(alarm)
        print(d)
        if a:print(a)
        time.sleep(1)
        
main()