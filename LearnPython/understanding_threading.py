import threading
import time

start = time.perf_counter()

def do_something():
    print("Start function")
    time.sleep(1)
    print("Done Sleeping!")

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

threads = []
for _ in range(1000):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'The time taken was {round((finish-start), 2)} second(s)')