def print_this():
    print ("Values you have entered are wrong. please re-enter")

def addition(p,q):
    r=p+q
    print("This is addition function. Sum of {0}+{1}={2}".format(p,q,r))
    print("***********************************")
    main()

def add(p,q):
    r=p+q
    return r

def addmul(p,q):
    add=p+q
    mul=p*q
    return add,mul

def main():
    a=int(input("enter a number:"))
    if a==0:
        print_this()
        main()
    else:
        print("You have entered",a)
    b=int(input("enter another number:"))
    if b==0:
        print_this()
        main()
    else:
        print("You have entered:",b)
    sums,product=addmul(a,b)
    print("sum = ",sums)
    print("product = ",product)
    c = add(a,b)
    print ("This is add function",c)
    addition(a,b)

main()
