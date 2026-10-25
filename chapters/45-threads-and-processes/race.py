import threading
import time

counter = 0
lock = threading.Lock()


def add_slowly():
    global counter
    for _ in range(50):
        with lock:
            current = counter
            time.sleep(0.0001)
            counter = current + 1


threads = [threading.Thread(target=add_slowly) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("expected 200, got", counter)
