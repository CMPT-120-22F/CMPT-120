def main():
    #good working example!
    stringInput = input("enter a string")
    if stringInput.isalpha():
        print("string!")
    else:
        print("not string :(")
        
    #can you google and find what function you should use to check if it's numeric (an int?)?
    intInput = input("enter an int")
    if intInput.isdigit():
        print("int!")
    else:
        print("not int :(")
    
    #what about if it's both letters and numbers?
    alphIntInput = input("Enter letters and numbers")
    if alphIntInput.isalnum():
        print("Letters and numbers!")
    else:
        print("weird characters :(")
       
    #good working example
    asterisk = input("Enter an asterisk please")
    if asterisk == "*":
        print("good!")
    else:
        print("not asterisk :(")
        
    #now write code to check if the input was either an asterisk OR an ampersand (&)
    astOrAmp = input("Enter an asterisk or an ampersand! ")
    if astOrAmp == "*":
        print("Asterisk!")
    elif astOrAmp == "&":
        print("The thing that nobody uses anymore!")
    else:
        print("You had one job")

        
    #do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
    num = input("Enter an int! ")
    if num.isdigit():
        num = int(num)
        print(num)

    # last challenge: find out how to check if the string input has the substring "marist"
    #google this one ;) substring is the key google term
    maristStr = input("Put a random string in this variable")
    if maristStr.length() > 6:
        for x in range(0, (maristStr.length() - 6)):
            if maristStr[x, x+6: 1] == "Marist":
                print("The string has the phrase 'Marist' in it!")
            else:
                print("The string doesn't have the phrase 'Marist' in it.")
    else:
        print("The string doesn't have the phrase 'Marist' in it.")
main()
