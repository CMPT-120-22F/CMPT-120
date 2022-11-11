#first of all, breathe
#don't let this intimidate you. break it down a part at a time. You've done all of these separately and now we're just combining them.
'''
Instructions: Create a list with at least 8 numbers, and make sure you have a raandom dispersement between 0-50
Create a loop (which loop would be best given we know how long we're going [the length of the list]?) that runs through the entire list
Inside of your loop, have an if/elif/else that checks AT EACH INDEX OF THE LIST:
if the number is greater than 35: print ("greater than 35")
elif the number is between 20-35: print ("between 20-35")
elif the number is between 5-20: print ("between 5 and 20")
else (the number is less than 5)
'''

def main():
    list = [41, 23, 6, 14, 7, 46, 43, 15]
    
    for i in range(len(list)):
        if list[i] >= 35:
            print("greater than 35")
        elif 20 <= list[i] < 35:
            print("Between 20 and 35")
        elif 5 <= list[i] < 20:
            print("Between 5 and 20")
        else:
            print("Less than 5")
    
main()
