
num = int(input("please input a number"))
Found = False
count = 1
listHarshad = []
userHarshad = 0
while Found == False:
  countString = str(count)
  myList = []
  for i in countString:
    myList.append(i)
  if count % sum(myList) == 0:
    listHarshad.append(count)
  else:
    count = count +1
  if listHarshad[num] != []:
    print(listHarshad[num])
    Found = True
    break


"""
#June 2022 Section B - WORKING
userInput = input("enter a string: ")
print(userInput)
vowels = ["a", "e", "i", "o", "u"]
vowelCount = 0
userVowels = []
reverseVowels = []
listInput = []
for letter in userInput:
  listInput.append(letter)
for letter in listInput:
  if letter in vowels:
    userVowels.append(letter)
reverseVowels = userVowels[::-1]
for i in range(len(listInput)):
  if listInput[i] in vowels:
    listInput[i] = reverseVowels[vowelCount]
    vowelCount += 1
afterTransformation = "".join(listInput)
print(afterTransformation)
"""

"""
#June 2019 Section B - WORKING
userInput = input("enter a string")
userInput2 = input("enter another string")
userList1 = []
Valid = True
userList2 = []
sameLetters = []
for i in userInput:
  userList1.append(i)
for i in userInput2:
  userList2.append(i)
for i in range(len(userList1)):
  if userList1[i] in userList2:
    sameLetters.append(userList1[i])
for i in range(len(sameLetters)):
  if userList1[i] not in sameLetters:
    Valid = False
if Valid:
  print("The first word can be created using only letters from the second word")
else:
  print("The first word cannot be created using only letters from the second word")
"""
