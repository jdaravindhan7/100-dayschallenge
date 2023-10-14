class bro:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def rand(self):
        print("name and age of the person is",self.name,"and his age is",self.age)
class bruh(bro):
    def __init__(self,name,age):
        super().__init__(name,age)
f=bruh("arav",19)
f.rand()
