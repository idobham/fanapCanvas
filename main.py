def reverseString(str):
    revStr = ""
    for i in range(len(str) - 1, -1, -1):
        revStr += str[i]
    return(revStr)

def mostRepeatedNum(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    mostRepeatedKey = -1
    mostRepeatedValue = None
    for key in counts:
        if counts[key] > mostRepeatedKey:
            mostRepeatedKey = key
            mostRepeatedValue = counts[key]
    return(mostRepeatedValue)

def primeChecker(num):
    if num <= 1: ## One itself is NOT a prime number
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def mainDiameterSumCalculator(matrix):
    matrixlength = len(matrix)
    mainDiameterSum = 0
    for i in range(matrixlength):
        mainDiameterSum += matrix[i][i]
    return mainDiameterSum


def wordsSorter(sentence):
    words = sentence.split()
    sortedWords = sorted(words)
    finalSentence = ' '.join(sortedWords)
    return finalSentence
