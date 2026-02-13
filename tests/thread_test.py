import threading

def worker():
    a = 10
    b = a + 5
    print(b)

t = threading.Thread(target=worker)
t.start()
t.join()
