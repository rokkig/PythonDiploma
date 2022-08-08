import time

a=0
try:
    myFile = open('excepttest2.txt','w')
    while a < 10:
        print (a)
        myFile.write(str(a))
        myFile.write("\n")
        time.sleep(1)
        a = a + 1

    print("trial ended")
    myFile.close()

# except: only will make an exception for any error
except KeyboardInterrupt:
    myFile.close()
    print("exiting...")
