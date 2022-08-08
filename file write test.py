a = open ('log.csv','a')
a.write("text to be written, add some extra text\n")
a.flush()
a.close()
print ("file written")

b = open('log.txt','r')
file_txt = b.read()
b.close
print("***************\n*******************\n")
print(file_txt)
