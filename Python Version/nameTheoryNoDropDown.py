#CHANGES TO MAKE: make it do newlines automatically wth are you doing

import json
import os
import tkinter as tk
from tkinter import ttk

#opening the json file containing names and advice for reference across all methods
with open(os.path.dirname(os.path.realpath(__file__)) + "\\names.json") as f:
    file = json.load(f)

#presents appropriate advice to the user-inputted name -----------------------#DOESNT RECOGNIZE Zoë
def enterButtonPressed():
    genAdviceLabel.config(text = "")

    #updates the 'name' tk label with the current name the program is holding
    nameStr = name.get().capitalize()
    nameLabel.config(text = "- " + nameStr + " -")

    #parsing through the json file to output the appropriate advice
    currentVal = ''
    for key, val in file[nameStr[0]].items():    
        #saving the current value in the event of an upcoming null. A key with a null value uses the most recent non-null advice as its value
        if currentVal == '' or val != None:
            currentVal = val

        #if you have reached the matching key:
        if key == nameStr:
            if currentVal == '' or val != None: #if the matching key is the first in the list or is a normal advice output case
                adviceLabel.config(text = nameSpellChecker(nameStr, val))
                resize(nameSpellChecker(nameStr, val))
            elif val == None: #if the matching key is null, pair it with the last saved non-null value in currentVal
                adviceLabel.config(text = nameSpellChecker(nameStr, currentVal))
                resize(nameSpellChecker(nameStr, currentVal))

            genAdviceLabel.config(text= "-----\nYou've recieved specific advice for " + nameStr + ", but there is still general advice about " + nameStr[0] + "s that you can see."
                                        "\nClick the 'General Advice' button if you want to see it, and if not, enter another name or quit.")

            genAdviceButton["state"] = "active"
            break  

        #general advice is always listed last in the json and is provided if this point is reached
        #If reached, the name has no specific advice or they inputted a single letter
        if "Advice" in key:
            adviceLabel.config(text = val)
            resize(nameSpellChecker(nameStr, val))

#make a letter list at the top where you can roll over a letter and a menu comes up that presents the names, kinda like dropdown() does

#provides the user with instructions
def instructionButtonPressed():
    instructionsWindow = tk.Tk()
    instructionsWindow.wm_title("Instructions")
    instructionsWindow.wm_minsize(1000,150)

    instructionLabel = tk.Label(instructionsWindow, text = "Hey, thanks for clicking on the instructions button. If you're new or need a refresher, this simple guide should explain it all."
        "\nEntering a name will give you an idea of what kind of personality that name will have, based on first letter and/or full name."
        "\nIf the name has a trend, you'll' get advice specific to it. If there is no specific advice, general rules of thumb for their letter will be presented to you."
        "\nPlease note that inputting your nickname may get you a different result than your full first name. Try them all!")
    instructionLabel.place(relx = 0.5, rely = 0.5, anchor = 'center')

#presents general advice to the user if they have already recieved specialized advice
def genAdviceButtonPressed():
    letter = name.get()[0].capitalize()

    generalAdvice = file[letter].get(letter + " Advice")
    genAdviceLabel.config(text = "-----\n" + generalAdvice)
    genAdviceButton["state"] = "disabled"

    resize(generalAdvice)
            
#gives the user an explanation as to how this is all literally for fun
def biasButtonPressed():
    biasWindow = tk.Tk()
    biasWindow.wm_title("Is this biased?")
    biasWindow.wm_minsize(1000,150)

    biasLabel = tk.Label(biasWindow, text = "Of course it is."
        "\n It was made exclusively by one person, and the advice is based on the similarities the creator found between people with those names."
        "\nIf it makes you feel any better, the creator only included a name if she'd met someone with that name at least twice."
        "\n\nAnother FAQ- is there any conflicting advice in here?"
        "\nYes, and you'll most likely find it between a specific name's advice and the advice for their general letter."
        "\nSome names break the trend of their overall letter. While the general advice is a good umbrella, there are always a few who want to walk in the rain."
        "\nIf you haven't come across any conflicting advice and want to see some, a mild example is Za(c/k/ch/ck). Try any of those names and then read over the Z general advice.")
    biasLabel.place(relx = 0.5, rely = 0.5, anchor = 'center')

#resizes the window if the general advice would run off the minimum borders
def resize(string):
    mainWindow.minsize(1100,500) if len(string) > 500 else mainWindow.minsize(900,500)

#allows the enter key to be bound to the tkinter enter button
def enterKeyPressed(x):
    enterButtonPressed()

#accounts for name-spelling differences in keys with null values
def nameSpellChecker(name, adviceString):
    updatedAdviceString = ''
    adviceList = adviceString.split("*")

    #replaces the *s in the json file with the name for output
    #first loop catches cases where a * is the first thing in the sentence
    #second ensures the name isn't appended to the end of the entire string
    for a in range(len(adviceList)):
        if (len(adviceList[a]) == 0) or (adviceList[a][len(adviceList[a])-1] not in {".", "?", "!"}):
            adviceList[a] += name
        
    for a in adviceList:
        updatedAdviceString += a

    return updatedAdviceString

#setting up mainWindow
mainWindow = tk.Tk()
mainWindow.wm_title("Allison's Name Theory, version 2.0.4")
mainWindow.wm_minsize(900,500)
#mainWindow.option_add('*Font', '2') -------------------------------------------FIGURE OUT THE FONT
mainWindow.bind('<Return>', enterKeyPressed)

#setting up mainWindow's user entry widgets
title = tk.Label(mainWindow, text = "- Welcome to Allison's Name Theory! -")
title.place(relx = 0.5, rely = 0.1, anchor = 'center')

name = tk.StringVar()
nameLabel = tk.Label(mainWindow, text = "Enter a name or letter below:")
nameLabel.place(relx = 0.5, rely = 0.2, anchor = 'center')

inputEntry = tk.Entry(textvariable = name)
inputEntry.place(relx = 0.5, rely = 0.3, anchor = 'center')

#setting up mainWindow's button alignments
enterButton = tk.Button(text = "Enter", fg = 'green', command = enterButtonPressed)
enterButton.place(relx = 0.3, rely = 0.4, anchor = 'center')

instructionButton = tk.Button(text = "Instructions", fg = 'orange', command = instructionButtonPressed)
instructionButton.place(relx = 0.4, rely = 0.4, anchor = 'center')

genAdviceButton = tk.Button(text = "General Advice", fg = 'blue', command = genAdviceButtonPressed)
genAdviceButton.place(relx = 0.5, rely = 0.4, anchor = 'center')
genAdviceButton["state"] = "disabled"

biasButton = tk.Button(text = "Is This Biased?", fg = 'black', command = biasButtonPressed)
biasButton.place(relx = 0.6, rely = 0.4, anchor = 'center')

#MAKE IT DESTROY THE BIAS/INSTRUCTINON WINDOWS TOO.IF YOU PUT THE INITIALIZERS ANYWHERE ELSE THEY SPAWN RIGHT AWAY--
quitButton = tk.Button(text = "Quit", fg = 'red', command = mainWindow.destroy)
quitButton.place(relx = 0.7, rely = 0.4, anchor = 'center')

#setting up mainWindow's output labels
adviceLabel = tk.Label(text = "")
adviceLabel.place(relx = 0.5, rely = 0.6, anchor = 'center')

genAdviceLabel = tk.Label(text = "")
genAdviceLabel.place(relx = 0.5, rely = 0.8, anchor = 'center')

mainWindow.mainloop()