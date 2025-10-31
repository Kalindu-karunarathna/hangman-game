import random
import hangmanWords
chooseWord = random.choice(hangmanWords.word_list)


hangmanPics = [
    """
    +----+
    |    |
         |
         |
         |
         |
     =========
    """,
    """
    +----+
    |    |
    O    |
         |
         |
         |
     =========
    """,
    """
    +----+
    |    |
    O    |
    |    |
         |
         |
     =========
    """,
    """
    +----+
    |    |
    O    |
   /|    |
         |
         |
     =========
    """,
    """
    +----+
    |    |
    O    |
   /|\\  |
         |
         |
     =========
    """,
    """
    +----+
    |    |
    O    |
   /|\\  |
   /     |
         |
     =========
    """,
    """
    +----+
    |    |
    O    |
   /|\\  |
   / \\  |
         |
     =========
    """
]



chooseWordLetters = list(chooseWord)
enteredLetters =[]

#tale length of chose word is used to have the number of spaces required and then assign those spaces to list
lengthOfChooseWord = len(chooseWord)
numberOfSpaces = ("_"*lengthOfChooseWord)
numberOfSpacesList = list(numberOfSpaces)
print("".join(numberOfSpacesList))

#instructions
print("*when game start, there is no hangman.")
print("*if enter wrong letter hangman start to appear step by step.")
print("if hangman fully appeared, you loss the game.")
print("if you find the word before hangman fully appeared, you won the game.")

allWrongChances = 6
wrongChances = 0


#while loop use to loop until the player finish the game
# if else statement use to define what happen based on letter is correct or not
# create indexes list which contain indexes of user entered letter  in the chose word
#replace the space list with entered letter if it corrects and then print

while chooseWordLetters!=numberOfSpacesList and wrongChances<allWrongChances :
    userEnteredLetter = input("enter a letter : ").lower()


    if userEnteredLetter in enteredLetters:
        print("you already enter  "+userEnteredLetter+"\n\n")
    else:

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
        print(hangmanPics[wrongChances])
    enteredLetters.append(userEnteredLetter)

if wrongChances<allWrongChances:
    print("hangman saved...you won the game\n\n\n")
else:
    print("word is...."+chooseWord)
    print("hangman died...you loss the game\n\n\n")




