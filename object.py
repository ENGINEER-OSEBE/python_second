class Animal(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s eats %s!"%(self.name,food))

class Dog(Animal):
    def fetch(self,thing):
        print("%s is fetching me a %s"%(self.name,thing))

    def show_affection(self,):
        print("%s waggs his tail when i get home."%self.name)


class Cat(Animal):
    def scratch(self,place):
        print("%s likes scratching the %s" %(self.name,place))

    def show_affection(self,):
        print("%s purrs upon seeing me." %self.name)


d = Dog("Rex")
c = Cat("Tanny")

d.eat("steak")
c.eat("fish")
d.fetch("bone")
d.show_affection()
c.scratch("lawn")
c.show_affection()