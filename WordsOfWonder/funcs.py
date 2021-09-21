from itertools import permutations
import cv2
import easyocr
import pyautogui
import time


def getAllPermutations(charList):
    possibleWords = []
    charsPermuted = []

    for length in range(len(charList)):
        charsPermuted += permutations(charList, length+3)

    for words in charsPermuted:
        possibleWords.append(''.join(words))

    return possibleWords


def getDictionary():
    pathWords = './palavrasFinal.txt'
    wordsList = []

    arquivo = open(pathWords, 'r')

    for words in arquivo.readlines():
        wordsList.append(words.replace('\n', ''))

    return wordsList


def getMatchedWords(dictionary, combionations):
    match = []

    for words in combionations:
        if words in dictionary:
            match.append(words)

    return match


def removeDuplicate(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def recognize():
    imagePath = 'imagens/wow/screenshot.png'
    img = cv2.imread(imagePath)
    charSet = 'ÇABCDEFGHIJKLMNOPQRSTUVWXYZ'

    reader = easyocr.Reader(['pt'])
    result = reader.readtext(img, detail=0, allowlist=charSet)

    return(list(''.join(result)))


def getScreenshot(x, y, width, heigth):
    pyautogui.screenshot('imagens/wow/screenshot.png',
                         region=(x, y, width, heigth))


def printMatches(match):
    for words in match:
        print(words)


def getListPositions(chars):
    length = len(chars)
    positionsList = []

    if(length == 3):
        positionsList.append([2290, 760, chars[0], False])
        positionsList.append([2200, 910, chars[1], False])
        positionsList.append([2380, 910, chars[2], False])

    elif(length == 4):
        positionsList.append([2290, 750, chars[0], False])
        positionsList.append([2185, 860, chars[1], False])
        positionsList.append([2290, 970, chars[2], False])
        positionsList.append([2400, 860, chars[3], False])

    elif(length == 5):
        positionsList.append([2312, 740, chars[0], False])
        positionsList.append([2222, 805, chars[1], False])
        positionsList.append([2255, 915, chars[2], False])
        positionsList.append([2365, 910, chars[3], False])
        positionsList.append([2400, 800, chars[4], False])

    elif(length == 6):
        positionsList.append([2323, 750, chars[0], False])
        positionsList.append([2240, 800, chars[1], False])
        positionsList.append([2252, 891, chars[2], False])
        positionsList.append([2326, 935, chars[3], False])
        positionsList.append([2405, 894, chars[4], False])
        positionsList.append([2400, 800, chars[5], False])

    return positionsList


def makeMoviment(word, positions):
    #primeira iteração precisa ir até o primeiro char e fazer o mouseDown
    for position in positions:
        if (position[2] == word[0]):
            pyautogui.moveTo(position[0], position[1])
            #time.sleep(0.1)
            pyautogui.mouseDown(button="left")
            position[3] = True
            break
    
    word = word[1:]        
    for char in word:
        for position in positions:
            if((position[2] == char) and (not(position[3]))):
                pyautogui.moveTo(position[0], position[1])
                #time.sleep(0.1)
                position[3] = True
                break
    
    pyautogui.mouseUp(button="left")
    
    for position in positions:
        position[3] = False
