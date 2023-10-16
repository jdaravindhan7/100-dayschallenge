age=35
se=23.5
v=29
name="my name is aravindhan and my age is {0} {2} and i am the HOTT{1}"
print(name.format(age,se,v))

def ds(n):
    return lambda a:a*n
mq=ds(3)
print(mq)
print(mq(1))
print(mq(10))
