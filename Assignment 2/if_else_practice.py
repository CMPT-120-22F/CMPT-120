#Instructions: Create a variable of any name and set it equal to 10.
#The first if statement should read: if 10 is greater than 12, print out "10 is greater than 12"
#The second if/else should read: Else if 10 is greater than 11, print out "10 is greater than 11"
#The third if/else should read: Else if 10 is equal to 10, print out "10 is equal to 10"
#The else should read: Else print out "10 is less than 10"

def main():
    ofAnyName = 10
    if ofAnyName > 12:
        print("10 is greater than 12")
    elif ofAnyName > 11:
        print("10 is greater than 11")
    elif ofAnyName == 10:
        print("10 is equal to 10")
    else:
        print("10 is less than 10")

main()