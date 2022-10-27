def spyGame(y):
    for x in y:
        if x == 0 and x + 1 == 0 and x + 2 == 7:
            return True
    return False

def main():
    listOfInts = [4, 8, 3, 6, 3, 0, 0, 7]
    print(spyGame(listOfInts))

    #Input Sanitizing!
    #These methods will help deter errors and such
    num = input("Enter an int! ") #Error outputted if a string is inputted and cast to an int
    if num.isdigit():     #isDigit is exactly what it sounds like
        num = int(num)
        print(num)

    '''if num.isalnum():     #isAlNum checks if there's a number in a string
        print("extra letter >:(")

    if num.isalpha():     #isAlpha checks if it's a string
        print("string")'''

    #Pause and play!
    string = input("enter a string")
    while string.isalpha() == False:
        string = input("i said to enter a string")

    print(string)










main()