numbers = [21, 25, -64, 16, -9, 14, 5, -144]
numbersPositive = []
numbersNegative = []
for x in numbers:
    if x >= 0:
        numbersPositive.append(x)
    else:
        numbersNegative.append(x**2)

even = []
odd = []
for x in numbers:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

intToChange = 12345
reverseNum = 0
while intToChange != 0:
    print(intToChange % 10)
    intToChange = (int)(intToChange / 10)
