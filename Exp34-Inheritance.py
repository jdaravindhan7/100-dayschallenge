class freed:
	def __init__(self,name,age):
		self.name=name;
		self.age=age;
	def greed(self):
		print("name of the student is",self.name)
class green(freed):
	pass
p=green("arun",24)
p.greed()
