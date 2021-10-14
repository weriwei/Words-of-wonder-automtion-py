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
    pathWords = './final.txt'
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
        positionsList.append([196, 443, chars[0], False])
        positionsList.append([143, 610, chars[2], False])
        positionsList.append([243, 605, chars[3], False])

    elif(length == 4):
        positionsList.append([2290, 750, chars[0], False])
        positionsList.append([2185, 860, chars[1], False])
        positionsList.append([2290, 970, chars[2], False])
        positionsList.append([2400, 860, chars[3], False])

    elif(length == 5):
        positionsList.append([196, 443, chars[0], False])
        positionsList.append([115, 513, chars[1], False])
        positionsList.append([143, 610, chars[2], False])
        positionsList.append([243, 605, chars[3], False])
        positionsList.append([277, 511, chars[4], False])

    elif(length == 6):
        positionsList.append([188, 441, chars[0], False])
        positionsList.append([115, 488, chars[1], False])
        positionsList.append([114, 587, chars[2], False])
        positionsList.append([192, 623, chars[3], False])
        positionsList.append([265, 582, chars[4], False])
        positionsList.append([268, 493, chars[5], False])

    return positionsList

def getBlueStacksTopleft():
    bluestack = pyautogui.getWindowsWithTitle("BlueStacks")[0]
    bluestack.restore()

    return bluestack.topleft


def makeMoviment(word, positions):
    

    #primeira iteração precisa ir até o primeiro char e fazer o mouseDown
    for position in positions:
        if (position[2] == word[0]):
            topLeft = getBlueStacksTopleft()
            pyautogui.moveTo(position[0]+topLeft.x, position[1]+topLeft.y, 0.001)
            #time.sleep(0.1)
            pyautogui.mouseDown(button="left")
            position[3] = True
            break
    
    word = word[1:]        
    for char in word:
        for position in positions:
            if((position[2] == char) and (not(position[3]))):
                topLeft = getBlueStacksTopleft()
                pyautogui.moveTo(position[0]+topLeft.x, position[1]+topLeft.y, 0.001)
                #time.sleep(0.1)
                position[3] = True
                break
    
    pyautogui.mouseUp(button="left")
    
    for position in positions:
        position[3] = False
