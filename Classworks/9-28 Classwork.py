'''
Make an infinite Loop!
funny = 24
while funny == 24:
    print("I've thought of something even funnier than 24")
'''

i = 0
while i < 10:
    print(i + 1)
    i = i + 1

backRange = int(input("PICK A NUMBER "))
sum = 0
for i in range(1, backRange + 1):
    sum = sum + i
print(sum)

list1 = [2, 3.456, "example", True]
list2 = []

for i in range(0, len(list1)):
    list2.append(type(list1[i]))

print(list2)