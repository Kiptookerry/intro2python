class Base:
    def __init__(self):
        self.a = "I have rights"
        self.b = "and priviledges"

class Derived(Base):
    def __init__(self):
        print(self.a)
        print(self.b)

#create an instance of the parent class
obj1 = Base()
print(obj1.a)
print(obj1.b)