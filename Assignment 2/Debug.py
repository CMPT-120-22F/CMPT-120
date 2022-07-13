#instructions: Something about these if statements aren't giving the desired effect. Look at them and see how to fix them. (Run them yourself and see what the output is!)


def main():
    
    #Start with this one! We have a compilation error :(
    #Side note: you can put these statements in parentheses or not. it's up to you.
    if (5 > 3)
        print("5 is greater than 3")
    
    #There are multiple correct answers and adjustments to this one 
    isFive = 5
    if isFive > 5:
        print("isFive is greater than 5")
    else:
        print("isFive is less than 5")

    #more multiple correct answers. Similar to the first. Adjust as perceived 
    toCheck = 4
    if toCheck > 5:
        print(toCheck, "is greater than 5.")
    elif toCheck < 3:
	    print(toCheck)
    else:
        print(toCheck, "is 3")

    #Is it really printing the BEST option though? Rearrange these as you see fit
    toCheck = 5
    if toCheck < 6:
        print("toCheck is less than 6")
    elif toCheck > 7:
        print("toCheck is greater than 7")
    elif toCheck == 5:
        print("toCheck is 5")
    else:
        print("toCheck is invalid")
    
    
    
    
main()
