import random

def generateOne(strlen, boolChecker, oldRes):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        if boolChecker[i] == True:
            res = res + oldRes[i]
        elif boolChecker[i] == False:
            res = res + alphabet[random.randrange(27)]
        else:
            print("What")

    return res

def score(generated, sentence, boolChecker):
    score = 0
    
    length = len(sentence)
    
    for i in range(length):
        if generated[i] == sentence[i]:
            score = score + 1
            boolChecker[i] = True

    return score

def generator(strlen):
    res = ""
    resScore = 0
    count = 0
    
    while resScore != strlen:
        res = generateOne(strlen, boolChecker, res)
        resScore = score(res, userSentence, boolChecker)
        count = count + 1

        if resScore == strlen:
            print("Generated a string that equals the user entered string")
            print(res)
            print(resScore)

        if count == 1:
            print("Current status")
            print(res)
            print(resScore)
            count = 0


userSentence = input("Enter a sentence: ")
userSentenceLength = len(userSentence)
boolChecker = [False] * userSentenceLength

generator(userSentenceLength)
