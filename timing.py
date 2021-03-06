import time
#Calculates runtime of the program
def calculate_time(timer):
    def wrapper():
        time1 = time.time()
        timer()
        time2 = time.time()
        x = time2 - time1
        print('Total time ' + x)
    return wrapper
#function that sleeps for 2 seconds
def sleep_time():
    time.sleep(2)
    
