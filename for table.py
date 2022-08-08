print("This is code for finding out the table of a number using for loop")
num = int(input("enter a number: "))
print ("You have entered:",num)
for i in range (0,11):
    res = num * i
    print ("{0} x {1} = {2}".format(num,i,res))
    print ("Value of i = ",i)
