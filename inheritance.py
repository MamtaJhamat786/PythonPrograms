class Animal:

    def __init__(self):
        print("Animal CReated")

    def who_am_i(self):
        print("animal")

    def eat(self):
        print("eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

    def bark(self):
        print("woof")

    def eat(self):
        print("dog eating")


mya=Animal()
mya.who_am_i();
mya.eat()

mya1=Dog()
mya1.who_am_i();
mya1.eat()


#special methods
class Book():
    def __init__(self, title, author, pages):
        self.titile = title
        self.author= author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author:{}, Pages: {}".format(self.titile,self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed")


b= Book("Python", "Jose", 29)

print(b)
print (len(b))
del(b)
