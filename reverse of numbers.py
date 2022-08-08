a = int(input("enter a number"))
print ("you have entered:",a)
rev = 0
while a > 0:
    rem = a % 10
    rev = (rev * 10) + rem
    a = a // 10
print ("Your reverse number is:",rev)

#still confusing for me, research on the while logic
