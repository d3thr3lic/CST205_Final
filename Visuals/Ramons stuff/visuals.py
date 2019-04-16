#Visual aspects of our final project
#this is a demo
#Ramon Lucindo
#Nick Saunders


import os

def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  if fullPathToFile.startswith('/'):
    setMediaPath(os.path.dirname(fullPathToFile))
  else:
    setMediaPath(os.path.dirname(fullPathToFile) + '\\')
    
setMediaPathToCurrentDir()

#Global Variables
welcomeImage = getMediaPath() + "welcome.jpg"
rulesImage = getMediaPath() + "rules.jpg"
noPlayImage = getMediaPath() + "noplay.jpg"
basementImage = getMediaPath() + "basement.jpg"
bathroomImage = getMediaPath() + "bathroom.jpg"
bedroomImage = getMediaPath() + "bedroom.jpg"
billiardroomImage = getMediaPath() + "billiardroom.jpg"
diningroomImage = getMediaPath() + "diningroom.jpg"
kitchenImage = getMediaPath() + "kitchen.jpg"
libraryImage = getMediaPath() + "library.jpg"
livingroomImage = getMediaPath() + "livingroom.jpg"
masterbedroomImage = getMediaPath() + "masterbedroom.jpg"
winnerImage = getMediaPath() + "winner.jpg"
loserImage = getMediaPath() + "loser.jpg"
group9Image = getMediaPath() + "group9.jpg"
#greenImage = getMediaPath() + "greenPic.jpg"

canvas = makeEmptyPicture(800,600)
welcome = makeEmptyPicture(welcomeImage)
rules = makeEmptyPicture(rulesImage)
noPlay = makePicture(noPlayImage)
basement = makePicture(basementImage)
bathroom = makePicture(bathroomImage)
bedroom = makePicture(bedroomImage)
billiardroom = makePicture(billiardroomImage)
diningroom = makePicture(diningroomImage)
kitchen = makePicture(kitchenImage)
library = makePicture(libraryImage)
livingroom = makePicture(livingroomImage)
masterbedroom = makePicture(masterbedroomImage)
winner = makePicture(winnerImage)
loser = makePicture(loserImage)
group9 = makePicture(group9Image)
#greenPic = makePicture(greenImage)


roomIn = ""
GAMERUNNING = True

def startDemo(): #################Use this function here to start demo
  if welcome():
    showInformation("This is a demo of the visuals. This also shows off a text box function and text")
    showInformation("To end this game, type exit at anytime")
    if instructions() == False:
      noPlay()
    else:
      whichRoom()
  else:
    noPlay()
        
  ## starts off with a requestString prompting user for room.
  ## once selected, will repaint into room and prompt to go to the next room
  ## if asked to go into same room, will reject responce and ask again.
  
def whichRoom():
  global roomIn
  global GAMERUNNING  
  userInput = requestString("Which room do you want to go into?\n      Basement\n      Bathroom\n      Bedroom\n      Billiard Room\n      Dining Room\n      Kitchen\n      Library\n      Living Room\n      Master Bedroom\n")
  userInput = userInput.lower()
  userInput = userInput.replace(" ", "")
  
  while GAMERUNNING:
    if userInput == "basement":
      if roomIn == "basement":
        #showInformation("You are already in the Basement")
        textInBox("You are already in the Basement")
        whichRoom()
      else:
        toBasement()
    elif userInput == "bathroom":
      if roomIn == "bathroom":
        #showInformation("You are already in BathRoom")
        textInBox("You are already in the BathRoom")
        whichRoom()
      else:
        toBathroom()
    elif userInput == "bedroom":
      if roomIn == "bedroom":
        #showInformation("You are already in the BedRoom")
        whichRoom()
      else:
        toBedroom()
    elif userInput == "billiardroom":
      if roomIn == "billiardroom":
        #showInformation("You are already in the BilliardRoom")
        whichRoom()
      else:
        toBilliardroom()
    elif userInput == "diningroom":
      if roomIn == "diningroom":
        #showInformation("You are already in the DiningRoom")
        whichRoom()
      else:
        toDiningroom()
    elif userInput == "kitchen":
      if roomIn == "kitchen":
        #showInformation("You are already in the Kitchen")
        whichRoom()
      else:
        toKitchen()
    elif userInput == "library":
      if roomIn == "library":
        #showInformation("You are already in the Library")
        whichRoom()
      else:
        toLibrary()
    elif userInput == "livingroom":
      if roomIn == "livingroom":
        #showInformation("You are already in the LivingRoom")
        whichRoom()
      else:
        toLivingroom()
    elif userInput == "masterbedroom":
      if roomIn == "masterbedroom":
        #showInformation("You are already in the Master BedRoom")
        whichRoom()
      else:
        toMasterBedroom()
    elif userInput == "exit":
      #showInformation("This demo is quitting... but won't yet close the main window, Sorry!")
      GAMERUNNING = False
    else:
      showInformation("This input is not reconginzed, please try again.")
      #textInBox("This is an invalid Input, please try again")
      whichRoom()
      
#######Beginning functions 
def welcome():
  copyInto(welcome,canvas,0,0)
  repaint(canvas)
  userInput = requestString("Would you like to play? Y or N?")
  userInput = userInput.lower()
  if userInput == "y":
    return True
  elif userInput == "n":
    return False
  else:
    showInformation("You made an invalid entry.")
    welcome()
    
def instructions():
  copyInto(rules,canvas,0,0)
  repaint(canvas)
  userInput = requestString("Would you like to continue? Y or N?")
  userInput = userInput.lower()
  if userInput == "y":
    return True
  elif userInput == "n":
    return False
  else:
    showInformation("You made an invalid entry.")
    instructions()
    
def noPlay():
  copyInto(noPlay,canvas,0,0)
  repaint(canvas)
  
#######Room Related Functions
def toBasement():
  global roomIn
  roomIn = "basement"
  copyInto(basement,canvas,0,0)
  repaint(canvas)
  text = "This room is the Basement"
  whiteText(text)
  whichRoom()

def toBathroom():
  global roomIn
  roomIn = "bathroom"
  copyInto(bathroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the BathRoom"
  whiteText(text)
  whichRoom()

def toBedroom():
  global roomIn
  roomIn = "bedroom"
  copyInto(bedroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the BedRoom"
  whiteText(text)
  whichRoom()

def toBilliardroom():
  global roomIn
  roomIn = "billardroom"
  copyInto(billiardroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the BilliardRoom"
  whiteText(text)
  whichRoom()
  
def toDiningroom():
  global roomIn
  roomIn = "diningroom"
  copyInto(diningroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the DiningRoom"
  whiteText(text)
  whichRoom()
  
def toKitchen():
  global roomIn
  roomIn = "kitchen"
  copyInto(kitchen,canvas,0,0)
  repaint(canvas)
  text = "This room is the Kitchen"
  whiteText(text)
  whichRoom()
  
def toLibrary():
  global roomIn
  roomIn = "library"
  copyInto(library,canvas,0,0)
  repaint(canvas)
  text = "This room is the Library"
  whiteText(text)
  whichRoom()
  
def toLivingroom():
  global roomIn
  roomIn = "livingroom"
  copyInto(livingroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the LivingRoom"
  whiteText(text)
  whichRoom()
  
def toMasterBedroom():
  global roomIn
  roomIn = "masterbedroom"
  copyInto(masterbedroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the Master BedRoom"
  whiteText(text)
  whichRoom()
    
######## Text related functions
def textBox():
  addRectFilled(canvas,50,480,700,100,black)

def whiteText(text):
  textBox()
  addText(canvas,75,500,text,white)
  repaint(canvas)

##for items?
def chromakey(greenPic, backgroundPic):
  pixelsFront = getPixels(greenPic)
  pixelsBack = getPixels(backgroundPic)
  for pixel in pixelsFront: 
    r = pixel.getRed()
    b = pixel.getBlue()
    g = pixel.getGreen()
    redBlueAvg = (r+b)/2.0
    if (g > (redBlueAvg)*2.0):
      pixelX = pixel.x
      pixelY = pixel.y
      backgroundPixel = getPixel(backgroundPic, pixelX, pixelY)
      setColor(pixel, getColor(backgroundPixel))
  repaint(greenPic)
