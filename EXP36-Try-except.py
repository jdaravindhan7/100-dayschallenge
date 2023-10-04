a=int(input("enter a number"))
b=int(input("enter a number"))
c=a+b
try:
    prin(c)
except NameError:
    print("something wrong")
except:
    print("therila")
finally:
    print("finally worked")
for i in range(10):
    if i>5:
        raise Exception("sorry bro")
    else:
        print(i)
