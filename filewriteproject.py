def removePunctuation(data: str):                       #list of sentences taken from the text file and broken up into words will be referred as clean list
    punc = '''!()-[]{};:'"\, <>./?@#$%^&amp;*_~'''      #takes in the clean list and removes punctuation marks and returns the list
    for i in punc:
        if i == data:
            data = data.replace(i, '')
        return data


def additionalSpaces(data: str):                        #takes in the clean list and removes spaces
    cleanBookList = []
    for i in data:
        x = i.strip()
        cleanBookList.append(x)
    return cleanBookList


def removeEmptyStrings(data: str):                     #takes in the clean list and removes empty strings ''
    elementNumber = 0
    for i in data:
        if i == "":
            data.pop(elementNumber)
        elif i == '':
            data.pop(elementNumber)
        elementNumber += 1
    return data


def checkRepeatedWords(data, variable, textFileList):     #takes in a list which contains used words i.e words which have already been compared to every other word in the
    for z in data:                                        #clean list
        if z == variable:                                 #second parameter is the string, which you want to check wether or not it has been compared already
            textFileList.remove(z)                        #if it has been compared already then it is removed from the clean list
                                                          #third parameter is the clean list itself
    return textFileList



def openFile():                                           #opens the file and stores the sentences in bookList and then it is broken up into words
    with open("blank", 'r+') as file:
        bookList = []                                     #after that all the punctuation, spaces and empty strings are removed and stored in cleanList
        for lines in file:
            for words in lines.split():
                bookList.append(words)
        cleanList = removeEmptyStrings(additionalSpaces(removePunctuation(bookList)))
    return cleanList


def main():
        cleanList = (openFile())
        lenCleanList = len(cleanList)
        listIndexNumber: int = 0                    #index number of the string which will be compared with every other string in the cleanList
        wordRepeatedTimes: int = 0                  #number of times the string is repeated
        countIndexNumber: int = 0
        frequencyDict = {}                          #stores the string and number of times which it has been repeated
        usedWords = []                              #stores the strings which have already been compared

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

#it is still very slow 

        print(frequencyDict)

main()

