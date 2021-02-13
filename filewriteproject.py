def removePunctuation(data: str):
     punc = '''!()-[]{};:'"\, <>./?@#$%^&amp;*_~'''
     for i in punc:
         if i == data:
             data = data.replace(i, '')
         return data


def additionalSpaces(data: str):
    cleanBookList = []
    for i in data:
        x = i.strip()
        cleanBookList.append(x)
    return cleanBookList


def removeEmptyStrings(data: str):
    elementNumber = 0
    for i in data:
        if i == "":
            data.pop(elementNumber)
        elif i == '':
            data.pop(elementNumber)
        elementNumber += 1
    return data


def checkRepeatedWords(data, variable):
    for z in range(len(data)):
        if variable == data[z]:
            return False
    return True


def openFile():
    with open("blank.txt", 'r+') as file:
        bookList = []
        for lines in file:
            for words in lines.split():
                bookList.append(words)
        cleanList = removeEmptyStrings(additionalSpaces(removePunctuation(bookList)))
        lenCleanList = len(cleanList)
        listIndexNumber: int = 0
        wordRepeatedTimes: int = 0
        countIndexNumber: int = 0
        deleteThis = 0
        deleteThis2 = 0
        usedWords = ["THIS"]
        frequencyDict = {}

        done: bool = False
        while not done:
            for word in cleanList:
                if cleanList[listIndexNumber] == word and checkRepeatedWords(usedWords, cleanList[listIndexNumber]):
                    wordRepeatedTimes += 1
                    deleteThis2 += 1
                elif not checkRepeatedWords(usedWords, cleanList[listIndexNumber]):
                    listIndexNumber += 1
                    deleteThis += 1
                    break
                elif countIndexNumber == lenCleanList - 1:
                    frequencyDict[cleanList[listIndexNumber]] = wordRepeatedTimes
                    usedWords.append(cleanList[listIndexNumber])
                    listIndexNumber += 1
                    print("3")
                elif cleanList[listIndexNumber] != word:
                    deleteThis2 += 1
                elif listIndexNumber == lenCleanList - 1:
                    done = True
                    break

            countIndexNumber += 1
        print(frequencyDict)
        print(deleteThis2)
        print(deleteThis)






#wordsUsed = ['what', '']
#cleanList = ['', 'what']
#print(checkRepeatedWords(wordsUsed, cleanList[0]))
openFile()

