f1 = open("this1.txt")
f2 = open("this2.txt","w")
for i in f1:
    f2.write(i)
f2.close()
f1.close()
