
from PIL import Image, ImageEnhance
import time
import os

firstRun = True
tbOfAvailableFolders = ["Beside Python Executable"]
parentdir = os.getcwd()

def wait(f):
    time.sleep(f)
def gettInput():
    x = input(": ")
    return x
    
def d(s):
    print(s )
    
    wait(len(s)/15.0)
def PullFloat(x, min, max):
    if x < min:
        x = min
    elif x > max:
        x = max
    
    return x

def BuildFolder(dirName):
    dirName = dirName +" folder"
    returnThis = dirName
    global tbOfAvailableFolders
    
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    else:
        global firstRun
        returnThis = False
        firstRun = False
    
    tbOfAvailableFolders.append(dirName)
    
    return returnThis

def gettInputValidFolder():
    global tbOfAvailableFolders
    print("Please type a number from 0 to "+ str(len(tbOfAvailableFolders)-1) +", ")
    print("to select a valid folder to save into.")
    
    for i in range(len(tbOfAvailableFolders)):
        print(str(i) +" - "+ tbOfAvailableFolders[i])
    
    x = "heh"
    while True:
        x = MightInt(gettInput())
        if x == 0:
            break
        elif x != "F":
            x = PullFloat(x, 0, len(tbOfAvailableFolders)-1)
            break
    return x
def MightInt(n):
    if n == "0":
        return 0
    
    try:
        n = int(n)
    except:
        d("["+n+ "] not a valid input")
        print("Please enter an integer.")
        n = "F"
    # return can be int, False or "q"
    return n
def MightFloat(n):
    if n == "0":
        return 0.0
    
    try:
        n = float(n)
    except:
        d("["+n+ "] not a valid input")
        print("Please enter an float.")
        n = False
    # return can be int, False or "q"
    return n

def gettInputOptions(dirName):
    returnThis = False
    remoteBool = False
    print("0 - Turn "+ dirName+" into a png.")
    print("1 - Turn "+ dirName+" into a jpg.")
    print("2 - Resize "+ dirName +".")
    print("3 - Rotate "+ dirName+" image.")
    print("4 - Convert "+ dirName +" into black and white.")
    print("5 - Blur "+ dirName +" as an image.")
    
    while True:
        remoteVar = MightInt(gettInput())
        if remoteVar == 0:
            returnThis = remoteVar
            break
        elif remoteVar != "F":
            # okay, this is an int
            returnThis = remoteVar
            
            break
    return returnThis
def SaveTargetAs(i, nameOfLocation, fn, sourceName):
    # fext = sourceName = typeOFfILE
    # fn - fileName
    global tbOfAvailableFolders
    nameOfLocation = tbOfAvailableFolders[nameOfLocation]
    
    
    NewCommandLine()
    
    if sourceName == False:
        sourceName = ".jpg"
        print("Would you like to save "+fn+" as a [.png] or [.jpg]?")
        print("0 - .png")
        print("1 - .jpg")
        wait(.5)
        while True:
            n = MightInt(gettInput())
            if n == 0:
                sourceName = ".png"
            break
    
    print("["+sourceName+ "] selected.")
    if (nameOfLocation != "Beside Python Executable"):
        i.save(nameOfLocation+ "/"+ fn +sourceName)
    else:
        i.save(fn + sourceName)
    
    d("Success!")
    print(fn+ " has been successfully saved in ["+ nameOfLocation+"]!")
    wait(1)
    
def gettListOfStuff():
    print("-- Options --")
    for f in os.listdir("."):
        n = f.lower()
        if n.endswith(".jpg") or n.endswith(".png"):
            print(f)
def NewCommandLine():
    for _ in range(150):
        print(" ")
def moshiDenwa(x):
    remoteInt= 0
    for i in range(len(x)):
        remoteInt= remoteInt+ PullFloat(0, 0, len(x))
    return str(remoteInt)

def RailTarget(dirName):
    found = False
    remoteString = "minor change"
    for f in os.listdir("."):
        n = f.lower()
        if n.endswith(".jpg") or n.endswith(".png"):
            if f == dirName:
                found = True
                i = Image.open(f)
                fn, fext = os.path.splitext(f)
                print("["+dirName+ "] located.")
                wait(.3)
                print("Type: "+ fext)
                wait(.3)
                print("What would you like to do with ["+ dirName+ "]?")
                wait(.3)
                n = gettInputOptions(dirName)
                n = PullFloat(n, 0, 5)
                if n != False:
                    if n == 0:
                        NewCommandLine()
                        print("What folder would you like to save "+ fn + ".png to?")
                        n = gettInputValidFolder()
                        SaveTargetAs(i, n, fn, ".png")
                    elif n == 1:
                        NewCommandLine()
                        print("What folder would you like to save "+ fn +".jpg to?")
                        n = gettInputValidFolder()
                        SaveTargetAs(i, n, fn, ".jpg")
                    elif n == 2:
                        xx, yy = False, False
                        remoteString = "resize"
                        while True:
                            print("Enter the x dimension to save "+ dirName+" by.")
                            xx = MightInt(gettInput())
                            print("Enter the y dimension to save "+ dirName+" by.")
                            yy = MightInt(gettInput())
                            if yy == "F" or xx == "F":
                                wait(1)
                            else:
                                break
                        
                        i = i.resize((xx, yy))
                        NewCommandLine()
                        
                        n = gettInputValidFolder()
                        SaveTargetAs(i, n, fn, False)
                    elif n == 3:
                        NewCommandLine()
                        print("Enter an int from -360 to 360 degrees to rotate "+ dirName+" by.")
                        xx = "heh"
                        remoteString = "rotation change"
                        while True:
                            xx = MightInt(gettInput())
                            if xx == 0:
                                break
                            elif xx != "F":
                                break
                        
                        print("Rotating by "+ str(xx)+ " degrees.")
                        i = i.rotate(xx)
                        
                        n = gettInputValidFolder()
                        SaveTargetAs(i, n, fn, False)
                    elif n == 4:
                        i = ImageEnhance.Color(i)
                        remoteString = "[rgb.null]"
                        i = i.enhance(0.0)
                        
                        n = gettInputValidFolder()
                        SaveTargetAs(i, n, fn, False)
                    elif n == 5:
                        remoteString = "enhancment change"
                        i = ImageEnhance.Sharpness(i)
                        n = 0.0
                        print("Enter a float between -2.0 and 2.0")
                        print("["+dirName +"] blur level: "+ moshiDenwa(dirName))
                        d("The lower the number, the more blur")
                        while True:
                            n = MightFloat(gettInput())
                            if n == 0.0:
                                break
                            elif n != False:
                                n = PullFloat(n, -2.0, 2.0)
                                break
                            
                        d("Bluring image by "+ str(n)+" degrees")
                        
                        NewCommandLine()
                        i = i.enhance(n)
                        
                        n = gettInputValidFolder()
                        SaveTargetAs(i, n, fn, False)
                    
                break
    
    if found ==False:
        print("["+ dirName+ "] not found.")
        print("Please be specific with capital characters")
        wait(2)
    else:
        
        NewCommandLine()
        print("Would you like to look at how your "+ remoteString+" affected ["+ dirName+"]?")
        print("[ANY KEY] - Not right now.")
        print("1 - Yes, show it now please.")
        n = MightInt(gettInput())
        if n == 1:
            i.show()
            NewCommandLine()
        
        i.close()
    return found
linux = ["Black and White", "200x200", "400x400", "600x600", "Rotated"]
for i in range(len(linux)):
    BuildFolder(linux[i])

print("Here, I have the ability to make anything into anything")
print("Give it a try")
print("Enter a name of an image file.")
print("Must be a jpg or png.")
print("Capital letters count.")

while True:
    x = gettInput()
    if x.lower() == "q":
        break
    elif x.lower() == "/help":
        gettListOfStuff()
        print("Example0::  : River.jpg")
        print("Example1::  : dino1.JPG")
        
        continue
    elif x.lower() == "/show":
        d("One of these below")
        gettListOfStuff()
        n = gettInput()
        found = False
        for f in os.listdir("."):
            x = f.lower()
            if f == n:
                found = True
                i = Image.open(f)
                i.show()
                i.close()
                break
        if found == False:
            d("["+ n + "] not found")
    elif x.lower() == "/buildfolder":
        d("Enter a folder name: ")
        n = False
        
        n = gettInput()
        
        if n != False:
            x = BuildFolder(n)
            if x != False:
                d("[" + x +"] successfully made")
            else:
                d("["+ n + " folder] already exists.")
        continue
    
    n = RailTarget(x)
    if n == False:
        print("Try [/help] to see your options")
        print("Try [/buildfolder] to create a folder")
        print("Try [/show] to look at an image")
    else: # welcome back
        gettListOfStuff()
        
    
