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


def checkRepeatedWords(data, variable, what):
    for z in data:
        if z == variable:
            what.remove(z)

    return what



def openFile():
    with open("blank", 'r+') as file:
        bookList = []
        for lines in file:
            for words in lines.split():
                bookList.append(words)
        cleanList = removeEmptyStrings(additionalSpaces(removePunctuation(bookList)))
    return cleanList


def main():
        cleanList = (openFile())
        lenCleanList = len(cleanList)
        listIndexNumber: int = 0
        wordRepeatedTimes: int = 0
        countIndexNumber: int = 0
        frequencyDict = {}
        usedWords = []

        done: bool = False
        while not done:
             for word in cleanList:
                if cleanList[listIndexNumber] == word:
                    wordRepeatedTimes += 1

                elif countIndexNumber == lenCleanList - 1:
                    frequencyDict[cleanList[listIndexNumber]] = wordRepeatedTimes
                    usedWords.append(cleanList[listIndexNumber])

                    listIndexNumber += 1
                    cleanList = checkRepeatedWords(usedWords, cleanList[listIndexNumber], cleanList)
                    lenCleanList = len(cleanList)
                    break
                elif listIndexNumber == lenCleanList - 1:
                    done = True
                    break


                countIndexNumber += 1
             wordRepeatedTimes = 0



        print(frequencyDict)

main()

