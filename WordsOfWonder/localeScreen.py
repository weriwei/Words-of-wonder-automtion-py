import pyautogui 


def printScreenAndReturnBluestackWindowCoordinates(imageName):
    imagePath = 'imagens/wow/'+imageName+'.png'
    return pyautogui.locateOnScreen(imagePath, confidence = 0.4)
    
bluestack = printScreenAndReturnBluestackWindowCoordinates("bluestackApp")



position = getBluestackCoordinates(bluestackCoordinates, 395, 700)
pyautogui.screenshot('bluestackScreen.png', position)




    
