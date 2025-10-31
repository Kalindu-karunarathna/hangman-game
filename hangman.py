import random

word_ist = ["aardvark","camel","baboon"]

#choose random word and move its letters to a list
randNum = random.randint(0,2)
chooseWord = word_ist[randNum]
chooseWordLetters = list(chooseWord)

#tale length of chose word is used to have the number of spaces required and then assign those spaces to list
lengthOfChooseWord = len(chooseWord)
numberOfSpaces = ("_"*lengthOfChooseWord)
numberOfSpacesList = list(numberOfSpaces)
print("".join(numberOfSpacesList))

allWrongChances = 4
wrongChances = 0


#while loop use to loop until the player finish the game
# if else statement use to define what happen based on letter is correct or not
# create indexes list which contain indexes of user entered letter  in the chose word
#replace the space list with entered letter if it corrects and then print

while chooseWordLetters!=numberOfSpacesList and wrongChances<allWrongChances :
    userEnteredLetter = input("enter a letter : ").lower()

    if userEnteredLetter in chooseWordLetters:
        indexes = [i for i, ch in enumerate(chooseWord) if ch == userEnteredLetter]
        for i in indexes:
            numberOfSpacesList[i] = userEnteredLetter
        print("you guess well!!!")
        print("".join(numberOfSpacesList))
    else:
        print("your guess is wrong!!!")
        print("".join(numberOfSpacesList))
        wrongChances+=1



if wrongChances<allWrongChances:
    print("you won the game")
else:
    print("you loss the game")



