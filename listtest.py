mylist = ["apple", "banana", "mango", "strawberry", 100, 500, 100, 100, 100]
print (mylist)
print (mylist[2])
mylist[3] = "blueberry"
mylist[5] = 750
print (mylist)

if 100 in mylist:
    print ("100 is present")

print (mylist[:3])
print (mylist[2:5])
print(len(mylist))
print(mylist*3)

mylist.append ("orange")
print(mylist)

#a = mylist
a = mylist.copy()


print (a)
print (mylist)
a[0] = "pineapple"

print (a)
print (mylist)
print(mylist.count(100))

mylist.extend(["asd","zxc","qwe"])
print(mylist)
print(mylist.index(100))

a = mylist.pop(0)
print (a)
print (mylist)

mylist.remove("mango")
print(mylist)

mylist.reverse()
print(mylist)

mylist2 = [2,3,4,5,145,657,750]
print (max(mylist2))

mylist2.append (23234)
print(mylist2)
#mylist2.clear()
print(mylist2)

mylist3 = mylist
print(mylist)
print(mylist3)
mylist[0] = "pineapple"
print(mylist)
print(mylist3)


mylist2.sort()
print (mylist2)
