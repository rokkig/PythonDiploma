a = int (input ("Enter a number"))
b = int (input ("Enter another number"))
c = a + b
d = a * b
print ("Sum is:",c)
print ("The sum of {0} + {1} = {2}".format(a,b,c))
print ("The product of {0} x {1} = {2}".format(a,b,d))

# input 5 numbers from user and find out its average

a = int (input ("Enter a number:"))
b = int (input ("Enter another number:"))
c = int (input ("Enter a number:"))
d = int (input ("Enter another number:"))
e = int (input ("Enter a number:"))
f = (a + b + c + d + e)  / 5
print ("Average is:",f)
print ("The average of {0},{1},{2},{3},{4} is {5}".format(a,b,c,d,e,f))
