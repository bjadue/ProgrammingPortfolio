# Brandon Jadue
# 10/23/23
# This program will determine whether a given word or phrase is a palindrome or not.
import time

def palenCheck(input):
    revStr = ''
    straList = []
    for i in range(int(len(input)), 0, -1):
        # print(input[i-1], end=" ")
        # print(i-1)
        straList.append(input[i-1])
    for char in straList:
        revStr += char
    return revStr

# all string conversions happen here, the user will see it.
userInput = input("Enter a word or phrase: ")
userInput = userInput.lower()
userInput = userInput.replace(" ", "")
reverseInput = palenCheck(userInput)

# meaningful messages to the user
print(f"{reverseInput} is {userInput} backwards!")
if reverseInput == userInput:
    print(f"{userInput} is a palindrome!")
else:
    print(f"{userInput} is not a palindrome.")

# Note to Prof K: This is because I like to run my programs on the
# command line, so I have this to keep it open for a bit longer.
time.sleep(3)
