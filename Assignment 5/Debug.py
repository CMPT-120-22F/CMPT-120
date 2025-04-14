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
    typedThing = input("Enter an asterisk or amperstand please")
if typedThing == "*":
    print("asterick!")
elif typedThing == "&":
    print("amperstand!")
else:
    print("neither :(")
        
    #do the live example we did in class: ask user to input an integer, but before you cast it to an int, check that it's an integer before doing your variable = int(variable) command
    intInput = input("enter an int")
if intInput.isdigit():
    print("int!")
else:
    print("not int :(")
    # last challenge: find out how to check if the string input has the substring "marist"
    def isSubstring(s1, s2):
    if s1 in s2:
        return s2.index(s1)
    return -1

word = "marist"
# Driver Code
if word == "marist":
    s1 = "marist"
    s2 = "UPenn"
    res = isSubstring(s1, s2)
    if res == -1:
        print("Not present")
    else:
        print("Present at index " + str(res))
    #google this one ;) substring is the key google term
    
main()
