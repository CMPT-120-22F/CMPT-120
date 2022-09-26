#Print your name 20 times!
name = "Samuel Louis Lavitt, First Of His Name"
for x in range(5):
    print(name)

for x in "Marist":
    print(x)
#This loop runs for the amount of characters in the list

for x in "Samuel Louis Lavitt, First Of His Name":
    print(x)

#Print your name in a loop!
print("Name is now in a list")
name2 = ["s", "a", "m", "u", "e", "l"]
for x in name2:
    print(x)

#While loops!
i = 0
while i < 4:
    print("Samuel Louis Lavitt, First Of His Name")
    i = i + 1

#Use loops to change numbers in lists!
loopList = [56, 93, 23, 106, 1]
for x in loopList:
    x = 69
print(loopList)

list = [59, 2, 3]
for x in list:
    print(x)
    list[x] = x + 1
