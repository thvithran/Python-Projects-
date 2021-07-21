import threading
def mytimer():
     print("python.science")
my_timer = threading.Timer(3.0,mytimer)
my_timer.start()


