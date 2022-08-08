print ("Select your desired operation:")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
a = int (input ("Select a choice:"))
b = int(input("Enter first number:"))
c = int(input("Enter second number:"))
d = b + c
e = b - c
f = b * c
g = b / c
if a == 1:
    print ("You have chosen addition")
    print ("The sum of {0} + {1} = {2}".format(b,c,d))
elif a == 2:
    print ("You have chosen subtraction")
    print ("The difference of {0} - {1} = {2}".format(b,c,e))
elif a == 3:
    print ("You have chosen multiplication")
    print ("The product of {0} * {1} = {2}".format(b,c,f))
elif a == 4:
    print ("You have chosen division")
    print ("The quotient of {0} / {1} = {2}".format(b,c,g))
else:
    print ("You have chosen an invalid number")

print ("end of code")
