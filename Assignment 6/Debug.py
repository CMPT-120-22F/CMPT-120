class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting
        
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("Fozzie" , 10)
    print("My dog", newDog.name, "is", newDog.age, "years old")
    
    #and what about a new employee
    newEmployee = Employee("Melissa Chodziutko", 42069, "Math + CS")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)
    
    #now create and print out a cake you make
    myCake = Cake("vanilla", "strawberry")
    print(myCake.flavor, "cake with", myCake.frosting, "frosting")
    
    #and now create another cake and print it out
    notMyCake = Cake("chocolate ice cream", "vanilla")
    print(notMyCake.flavor, "cake with", notMyCake.frosting, "frosting")
main()
