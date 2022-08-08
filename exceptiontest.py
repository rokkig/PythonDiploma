import time
a = 0
try:
    while True:
        print("Value of a = ",a)
        a = a + 1
        time.sleep(2)
except KeyboardInterrupt:
    print("I am exiting...")
