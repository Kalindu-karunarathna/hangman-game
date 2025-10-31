import random

word_ist = ["aardvark","camel","baboon"]

randNum = random.randint(0,2)
chooseWord = word_ist[randNum]
chooseWordLetters = list(chooseWord)

lengthOfChooseWord = len(chooseWord)
numberOfSpaces = ("_"*lengthOfChooseWord)

numberOfSpacesList = list(numberOfSpaces)

print("".join(numberOfSpacesList))


while chooseWordLetters!=numberOfSpacesList:

    userEnteredLetter = input("enter a letter : ").lower()

    if userEnteredLetter in chooseWordLetters:
        indexes = [i for i, ch in enumerate(chooseWord) if ch == userEnteredLetter]
        for i in indexes:
            numberOfSpacesList[i] = userEnteredLetter
        print("".join(numberOfSpacesList))
    else:
        print("".join(numberOfSpacesList))




