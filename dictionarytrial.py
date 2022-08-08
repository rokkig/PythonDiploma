dix = {"brand":"Toyota", "model":"Magnafanta","year":1991,"Country":"Camiendo", 1:2020}
print (dix)

newdix ={"price":123,"tax":45,"year":1995}

x=dix["model"]
print(x)

smalldix=dix.copy()
dix.update(newdix)
print (dix)

#dix.clear()
#print(dix)

bigdix = dix.copy()
print (bigdix)
print(dix.get("Country"))
print(dix.keys())

a = (dix.get("brand"))
print(a)

#b= (dix.pop("brand"))
'''
b=(dix.popitem())
print(b)
print(dix)

b=(dix.popitem())
print(b)
print(dix)
'''

print ("brand" in dix)
print ("name" in dix)

if "year" in dix:
    print ("year is present")
else:
    print ("year is absent")

if "1995" in dix:
    print ("1995 is present")
else:
    print ("1995 is absent, not a key")

print (len(dix))

dix["colour"]="burgundy"
print (dix)

dix["brand"]="Honda"
print (dix)
