class Animal(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s !"%(self.name,food))


class Dog(Animal):
    def fetch(self,thing):
        print("%s goes after the %s," % (self.name,thing))


class Cat(Animal):
    def swatstring(self):
        print("%s shreds the string!" % self.name)


d = Dog("Mike")
c = Cat("Mercy")

d.fetch("ball")
c.swatstring()
d.eat("dod food")
c.eat("cat food")


# ex3
