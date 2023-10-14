class v1:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def near(self):
        print("just for fun")
class v2(v1):
    def near(self):
        print("india")
class v3(v1):
    def __init(self,brand,model):
        super.__init_(self,brand,model)
    def near(self):
        print("america")
c1=v2("tata","nexon")
c2=v3("ford","sewe")
c3=v1("mahindra","scorpio")
for i in (c3,c1,c2):
    print(i.brand)
    print(i.model)
    i.near()

        
