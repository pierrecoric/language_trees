#some data structure to count for each collumn how many time a given letter is used
#another data structure to count for each gap how many connections they are

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listWords = []
longestWord = 0

#clean the text and turn it into a list
def prepareText():
    srcFile = open('raw_text.txt', 'r')
    rawText = srcFile.read()
    rawText = rawText.lower()
    alphaText = ''
    for c in rawText:
        if c.isalpha():
            alphaText += c
        elif c == '\'':
            alphaText += ' '
        elif c == '\n':
            alphaText += ' '
        elif c == ' ':
            alphaText += c
    listWords = alphaText.split(' ')
    return(listWords)

listWords = prepareText()
print(listWords)
#function to print the letter frequencies
def printFrequencies():
    for col in lettersFrequencies:
        print(col)

#compute the longest word
for word in listWords:
    if len(word) > longestWord:
        longestWord = len(word)


#create list of longestWord columns containing each a list of 26 letters
lettersFrequencies = []
for c in range(longestWord):
    column = []
    for i in range(len(alphabet)):
        column.append(0)
    lettersFrequencies.append(column)

#calculate the frequency of each letter for each column
for word in listWords:
    for c in range(len(word)):
        for i in range(len(alphabet)):
            if word[c] == alphabet[i]:
                lettersFrequencies[c][i] += 1



printFrequencies()
print(lettersFrequencies)