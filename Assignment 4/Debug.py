
def printHello():
    print("Hello")
    
def printName(x):
    print(x)
    
def addition(x, y):
    #add x and y together and return them
    z = x + y
    return z

def smaller(i, j):
    #if i is smaller than j, return i
    #if j is smaller than i, return j
    #if they're even, return 0
    if i < j:
        return i
    elif j < i:
        return j
    else:
        return 0

def main():
    
    #call the printHello function here
    printHello()
    #call printName and give it the parameter of your name

    printName("Slavitt")
    var1= 10
    var2= 20
    #What do we put in here to make it work?
    print(addition(var1, var2))
    
    num1 = int(input("Enter number 1"))
    num2 = int(input("Enter number 2"))
    #what go here?
    print(smaller(num1, num2))






main()
