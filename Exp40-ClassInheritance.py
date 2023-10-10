class bro:
    def __init__(self,name):
        self.name=name
class bruh(bro):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
class ge(bruh):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
    def deen(self):
        print("name:",self.name,"age:",self.age,"dept",self.dept)
p=ge("arav",19,"cse")
p.deen()
