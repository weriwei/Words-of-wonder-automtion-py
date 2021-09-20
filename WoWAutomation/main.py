import funcs as f
import keyboard

dictionary = f.getDictionary()
listPositions = []


print("Pressione X para tirar um print da tela: ")

while(True):
    
    if keyboard.is_pressed('x'):
        
        f.getScreenshot(2240, 660, 150, 40)

        charsRecognized = f.recognize()
        
        listPositions = f.getListPositions(charsRecognized)

        possibleWords = f.getAllPermutations(charsRecognized)

        match = f.getMatchedWords(dictionary, possibleWords)

        match = f.removeDuplicate(match)

        f.printMatches(match)
        
        for word in match:
            f.makeMoviment(word, listPositions)
        




