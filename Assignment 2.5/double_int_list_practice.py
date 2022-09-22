def main():
  
  #set this to any double
  doubleValue = 123.456789
  
  #set this to any int
  intValue = 44
  
  #print out addition, subtraction, multiplication, and division of these two values
  print (intValue + doubleValue)
  print(intValue - doubleValue)
  print(intValue * doubleValue)
  print(intValue / doubleValue)

  #populate this list
  myFriends = ["John", "Tyler", "Eoin", "Mat", "Neil", "Colin"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2] + " " + myFriends[3])
  
  #populate this list with five numbers
  fiveNumbers = [1, 2, 3, 4, 6]
  
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[0] + fiveNumbers[4])
  print(fiveNumbers[1] - fiveNumbers[0])
  print(fiveNumbers[2] * fiveNumbers[1])
  print(fiveNumbers[3] / fiveNumbers[2])

  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers.remove(2)
  fiveNumbers.insert(2, 7)

  #print out the list
  i = 0
  while i < 5:
    print(fiveNumbers[i])
    i = i + 1
  
main()
