global temp
temp = 45

def print_temp():
    global temp
    temp = 50
    print (temp)

    
def inc_temp():
    global temp
    temp = temp + 5
    print (temp)

print("Original value of temp:",temp)

print_temp()
print("Original value of temp:",temp)

inc_temp()
inc_temp()
print("Original value of temp:",temp)

global result

def addition(a,b):
    global result
    result = a+b

def mul(a,b):
    global result
    result = a*b

addition(5,500)
print (result)

mul(3,4)
print (result)

#Next line are arguments

def trial(name, msg = "Hello,"):
    print (msg, name)
    
def keywordArg (name, role, msg1="My name is", msg2="I am a/an"):
    print(msg1, name, ",", msg2, role)

def printthem(*vars):
    print (vars)
    print (len(vars))
    for i in (vars):
        print (i)

trial("Rokki")

keywordArg(name = "Rokki",role = "Programmer")
keywordArg("Rokki","Programmer")

printthem (1,4,2,1,399)
