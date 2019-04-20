#CST 205 Final Project
## Team #9 S.C.E.S.
## Team Members:
## Austin Ah Loo
## Mikie Reed
## Mitchell Saunders
## Nicholas Saunders
## Ramon Lucindo

import os
# Global Variables
#global GAMERUNNING = True
#global CANVAS = makeEmptyPicture(800,600)

# driver
def main():#---------------------------------------------------------------------------------------------------
  setMediaPathToCurrentDir()
  # game settings
  # TODO: username
  startingRoom = "livingroom"
  global GAMERUNNING
  GAMERUNNING = true
  visual = visuals()
  inventory = []
  allItems = []
  if not visual.welcome():
    GAMERUNNING = false
  if GAMERUNNING and not visual.instructions():
    GAMERUNNING = false
  
  if GAMERUNNING:
    poorSoul = player("Sucks to be Me") # TODO: add userName
    room = houseRooms(startingRoom, getRooms())
    visual.paintRoom(room.houseRooms[startingRoom])
    
  while GAMERUNNING:
    userCmd = requestString("What would you like to do?\nEnter 'commands'\n'inventory'\nor 'exit'")
    if len(userCmd) > 0:
      userCmd = userCmd.lower()
    else:
      #user entered nothing, ask again
      continue
    if userCmd in movementCommands(): #check to make sure that the command given was valid for each control type
      room.changeRoom(userCmd, visual)
      
      
      
      
      
    elif userCmd in spMoveCommands():
      spMove(userCmd, roomIn, inventory)
    elif userCmd in controlCommands():
      otherCommand(userCmd, roomIn, inventory, allItems)
    elif userCmd == "exit":
      GAMERUNNING = False
      printNow("\nYou are a quitter.\n")
    else:
      printNow("I do not know that command.")

# specific moves within specified room with current inventory of items on player
def spMove(userCmd, roomIn, inventory):#-------------------------------------------------------------------------------------------------------
  if userCmd == "jump":
    jump(roomIn, inventory)
  if userCmd == "fall":
    fall(roomIn, inventory)
  if userCmd == "dance":
    dance(roomIn, inventory)
  if userCmd == "sleep":
    sleep(roomIn)
  if userCmd == "run":
    run()
  if userCmd == "cry":
    cry(roomIn)
  if userCmd == "scream":
    scream(roomIn)
  if userCmd == "laugh":
    laugh(roomIn)

# other commands within specified room with current inventory of items on player
def otherCommand(str, roomIn, inventory, allItems):#---------------------------------------------------------------------------------------------------
  #define and perform the other actions
  if str == "help":
    printNow(welcomeMsg(roomIn))
  elif str == "look":
    printNow(roomDescription(roomIn))
  elif str == "commands":
    listCommands()
  elif str == "inventory":
    listInventory(inventory)
  elif str == "examine":
    examineItem(inventory, allItems)

# valid moves: north, south, east, and west
def movementCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['n', 's', 'e', 'w', 'u', 'd']
  return validCommands

# specific valid moves
def spMoveCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['jump', 'dance', 'fall', 'sleep', 'run', 'cry', 'scream', 'laugh']
  return validCommands

# specific valid other commands
def controlCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['help', 'look', 'commands', 'examine', 'inventory']
  return validCommands

# lists inventory of items on player
def listInventory(inventory):#---------------------------------------------------------------------------------------------------
  if len(inventory) > 0:
    for i in inventory:
      printNow(i)
  else:
    printNow("You have nothing on you.")
    
# add an item to inventory of items on player
def addToInventory(item, inventory):#---------------------------------------------------------------------------------------------------
  inventory.append(item)

# check if an item is in the inventory of items
def examineItem(inventory, allItems):#---------------------------------------------------------------------------------------------------
  if len(inventory) > 0:
    userCmd = requestString("What item do you want to examine?")
    if userCmd in inventory:
      printNow(allItems[userCmd])
    else:
      printNow("You do not have that item in inventory.")
  else:
    printNow("You do not have any items in inventory.")


# lists different types of commands or movements 
def listCommands():
  print "Move: ", movementCommands()
  print "Special: ", spMoveCommands()
  print "Menu Commands: ", controlCommands()

# jump in specified room with items on player
# the user will need to exectue the jump action at some point in order to trigger the jump() function that
# advances the gameplay
def jump(roomIn, inventory):
  if roomIn == 4:
    printNow("You climb onto the bed and start jumping on it as you once did as a kid.\n" + \
              "While you where jumping, you hear a metallic sounding object hit the ground.\n" + \
              "After you had your fill of jumping, you climb down and stand next to the bed.\n" + \
              "You feel great, a little exausted, and a little embarrased that you did such a thing.\n" + \
              "You look around for that weird noise, and find a key.")
    addToInventory('key', inventory)
  else:
    printNow("You jumped. Are you happy?")

# fall in specified room with items on player
# the user will need to exectue the fall action at some point in order to trigger the fall() function that
# advances the gameplay
def fall(roomIn, inventory):
  if roomIn == 5:
    printNow("When you fall, you notice a weird object underneath the table.\n"+\
            "You grab the item, and it appears to be a medallion.")
    addToInventory('medallion', inventory)
  else:
    printNow("You should probably get up.")

# dance in specified room with items on player
# the dance() function includes the logic to determine whether the user wins or loses the game
def dance(roomIn, inventory):
  if (roomIn == 2):
    userCmd = ""
    printNow("You dance wildly, so much so that you move the couch.\n" +\
              "You notice a hatch where the couch was.")
    if('key' in inventory):
      printNow("The key that you have appears to be a perfect fit, and the hatch opens.")
      while True:
        userCmd = requestString("Would you like to enter the hatch? y/n")
        if(len(userCmd) > 0):
          userCmd = userCmd.lower()
          if(userCmd == 'y' or userCmd == 'n'):
            break
      if(userCmd == 'y'):
        printNow("You enter the hatch.\n" +\
                 "It is dark and damp, with a sense of dread as you step inside. Suddenly, the hatch closes and locks behind you.")
        if('medallion' in inventory):
          printNow("To your surprise, the medallion you found earlier starts to glow with a warm, golden aura, and your initial dread immediately dissolves.\n"+\
                   "You then see a distant light in the dark room.\n"+\
                   "You approach the light, and it leads you outside where it is safe.")
          win(True)
        else:
          printNow("There is a horrible stench and the sound of heavy breathing\n"+\
                   "A loud screech is made and you feel your body being ripped to pieces")
          win(False)
      elif(userCmd == 'n'):
        printNow("You do not enter the hatch.")
    else:
      printNow("This hatch appears to have a strange looking keyhole.\n" +\
               "Perhaps it is around here somewhere.")
  else:
    printNow("Keep going, like nobody's watching\n" + \
            "Except me...")

# determine if player won
def win(didWin):
  global GAMERUNNING

  if(didWin):
    printNow("Congratulations! You win the game!")
  else:
    printNow("You were killed by a monster, sorry, you lose the game, try again.")

  GAMERUNNING = False

# sleep in specified room
def sleep(roomIn):
  if roomIn == 4:
    printNow("Enjoy your rest, in some stranger's bed. You might regret this.")
  elif roomIn == 3:
    printNow("You're in the kitchen, at least go in the bedroom.")
  else:
    printNow("It's probably not a good time to sleep. You're in a creepy house\n" + \
              "and trying to get out!")

# run regardless of room
def run():
  printNow("What are you 6? Grow up!")

# cry in specified room
def cry(roomIn):
  if (roomIn % 2 == 0):
    printNow("I'm so sorry this happened to you!")
  else:
    printNow("Grow up Peter Pan!")

# scream in specified room
def scream(roomIn):
  if (roomIn % 2 == 1):
    printNow("I hear you, but I don't care...")
  else:
    printNow("I'd love to help you, but I'm just a wall.")

# laugh in specified room
def laugh(roomIn):
  if (roomIn % 2 == 1):
    printNow("You did it. Sort of. Good luck with the rest of this thing.")
  else:
    printNow("Kinda weird that you're laughing right now...")


  

# ====================================== general functions =================================================
def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  filePathForAssets = os.path.dirname(fullPathToFile) + '\Assets'
  # TODO: have Nick fix this logic (I added the \Assets)
  if fullPathToFile.startswith('/'):
    setMediaPath(filePathForAssets)
  else:
    setMediaPath(filePathForAssets + '\\')
    
def getRooms():
  #             Map of home
  #                  N
  #                W + E
  #                  S
  #  Basement
  #  |---------------|
  #  |   Basement    |
  #  |  up Library   |
  #  |---------------|
  #  1st Floor
  #  |--------------------------------|
  #  |               |                |
  #  |    Kitchen    _   Dining Room  |
  #  |               |                |
  #  |------- |------|-------- |------|
  #  |               |                | 
  #  |    Library    _   Living Room  |
  #  | down basement |up Billiard Room|
  #  |----------------------|  |------|
  #  2nd Floor
  #  |--------------------------------|
  #  |               |                |
  #  |   Bathroom    _     Bedroom    |
  #  |               |                |
  #  |------- |------|-------- |------|
  #  |               |                | 
  #  |Master Bedroom _ Billiard Room  |
  #  |               |down Living Room|
  #  |--------------------------------|
  rooms = dict()
  # addRoom(roomName, roomToNorth, roomToSouth, roomToWest, RoomToEast, stairsUp, stairsDown, roomsDictionary)
  addRoom("basement", "", "", "", "", "library", "", rooms)
  # 2nd floor rooms
  addRoom("bedroom", "", "billiardroom", "bathroom", "", "", "", rooms)
  addRoom("billiardroom", "bedroom", "", "masterbedroom", "", "", "livingroom", rooms)
  addRoom("masterbedroom", "bathroom", "", "", "billiardroom", "", "", rooms)
  addRoom("bathroom", "", "masterbedroom", "", "bedroom", "", "", rooms)
  # 1st floor rooms
  addRoom("kitchen", "", "library", "", "diningroom", "", "", rooms)
  addRoom("diningroom", "", "livingroom", "kitchen", "", "", "", rooms)
  addRoom("library", "kitchen", "", "", "livingroom", "", "basement", rooms)
  addRoom("livingroom", "diningroom", "", "library", "", "billiardroom", "", rooms)
  return rooms
  
def addRoom(roomName, roomToNorth, roomToSouth, roomToWest, RoomToEast, stairsUp, stairsDown, roomsDictionary):
  roomsDictionary[roomName] = singleRoom(getMediaPath() + roomName +".jpg", roomToNorth, roomToSouth, roomToWest, RoomToEast, stairsUp, stairsDown)


# ********************************************** visuals **************************************************
class visuals:
# Represents the current picture being displayed
# attributes: canvas 
  def __init__(self):
    self.canvas = makeEmptyPicture(800,600)
    
  def welcome(self):
    title = makePicture(getMediaPath() + "title.jpg")
    copyInto(title,self.canvas,0,0)
    repaint(self.canvas)
    userInput = requestString("Would you like to play? Y or N?")
    userInput = userInput.lower()
    if userInput != "y" and userInput != "n":
      showInformation("You made an invalid entry.")
      self.welcome()
    elif userInput == "y":
      return true
    else:
      return false

  def instructions(self):
    rules = makePicture(getMediaPath() + "rules.jpg")
    copyInto(rules, self.canvas, 0, 0)
    repaint(self.canvas)
    userInput = requestString("Would you like to continue? Y or N?")
    userInput = userInput.lower()
    if userInput == "y":
      return true
    elif userInput == "n":
      return false
    else:
      showInformation("You made an invalid entry.")
      self.instructions()
      
  def paintRoom(self, room):
    roomToPaint = makePicture(room.picture)
    copyInto(roomToPaint, self.canvas, 0, 0)
    repaint(self.canvas)
    text = "This room is the " + room.picture[len(getMediaPath()):-4] # 4 characters for .jpg
    # could have added room name to class, but thought this was a good use of substrings
    text += room.getDoors()
    self.whiteText(text)
    
  ######## Text related functions
  def textBox(self):
    addRectFilled(self.canvas, 50, 480, 700, 100, black)
  
  def whiteText(self, text):
    self.textBox()
    lines = text.split('\n')
    y = 500
    for line in lines:
      addText(self.canvas, 75, y, line, white)
      y += 12 # line spacing
      repaint(self.canvas)
    
  
# --------------------------------------------- sounds --------------------------------------------------

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Classes ++++++++++++++++++++++++++++++++++++++++++++++++++++
class player:
  # Represents the character in the game
  # attributes: 
  def __init__(self, name):
    self.name = name
    
  
  
class houseRooms:
  # Represents the rooms in the house
  # attributes: 
  def __init__(self, startingRoom, roomsDictionary):
    self.currentRoom = startingRoom
    self.houseRooms = roomsDictionary
    
  def changeRoom(self, direction, visual):
    newRoom = self.tryDirection(direction)
    if newRoom != self.currentRoom and newRoom != "":
      self.currentRoom = newRoom
      visual.paintRoom(self.houseRooms[newRoom])
  
  def tryDirection(self, direction):
    newRoom = ""
    currentRoom = self.houseRooms[self.currentRoom]
    if direction == 'n':
      newRoom = currentRoom.north
    elif direction == 's':
      newRoom = currentRoom.south
    elif direction == 'e':
      newRoom = currentRoom.east
    elif direction == 'w':
      newRoom = currentRoom.west
    elif direction == 'u':
      newRoom = currentRoom.stairsUp
    elif direction == 'd':
      newRoom = currentRoom.stairsDown
    return newRoom    

class singleRoom:
  # Represents a room
  # attribute: picture, north, south, west, east, upDown
  def __init__(self, picture, north, south, west, east, stairsUp, stairsDown):
    self.picture = picture
    self.north = north
    self.south = south
    self.west = west
    self.east = east
    self.stairsUp = stairsUp
    self.stairsDown = stairsDown
    
  def __str__(self):
    return self.picture
    
  def getDoors(self):
    doorLocations = ""
    if self.north != "":
      doorLocations += "\nn: " + self.north
    if self.south != "":
      doorLocations += "\ns: " + self.south
    if self.west != "":
      doorLocations += "\nw: " + self.west
    if self.east != "":
      doorLocations += "\ne: " + self.east
    if self.stairsUp != "":
      doorLocations += "\nu: " + self.stairsUp
    if self.stairsDown != "":
      doorLocations += "\nd: " + self.stairsDown
    return doorLocations
    
    
class items:
  # Represents character items
  # attributes:
  def __init__(self, item):
    self.addItem(item) 
  
#class actions:
  # Represents character actions