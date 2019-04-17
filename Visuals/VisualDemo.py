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
CANVAS = makeEmptyPicture(800,600)
GAMERUNNING = True

roomIn = ""


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
  endings()

  ## starts off with a requestString prompting user for room.
  ## once selected, will repaint into room and prompt to go to the next room
  ## if asked to go into same room, will reject responce and ask again.

def whichRoom(): ## when implemented in game, will take a parameter to switch rooms.
  #i.e. def whichRoom(userInput):
  #         if userInput == "basement":
  #           if roomIn == "basement":
  #             whiteText("You are already in the basement")
  #             #ask for action again
  #           else:
  #             toBasement()
  global roomIn
  global GAMERUNNING
  
  ############################################################## this section is for development purposes only, will be handled by base game.
  userInput = requestString("Which room do you want to go into?\n      Basement\n      Bathroom\n      Bedroom\n      Billiard Room\n      Dining Room\n      Kitchen\n      Library\n      Living Room\n      Master Bedroom\nFor items, see Inventory")
  userInput = userInput.lower()
  userInput = userInput.replace(" ", "")
  
  while GAMERUNNING:
  ###room inputs only  
    if userInput == "basement":
      if roomIn == "basement":
        whiteText("You are already in the basement")
        whichRoom()
      else:
        toBasement()
    elif userInput == "bathroom":
      if roomIn == "bathroom":
        whiteText("You are already in the bathroom")
        whichRoom()
      else:
        toBathroom()
    elif userInput == "bedroom":
      if roomIn == "bedroom":
        whiteText("You are already in the bedroom")
        whichRoom()
      else:
        toBedroom()
    elif userInput == "billiardroom":
      if roomIn == "billiardroom":
        whiteText("You are already in the billiardroom")
        whichRoom()
      else:
        toBilliardRoom()
    elif userInput == "diningroom":
      if roomIn == "diningroom":
        whiteText("You are already in the diningroom")
        whichRoom()
      else:
        toDiningRoom()
    elif userInput == "kitchen":
      if roomIn == "kitchen":
        whiteText("You are already in the kitchen")
        whichRoom()
      else:
        toKitchen()
    elif userInput == "library":
      if roomIn == "library":
        whiteText("You are already in the library")
        whichRoom()
      else:
        toLibrary()
    elif userInput == "livingroom":
      if roomIn == "livingroom":
        whiteText("You are already in the livingroom")
        whichRoom()
      else:
        toLivingRoom()
    elif userInput == "masterbedroom":
      if roomIn == "masterbedroom":
        whiteText("You are already in the Master bedroom")
        whichRoom()
      else:
        tomasterbedroom()
    ### end of rooms 
    ### start of misc items
    elif userInput == "inventory":
      displayInventory()
    elif userInput == "exit":
      GAMERUNNING = False ## closes request string, but does not close game window
    else:
      showInformation("This input is not reconginzed, please try again.")
      #whiteText("This is an invalid Input, please try again")
      whichRoom()
########################################################################################


#######Beginning and ending functions
def welcome():
### found bug, when you put in invalid entry at first question, then when it reprompts, and Y is selected, it rolls win/lose +credits
  title = makePicture(getMediaPath() + "title.jpg")
  copyInto(title,CANVAS,0,0)
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
  rules = makePicture(getMediaPath() + "rules.jpg")
  copyInto(rules,CANVAS,0,0)
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
  noPlay = makePicture(getMediaPath() + "noPlay.jpg")
  copyInto(noPlay,CANVAS,0,0)
  repaint(CANVAS)

def endings():
  winner = makePicture(getMediaPath() + "winner.jpg")
  loser = makePicture(getMediaPath() + "loser.jpg")
  group9 = makePicture(getMediaPath() + "group9.jpg")

  showInformation("If you won the game...")
  copyInto(winner,CANVAS,0,0)
  repaint(CANVAS)
  showInformation("if you lost the game...")
  copyInto(loser,CANVAS,0,0)
  repaint(CANVAS)
  showInformation("Roll the credits.")
  copyInto(group9,CANVAS,0,0)
  repaint(CANVAS)

#######Room Related Functions
def toBasement():
  global roomIn
  roomIn = "basement"
  basement = makePicture(getMediaPath() + "basement.jpg")
  copyInto(basement,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the BASEMENT"
  whiteText(text)
  whichRoom() ## will be changed to userInput commands, 
  #if they want to move around or switch rooms, they would have to go through the correct door using N,E,S,W rather that the ability to go to any room at will

def toBathroom():
  global roomIn
  roomIn = "bathroom"
  bathroom = makePicture(getMediaPath() + "bathroom.jpg")
  copyInto(bathroom,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the bathroom"
  whiteText(text)
  whichRoom()

def toBedroom():
  global roomIn
  roomIn = "bedroom"
  bedroom = makePicture(getMediaPath() + "bedroom.jpg")
  copyInto(bedroom,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the bedroom"
  whiteText(text)
  whichRoom()

def toBilliardRoom():
  global roomIn
  roomIn = "billardroom"
  billiardroom = makePicture(getMediaPath() + "billiardroom.jpg")
  copyInto(billiardroom,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the billiardroom"
  whiteText(text)
  whichRoom()

def toDiningRoom():
  global roomIn
  roomIn = "diningroom"
  diningroom = makePicture(getMediaPath() + "diningroom.jpg")
  copyInto(diningroom,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the diningroom"
  whiteText(text)
  whichRoom()

def toKitchen():
  global roomIn
  roomIn = "kitchen"
  kitchen = makePicture(getMediaPath() + "kitchen.jpg")
  copyInto(kitchen,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the kitchen"
  whiteText(text)
  whichRoom()

def toLibrary():
  global roomIn
  roomIn = "library"
  library = makePicture(getMediaPath() + "library.jpg")
  copyInto(library,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the library"
  whiteText(text)
  whichRoom()

def toLivingRoom():
  global roomIn
  roomIn = "livingroom"
  livingroom = makePicture(getMediaPath() + "livingroom.jpg")
  copyInto(livingroom,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the livingroom"
  whiteText(text)
  whichRoom()

def tomasterbedroom():
  global roomIn
  roomIn = "masterbedroom"
  masterbedroom = makePicture(getMediaPath() + "masterbedroom.jpg")
  copyInto(masterbedroom,CANVAS,0,0)
  repaint(CANVAS)
  text = "This room is the Master bedroom"
  whiteText(text)
  whichRoom()

######## Text related functions
def textBox():
  addRectFilled(CANVAS,50,480,700,100,black)

def whiteText(text):
  textBox()
  addText(CANVAS,75,500,text,white)
  repaint(CANVAS)


#######For inventory
def displayInventory():
###
### attempting to generalize for all items in a list. has issues, only takes in first element of list.
### can easily be hard coded in a list to draw on screen by calling drawInventory() with the item's picture
###
  inventory = ['one','two','three'] ## items in inventory for purposes of demo
  if len(inventory) == 0: ## if inventory is empty, will handle case
    showInformation("You do not have any items in your inventory")
    whichRoom()
  else:
    invInput = requestString("Which item do you want to see?\n" + str(inventory)+"\nType leave to leave menu")
    #repaint(CANVAS)#clears screen so if multiple items are looked at on screen, it will not overlap
    
    if invInput == 'leave':
       whichRoom()
        
    for item in inventory:
      if invInput != item:
        showInformation("You do not have that item.")
        break
      elif invInput == item:        
        itemPic = makePicture(getMediaPath() + item + ".png") #takes in item image
        posX = getWidth(CANVAS)/2-getWidth(itemPic)/2
        posY = getHeight(CANVAS)/2-getHeight(itemPic)/2
        drawInventory(itemPic,posX,posY)
        break    
 
    
def drawInventory(itemPic,width,height):
  inventory = pyCopyIgnoreColor(itemPic,CANVAS,width,height,white) #white was used for demo purposes
  repaint(CANVAS)


#copys images of items onto screen, ignores specfied color.
def pyCopyIgnoreColor(source, target,targetX,targetY,colorToIgnore):
  sWidth = getWidth(source)
  sHeight = getHeight(source)
  tWidth = getWidth(target)
  tHeight = getHeight(target)
  
  for x in range(0, sWidth):
    for y in range(0, sHeight):
      oldPix = getPixel(source, x, y)
      newX = x + targetX
      newY = y + targetY
      #this will allow me to have some of the photos leave the frame a little bit without crashing
      if (newX < tWidth) and (newX >= 0) and (newY < tHeight) and (newY >= 0):
        if getColor(oldPix) != colorToIgnore:
          newPix = getPixel(target, newX, newY)
          setColor(newPix, getColor(oldPix))
  return target    
