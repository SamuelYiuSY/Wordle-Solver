
def getWordList():
    with open("list of Wordle words.txt") as wordsFile:
        wordList = []
        firstLine = wordsFile.readline()
        for each in firstLine.split(", "):
            wordList.append(each.replace('\n', ''))
        return wordList

def isResultValidate(result):
    if len(result) != 5:
        return False
    for each in result:
        if not (each in ["g", "y", "b"]):
            return False
    return True


if __name__ == "__main__":
    fullWordList = getWordList()    # used to check if the inputted word is valid
    newWordList = fullWordList.copy() # used to store the possible target words
    loopFlag = True
    while loopFlag:
        print("Please input your guess (e.g 'crane')")
        guess = input(">").lower()
        while not (guess in fullWordList):
            print("Your word is not in our word list, please input your guess (e.g 'crane') again")
            guess = input(">").lower()

        print("""Please input your result using the following rules (e.g. ggbyb)\n•g = green tile  (that means the letter is in the correct spot)\n•y = yellow tile (that means the letter is in the word but in the wrong spot)\n•b = black tile  (that means the letter is not in the word in any spot)""")
        result = input(">").lower()
        while not(isResultValidate(result)):
            print("""Invalid input, please input your result using the following rules (e.g. ggbyb) again\n•g = green tile  (that means the letter is in the correct spot)\n•y = yellow tile (that means the letter is in the word but in the wrong spot)\n•b = black tile  (that means the letter is not in the word in any spot)""")
            result = input(">").lower()

        for i1 in range(5):
            oldWordList = newWordList
            newWordList = []
            if result[i1] == "g":
                for each in oldWordList:
                    if each[i1] == guess[i1]:
                        newWordList.append(each)

            elif result[i1] == "y":
                for each in oldWordList:
                    # append case:
                    # 1, guess[i1] exist in each
                    # 2, guess[i1] != each[i1]
                    if guess[i1] in each and guess[i1] != each[i1]:
                        newWordList.append(each)

            # else:   # result[i1] == "b":
            elif result[i1] == "b":
                for each in oldWordList:
                    if not (guess[i1] in each):
                        newWordList.append(each)

            # print("old list: " + str(oldWordList))
            # print("new list: " + str(newWordList))

        print("The possible answer is 1 of the " + str(len(newWordList)) + " words: " + str(newWordList))




