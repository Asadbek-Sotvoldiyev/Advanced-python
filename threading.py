import time
import threading
import concurrent.futures

start = time.perf_counter()

def index():
    print('Running a function')
    time.sleep(3)
    print('Complete a function')

finish = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    t = [executor.submit(index) for _ in range(10)]

    for f in concurrent.futures.as_completed(t):
        f.result()
# thread1 = threading.Thread(target=index)
# thread2 = threading.Thread(target=index)
#
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

print(f"Finished in {finish-start} seconds")
