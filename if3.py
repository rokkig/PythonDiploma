a = int(input("Enter first number"))
b = int(input("Enter second number"))
if a > b:
    print("First number is larger")
    print("am in print loop")
    print("i'll be printed because a > b")
    print("done with loop")
    if a > 100:
        print("A is also greater than 100")
        if a > 1000:
            print("A is also greater than 1000")
        else:
            print ("A is in between 100 and 1000")
if a > b and a > 100 and a > 1000:
    print("a is larger than b, and a is more than 100 and 1000")
if b > a or b > 100 or b > 50:
    print ("b is either bigger than a or larger than 100 or 1000")
else:
    print("Either b is larger or they the same bro")
print ("I am in the main code")
print("Code exiting")

#input 3 numbers from user and find the largest
#input 6 numbers from user and find the largest to smallest

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
if a > b and a > c:
    print ("a is the largest")
elif b > a and b > c:
    print ("b is the largest")
elif c > b and c > a:
    print ("c is the largest")
else:
    print ("some numbers are the same")
a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
d = int(input("Enter fourth number"))
e = int(input("Enter fifth number"))
f = int(input("Enter sixth number"))
if a > b and a > c and a > d and a > e and a > f:
    print ("a is the largest")
if a < b and a < c and a < d and a < e and a < f:
    print ("a is the smallest")
if b > a and b > c and b > d and b > e and b > f:
    print ("b is the largest")
if b < a and b < c and b < d and b < e and b < f:
    print ("b is the smallest")
if c > b and c > a and c > d and c > e and c > f:
    print ("c is the largest")
if c < b and c < a and c < d and c < e and c < f:
    print ("c is the smallest")
if d > a and d > b and d > c and d > e and d > f:
    print ("d is the largest")
if d < a and d < b and d < c and d < e and d < f:
    print ("d is the smallest")
if e > b and e > a and e > d and e > c and e > f:
    print ("e is the largest")
if e < b and e < a and e < d and e < c and e < f:
    print ("e is the smallest")
if f > b and f > a and f > d and f > e and f > c:
    print ("f is the largest")
if f < b and f < a and f < d and f < e and f < c:
    print ("f is the smallest")
