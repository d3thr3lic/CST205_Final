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
TITLEIMAGE = getMediaPath() + "title.jpg"
RULESIMAGE = getMediaPath() + "rules.jpg"
NOPLAYIMAGE = getMediaPath() + "noPlay.jpg"
BASEMENTIMAGE = getMediaPath() + "basement.jpg"
BATHROOMIMAGE = getMediaPath() + "bathroom.jpg"
BEDROOMIMAGE = getMediaPath() + "bedroom.jpg"
BILLIARDROOMIMAGE = getMediaPath() + "billiardroom.jpg"
DININGROOMIMAGE = getMediaPath() + "diningroom.jpg"
KITCHENIMAGE = getMediaPath() + "kitchen.jpg"
LIBRARYIMAGE = getMediaPath() + "library.jpg"
LIVINGROOMIMAGE = getMediaPath() + "livingroom.jpg"
MASTERBEDROOMIMAGE = getMediaPath() + "masterbedroom.jpg"
WINNERIMAGE = getMediaPath() + "winner.jpg"
LOSERIMAGE = getMediaPath() + "loser.jpg"
GROUP9IMAGE = getMediaPath() + "group9.jpg"
#GREENIMAGE = getMediaPath() + "greenPic.jpg"

CANVAS = makeEmptyPicture(800,600)
TITLE = makePicture(TITLEIMAGE)
RULES = makePicture(RULESIMAGE)
NOPLAY = makePicture(NOPLAYIMAGE)
BASEMENT = makePicture(BASEMENTIMAGE)
BATHROOM = makePicture(BATHROOMIMAGE)
BEDROOM = makePicture(BEDROOMIMAGE)
BILLIARDROOM = makePicture(BILLIARDROOMIMAGE)
DININGROOM = makePicture(DININGROOMIMAGE)
KITCHEN = makePicture(KITCHENIMAGE)
LIBRARY = makePicture(LIBRARYIMAGE)
LIVINGROOM = makePicture(LIVINGROOMIMAGE)
MASTERBEDROOM = makePicture(MASTERBEDROOMIMAGE)
WINNER = makePicture(WINNERIMAGE)
LOSER = makePicture(LOSERIMAGE)
GROUP9 = makePicture(GROUP9IMAGE)
#GREENPIC = makePicture(GREENIMAGE)


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
  showInformation("If you won the game...")
  copyInto(WINNER,CANVAS,0,0)
  repaint(CANVAS)
  showInformation("if you lost the game...")
  copyInto(LOSER,CANVAS,0,0)
  repaint(CANVAS)
  showInformation("Roll the credits.")
  copyInto(GROUP9,CANVAS,0,0)
  repaint(CANVAS)

  ## starts off with a requestString prompting user for room.
  ## once selected, will repaint into room and prompt to go to the next room
  ## if asked to go into same room, will reject responce and ask again.

def whichRoom():
  global roomIn
  global GAMERUNNING
  userInput = requestString("Which room do you want to go into?\n      Basement\n      Bathroom\n      Bedroom\n      Billiard Room\n      Dining Room\n      Kitchen\n      Library\n      Living Room\n      Master Bedroom\n")
  userInput = userInput.upper()
  userInput = userInput.replace(" ", "")

  while GAMERUNNING:
    if userInput == "BASEMENT":
      if roomIn == "BASEMENT":
        #showInformation("You are already in the BASEMENT")
        textInBox("You are already in the BASEMENT")
        whichRoom()
      else:
        toBasement()
    elif userInput == "BATHROOM":
      if roomIn == "BATHROOM":
        #showInformation("You are already in BATHROOM")
        textInBox("You are already in the BATHROOM")
        whichRoom()
      else:
        toBathroom()
    elif userInput == "BEDROOM":
      if roomIn == "BEDROOM":
        #showInformation("You are already in the BEDROOM")
        whichRoom()
      else:
        toBedroom()
    elif userInput == "BILLIARDROOM":
      if roomIn == "BILLIARDROOM":
        #showInformation("You are already in the BILLIARDROOM")
        whichRoom()
      else:
        toBilliardRoom()
    elif userInput == "DININGROOM":
      if roomIn == "DININGROOM":
        #showInformation("You are already in the DININGROOM")
        whichRoom()
      else:
        toDiningRoom()
    elif userInput == "KITCHEN":
      if roomIn == "KITCHEN":
        #showInformation("You are already in the KITCHEN")
        whichRoom()
      else:
        toKitchen()
    elif userInput == "LIBRARY":
      if roomIn == "LIBRARY":
        #showInformation("You are already in the LIBRARY")
        whichRoom()
      else:
        toLibrary()
    elif userInput == "LIVINGROOM":
      if roomIn == "LIVINGROOM":
        #showInformation("You are already in the LIVINGROOM")
        whichRoom()
      else:
        toLivingRoom()
    elif userInput == "MASTERBEDROOM":
      if roomIn == "MASTERBEDROOM":
        #showInformation("You are already in the Master BEDROOM")
        whichRoom()
      else:
        toMasterBedroom()
    elif userInput == "EXIT":
      #showInformation("This demo is quitting... but won't yet close the main window, Sorry!")
      GAMERUNNING = False
    else:
      showInformation("This input is not reconginzed, please try again.")
      #textInBox("This is an invalid Input, please try again")
      whichRoom()

#######Beginning functions
def welcome():
  copyInto(TITLE,CANVAS,0,0)
  repaint(CANVAS)
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
  copyInto(RULES,CANVAS,0,0)
  repaint(CANVAS)
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
  copyInto(NOPLAY,CANVAS,0,0)
  repaint(CANVAS)

#######Room Related Functions
def toBasement():
  global roomIn
  roomIn = "BASEMENT"
  copyInto(BASEMENT,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the BASEMENT"
  whiteText(text)
  whichRoom()

def toBathroom():
  global roomIn
  roomIn = "BATHROOM"
  copyInto(BATHROOM,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the BATHROOM"
  whiteText(text)
  whichRoom()

def toBedroom():
  global roomIn
  roomIn = "BEDROOM"
  copyInto(BEDROOM,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the BEDROOM"
  whiteText(text)
  whichRoom()

def toBilliardRoom():
  global roomIn
  roomIn = "billardroom"
  copyInto(BILLIARDROOM,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the BILLIARDROOM"
  whiteText(text)
  whichRoom()

def toDiningRoom():
  global roomIn
  roomIn = "DININGROOM"
  copyInto(DININGROOM,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the DININGROOM"
  whiteText(text)
  whichRoom()

def toKitchen():
  global roomIn
  roomIn = "KITCHEN"
  copyInto(KITCHEN,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the KITCHEN"
  whiteText(text)
  whichRoom()

def toLibrary():
  global roomIn
  roomIn = "LIBRARY"
  copyInto(LIBRARY,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the LIBRARY"
  whiteText(text)
  whichRoom()

def toLivingRoom():
  global roomIn
  roomIn = "LIVINGROOM"
  copyInto(LIVINGROOM,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the LIVINGROOM"
  whiteText(text)
  whichRoom()

def toMasterBedroom():
  global roomIn
  roomIn = "MASTERBEDROOM"
  copyInto(MASTERBEDROOM,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the Master BEDROOM"
  whiteText(text)
  whichRoom()

######## Text related functions
def textBox():
  addRectFilled(CANVAS,50,480,700,100,black)

def whiteText(text):
  textBox()
  addText(CANVAS,75,500,text,white)
  repaint(CANVAS)

##for items?
def chromakey(GREENPIC, backgroundPic):
  pixelsFront = getPixels(GREENPIC)
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
  repaint(GREENPIC)
