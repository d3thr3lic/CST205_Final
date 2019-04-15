#Ramon Lucindo
#Enhancements to Nick's original file
#Visual ascepts of our final project

#import os

#def setMediaPathToCurrentDir():
  #fullPathToFile = os.path.abspath(__file__)
  #if fullPathToFile.startswith('/'):
    #setMediaPath(os.path.dirname(fullPathToFile))
  #else:
    #setMediaPath(os.path.dirname(fullPathToFile) + '\\')


#Global Variables
#basementImage = getMediaPath() + "basement.jpg"
#bathroomImage = getMediaPath() + "bathroom.jpg"
#bedroomImage = getMediaPath() + "bedroom.jpg"
#billiardroomImage = getMediaPath() + "billiardroom.jpg"
#diningroomImage = getMediaPath() + "diningroom.jpg"
#kitchenImage = getMediaPath() + "kitchen.jpg"
#libraryImage = getMediaPath() + "library.jpg"
#livingroomImage = getMediaPath() + "livingroom.jpg"
#masterbedroomImage = getMediaPath() + "masterbedroom.jpg"

basementImage = pickAFile()
bathroomImage = pickAFile()
bedroomImage = pickAFile()
billiardroomImage = pickAFile()
diningroomImage = pickAFile()
kitchenImage = pickAFile()
libraryImage = pickAFile()
livingroomImage = pickAFile()
masterbedroomImage = pickAFile()

canvas = makeEmptyPicture(800,600)
basement = makePicture(basementImage)
bathroom = makePicture(bathroomImage)
bedroom = makePicture(bedroomImage)
billiardroom = makePicture(billiardroomImage)
diningroom = makePicture(diningroomImage)
kitchen = makePicture(kitchenImage)
library = makePicture(libraryImage)
livingroom = makePicture(livingroomImage)
masterbedroom = makePicture(masterbedroomImage)


roomIn = ""
GAMERUNNING = True

def startDemo(): #################Use this function here to start demo
  #setMediaPathToCurrentDir()
  showInformation("This is a demo of the visuals. This also shows off a text box function and text")
  showInformation("To end this game, type exit at anytime")
  whichRoom()
  ## starts off with a requestString prompting user for room.
  ## once selected, will repaint into room and prompt to go to the next room
  ## if asked to go into same room, will reject responce and ask again.

def whichRoom():
  global roomIn
  global GAMERUNNING

  userInput = requestString("Which room do you want to go into?\n -Basement\n -Bathroom\n -Bedroom\n -BilliardRoom\n -DiningRom\n -Kitchen\n -Library\n -LivingRoom\n -Master BedRoom\n")
  userInput = userInput.lower()
  usedInput = userInput.strip()

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
        #############3
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
      #showInformation("This input is not reconginzed, please try again.\nCheck out the textbox change after you press okay")
      textInBox("This is an invalid Input, please try again")
      whichRoom()

#######Room Related Functions
def toBasement():
  global roomIn
  roomIn = "basement"
  copyInto(basement,canvas,0,0)
  repaint(canvas)
  text = "This room is the Basement"
  textInBox(text)
  whichRoom()

def toBathroom():
  global roomIn
  roomIn = "bathroom"
  copyInto(bathroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the BathRoom"
  textInBox(text)
  whichRoom()

def toBedroom():
  global roomIn
  roomIn = "bedroom"
  copyInto(bedroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the BedRoom"
  textInBox(text)
  whichRoom()

def toBilliardroom():
  global roomIn
  roomIn = "billardroom"
  copyInto(billiardroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the BilliardRoom"
  textInBox(text)
  whichRoom()
  
def toDiningroom():
  global roomIn
  roomIn = "diningroom"
  copyInto(diningroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the DiningRoom"
  textInBox(text)
  whichRoom()
  
def toKitchen():
  global roomIn
  roomIn = "kitchen"
  copyInto(kitchen,canvas,0,0)
  repaint(canvas)
  text = "This room is the Kitchen"
  textInBox(text)
  whichRoom()
  
def toLibrary():
  global roomIn
  roomIn = "library"
  copyInto(library,canvas,0,0)
  repaint(canvas)
  text = "This room is the Library"
  textInBox(text)
  whichRoom()
  
def toLivingroom():
  global roomIn
  roomIn = "livingroom"
  copyInto(livingroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the LivingRoom"
  textInBox(text)
  whichRoom()
  
def toMasterBedroom():
  global roomIn
  roomIn = "masterbedroom"
  copyInto(masterbedroom,canvas,0,0)
  repaint(canvas)
  text = "This room is the Master BedRoom"
  textInBox(text)
  whichRoom()
    
######## Text related functions
def textBox():
#draws black box on bottom 100px of play window
  addRectFilled(canvas,50,500,700,80,black)
  repaint(canvas)

def textInBox(text):
  textBox()
  addText(canvas,100,520,text,white)
  repaint(canvas)
