pi = 3.1415926

def thisIsAFunction(x):
    if x > 10:
        print("big number")
    elif x < 10:
        print("small number")
    elif x == 10:
        print("medium number")

def printNames(x, y):
    print("My name is " + x + " any my best friend's name is " + y)

def favFoodPrint():
    print("My favorite food is pizza")

def favDrinkPrint():
    print("My favorite drink is water")

def multiply(m, c):
    return (m * c)

def add(a, b):
    return (a + b)

def multFour():
    a = input("Pick a number to multiply")
    b = input("Pick a number to multiply")
    c = input("Pick a number to multiply")
    d = input("Pick a number to multiply")

    return (a * b * c * d)

momsName = "Michelle"
def myName():
    return "Samuel"

def main():
    thisIsAFunction(30)
    favFoodPrint()
    favDrinkPrint()
    print(multiply(2030, 1113))
    print(add(4, 9537))

    localVar = 3.41
    print(pi, localVar)

    print(momsName)
    print(myName)
main()