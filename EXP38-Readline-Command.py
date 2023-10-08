a=open("iron.txt","r")
x=a.read()
#print(a.readline())
b=open("dome.txt","a")
print(b.write(x))
b.close()
a.close()

