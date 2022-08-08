import datetime
now = datetime.datetime.now()

print (now)

mytime = now.strftime("%d-%m-%Y")

month_name = now.strftime("%B")
print (mytime)
print (month_name)
