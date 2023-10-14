class MyNumbers:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    x = self.a
    self.a += 2
    return x

myclass = MyNumbers()
#print("myclass",myclass)
myiter = iter(myclass)
n=int(input("enter n"))
for i in range(0,n,2):
    print(next(myiter))

class dell:
    def __iter__(self):
        self.a=a
        return self
    def __next__(self):
        if self.a < 10:
            x=self.a
            self.a+=1
            return x
        else:
            raise stopiteration
de=dell()
f=iter(de)
            
