# class Dog:

#     #CLASS OBJECT ATTRIBUTE
#     species ='mammal'
    
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name= name


# mydog= Dog(breed = "lab", name="Lonkey")
# print(mydog.breed)
# print(mydog.name)
# print(mydog.species)

class Circle():
    pi =3.14
    def __init__(self, radius=1) :
        self.radius = radius

    def area(self):
        return self.radius * self.radius *Circle.pi

    def set_radius(self, new_r):
        self.radius= new_r

mycir =Circle(3)
mycir.set_radius(999)
print(mycir.area())