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
        countVar: int = 0
        lenList: int = len(cleanList)
        done: bool = False
        elementNumber: int = 1
        repeatedVariable: int = 0
        repeatedDictionary = {}
        wordsUsed = []
        limit = 1
    file.close()

    while not done:
        repeatedVariable = 0
        for i in cleanList:
            if cleanList[countVar] == i and checkRepeatedWords(wordsUsed, cleanList[countVar]):
                repeatedVariable += 1
                elementNumber += 1


            elif not checkRepeatedWords(wordsUsed, cleanList[countVar]):
                countVar += 1
                limit += 1
                repeatedVariable = 0
                elementNumber = 0


            elif elementNumber == lenList - 1:
                wordsUsed.append(cleanList[countVar])
                repeatedDictionary[cleanList[countVar]] = repeatedVariable
                countVar += 1
                limit += 1
                repeatedVariable = 0
                elementNumber = 0


            elif countVar == lenList -1:
                done = True
                break

            else:
                pass

    print(repeatedDictionary)

#wordsUsed = ['what', '']
#cleanList = ['', 'what']
#print(checkRepeatedWords(wordsUsed, cleanList[0]))
openFile()
