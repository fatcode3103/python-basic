# class MyClass:
#   x = 5

# p1 = MyClass()
# print(p1.x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"
  
#   def helllFunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)

# p1.helllFunc()

# print(p1.name)
# print(p1.age)
# print(p1)


### Inheritance

# class Person:
#   def __init__(self, fname, lname):
#     self.firstName = fname
#     self.lastName = lname

#   def printname(self):
#     print(self.firstName, self.lastName)

# class Student(Person):
#   def __init__ (self, fname, lname, age): 
#     # Person.__init__(self, fname, lname)
#     super().__init__(fname, lname)
#     self.age = age

#   def welcome(self):
#     self.printname() 
#     print("Age:", self.age)

# x = Student("Mike", "Olsen", 20)
# x.welcome()


### iterator

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 6:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


### Polymorphism

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
