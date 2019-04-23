#CST 205 Final Project
## Team #9 S.C.E.S.
## Team Members:
## Austin Ah Loo
## Mikie Reed
## Mitchell Saunders
## Nicholas Saunders
## Ramon Lucindo

import os
import time

def main():
  setMediaPathToCurrentDir()
  
  # game settings
  startingRoom = "living room"
  house = houseRooms(startingRoom)
  visual = visuals()
  sound = gameSounds()
  sound.startMusic()
  visual.welcome()
  visual.instructions()
  poorSoul = player()
    
  while poorSoul.gameRunning:
    visual.paintRoom(house.rooms[house.currentRoom])
    sound.continueMusic()
    userCmd = requestString("What would you like to do?\n'1' for commands.\n'2' to view Inventory.\n'quit' if you're scared.")
    sound.continueMusic() #the user may take a long time to choose what to do, so when they press okay it will resume music
    if len(userCmd) > 0:
      userCmd = userCmd.lower()
    else:
      #user entered nothing, ask again
      continue
    if userCmd in movementCommands(): #check to make sure that the command given was valid for each control type
      changedRoom = house.changeRoom(userCmd, sound)
      if not changedRoom: # user input was not allowed
        showInformation("There is no where to go in the direction")
        continue
      visual.paintRoom(house.rooms[house.currentRoom])
      house.getRoomItem(poorSoul, visual)
    elif userCmd == "1":
      displayCommands()
    elif userCmd == "2":
      visual.displayInventory(poorSoul)  
    elif userCmd == "quit":
      poorSoul.gameRunning = False    
    else:
      showInformation("That is not a valid command.")
  # end main() while loop ---------------------------------------
  visual.paintTile("group9")
  sound.soundEffect("main fade")
  sound.stopMusic()
  time.sleep(3)
# end main() -----------------------------------------------------------------------------------------------------------------------  
  
# valid moves: north, south, east, and west
def movementCommands():#---------------------------------------------------------------------------------------------------
  validCommands = ['n', 's', 'e', 'w', 'u', 'd']
  return validCommands
  
def displayCommands():
  showInformation("n = north\ns = south\ne = east\nw = west\nu = upstairs (if stairs are present)\nd = downstairs (if stairs are present)")

# ====================================== general functions =================================================
def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  filePath = os.path.dirname(fullPathToFile)
  if fullPathToFile.startswith('/'):
    setMediaPath(filePath + "/Assets/")
  else:
    setMediaPath(filePath + '\\Assets\\')
    
def getTextFile(fileName):
  return open(getMediaPath() + fileName + ".txt", 'r')

# ********************************************** visuals **************************************************
class visuals:
# Represents the current picture being displayed
# attributes: canvas 
  def __init__(self):
    self.canvas = makeEmptyPicture(800,600)
    
  def welcome(self):
    self.paintTile("title")
    showInformation("Let's get weird!")  

  def instructions(self):
    self.paintTile("rules")
    time.sleep(3)
    self.paintLongText("starting information")
     
  def paintTile(self, tile):
    newCanvas = makePicture(getMediaPath() + tile + ".jpg")
    self.paintCanvas(newCanvas)
  
  def paintCanvas(self, picture):
    copyInto(picture, self.canvas, 0, 0)
    repaint(self.canvas)
                          
  def paintRoom(self, room):
    roomToPaint = makePicture(room.picture)
    self.paintCanvas(roomToPaint)
    text = "This room is the " + room.picture[len(getMediaPath()):-4] # 4 characters for .jpg
    # could have added room name to class, but thought this was a good use of substrings
    text += room.getDoors()
    self.whiteText(text)
  
  #######For inventory
  def displayInventory(self,player):
    #inventory = ["king", "queen", "ace","paper","book","joker"] ## for testing purposes
    inventoryList = []
    
    for item in player.inventory.currentItems:
       inventoryList.append(item)
       
    if len(inventoryList) == 0: ## if inventory is empty, will handle case
      showInformation("You do not have any items in your inventory")
      invInput = 'leave'
    else:
      invInput = requestString("Which item do you want to see?\n" + str(inventoryList)+"\nType 'leave' to leave menu")
      #TODO:(maybe) account for Caps and spaces
    if invInput == 'leave':
       return True ##should return user back to general action prompt
  
    #for item in inventory: 
    if invInput in inventoryList:
      itemPic = makePicture(getMediaPath() + invInput + ".jpg") #takes in item image
      posX = getWidth(self.canvas)/2-getWidth(itemPic)/2
      posY = getHeight(self.canvas)/2-getHeight(itemPic)/2
      self.whiteText(player.inventory.currentItems[invInput])
      self.drawInventory(itemPic,posX,posY)
      showInformation("Continue?")
    else:      
      showInformation("You do not have that item.")    
   
  def showInventory(self, itemPic, definition):
    posX = getWidth(self.canvas)/2-getWidth(itemPic)/2
    posY = getHeight(self.canvas)/2-getHeight(itemPic)/2
    self.whiteText(definition)
    self.drawInventory(itemPic,posX,posY)   
         
  def drawInventory(self,itemPic,width,height):
    inventory = self.pyCopyIgnoreColor(itemPic,self.canvas,width,height,green) 
    #green was used items that need to not be square
    repaint(self.canvas)
    time.sleep(1)  

  #copys images of items onto screen, ignores specfied color.
  def pyCopyIgnoreColor(self,source, target,targetX,targetY,colorToIgnore):
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
        
  ######## Text related functions
  def paintLongText(self, fileName):
    lines = getTextFile(fileName)
    linesList = []
    for line in lines:
      linesList.append(line)
    self.whiteText(linesList)
    time.sleep(3)
    showInformation("Good luck!")
  
  def textBox(self, x, y, xLen, yLen):
    addRectFilled(self.canvas, x, y, xLen, yLen, black)
  
  def whiteText(self, text):
    x = 50
    xLen = 700
    if isinstance(text, str):
      y = 480
      self.textBox(x, y, xLen, 100)  
    else:
      y = 50
      self.textBox(x, y, xLen, 500)
    typeIndent = 25
    x += typeIndent
    y += typeIndent
    if not isinstance(text, list): # files already come in as lists
      lines = text.split('\n')
    else:
      lines = self.fitTextBox(text, (xLen - (typeIndent * 5))) #indent on both sides
    for line in lines:
      addText(self.canvas, x, y, line, white)
      y += 12 # line spacing
      repaint(self.canvas)
  
  def fitTextBox(self, text, boxLength):
    charPerLine = int(boxLength / 5.9)
    smallLines = []
    delimiter = " "
    for line in text:    
      while len(line) > charPerLine:
        breakPoint = line.find(delimiter, charPerLine)
        if breakPoint == -1:
          break   
        smallLines.append(line[0:breakPoint])
        line = line[breakPoint + 1:len(line)]
      smallLines.append(line)
    return smallLines    
      
# --------------------------------------------- sounds --------------------------------------------------
class gameSounds:
  bGTimeStarted = 0
  
  def __init__(self, bGTrack = makeEmptySound(1)):
    self.bGTrack = bGTrack
    
  #SOUND EFFECTS
  def soundEffect(self, sound):
    trackPath = getMediaPath() + sound + ".wav"
    track = makeSound(trackPath)
    play(track)

  #BACKGROUND MUSIC FUNCTIONS
  def startMusic(self):
    trackPath = getMediaPath() + "main.wav"
    self.bGTrack = makeSound(trackPath)
    self.bGTimeStarted = time.time()
    play(self.bGTrack)
  
  #checks the song duration and the last time that it was started
  #then calls the startBgMusic() if is isn't playing any longer
  #this can be called in lou of calling startBgMusic() completely, even for the first time
  def continueMusic(self):
    songDuration = getDuration(self.bGTrack)
    now = time.time()
    timePassed = now - self.bGTimeStarted
    if timePassed > songDuration:
      self.startMusic()
      
  def stopMusic(self):
    stopPlaying(self.bGTrack)
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Classes ++++++++++++++++++++++++++++++++++++++++++++++++++++
class player:
  # Represents the character in the game
  # attributes: inventory, gameRunning
  def __init__(self):
    self.inventory = inventory()
    self.gameRunning = true
     
class houseRooms:
  # Represents the rooms in the house and the current room
  # attributes: currentRoom, rooms
  def __init__(self, startingRoom):
    self.currentRoom = startingRoom
    self.getRooms()
  
  def getRooms(self):
  #             Map of home
  #                  N
  #                W + E
  #                  S
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
  #  Basement
  #  |---------------|
  #  |   Basement    |
  #  |  up Library   |
  #  |---------------|
  
    self.rooms = dict()
    # addRoom(roomName, roomToNorth, roomToSouth, roomToWest, RoomToEast, stairsUp, stairsDown, itemInRoom)
    self.addRoom("basement", "", "", "", "", "library")
    # 2nd floor rooms
    self.addRoom("bedroom", "", "billiard room", "bathroom", "", "", "", "Ledger")
    self.addRoom("billiard room", "bedroom", "", "master bedroom", "", "", "living room", "Joker")
    self.addRoom("master bedroom", "bathroom", "", "", "billiard room", "","", "Ace of Spades")
    self.addRoom("bathroom", "", "master bedroom", "", "bedroom", "", "", "Crumpled Note")
    # 1st floor rooms
    self.addRoom("kitchen", "", "library", "", "dining room", "", "", "Queen of Spades")
    self.addRoom("dining room", "", "living room", "kitchen", "", "", "", "Mysterious Note")
    self.addRoom("library", "kitchen", "", "", "living room", "", "basement", "King of Spades")
    self.addRoom("living room", "dining room", "", "library", "", "billiard room","", "")
    #return rooms
  
  def addRoom(self, roomName, roomToNorth, roomToSouth, roomToWest, RoomToEast, stairsUp = "", stairsDown = "", itemInRoom = ""):
    self.rooms[roomName] = singleRoom(getMediaPath() + roomName +".jpg", roomToNorth, roomToSouth, roomToWest, RoomToEast, stairsUp, stairsDown, itemInRoom)
  
  def changeRoom(self, direction, sound):
    newRoom = self.tryDirection(direction)
    if newRoom != self.currentRoom and newRoom != "":
      self.currentRoom = newRoom
      if direction == "u" or direction == "d":
        sound.soundEffect("stairs")
      else:
        sound.soundEffect("open door")
      return true
    return false # in the same room
  
  def tryDirection(self, direction):
    newRoom = ""
    currentRoom = self.rooms[self.currentRoom]
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
    
  def getRoomItem(self, player, visual):
    roomItem = self.rooms[self.currentRoom].itemInRoom
    if roomItem == "":
      return # no items in this room
    for item in player.inventory.currentItems:
      if roomItem == item:
        return # player already has item
    player.inventory.addItem(roomItem)
    visual.showInventory(makePicture(getMediaPath() + roomItem + ".jpg"), player.inventory.currentItems[roomItem])
    showInformation("This item is now in your inventory.")
    
class singleRoom:
  # Represents a room
  # attribute: picture, north, south, west, east, upDown
  def __init__(self, picture, north, south, west, east, stairsUp = "", stairsDown = "", itemInRoom = ""):
    self.picture = picture
    self.north = north
    self.south = south
    self.west = west
    self.east = east
    self.stairsUp = stairsUp
    self.stairsDown = stairsDown
    self.itemInRoom = itemInRoom
    
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
    
class inventory:
  # Represents character items
  # attributes: currentItems, possibleItems
  def __init__(self):
    self.currentItems = dict()
    self.getItems() # gets all possible items from txt file
  
  def __str__(self):
    itemsString = ""
    for item in self.currentItems:
      itemsString += item + "\n"
    return itemsString  
        
  def getItems(self):
    itemsFile = getTextFile("inventory items")
    delimiter = "$"
    self.possibleItems = dict()
    for line in itemsFile:
      itemAndDefinition = line.split(delimiter)
      self.possibleItems[itemAndDefinition[0].strip()] = itemAndDefinition[1].strip()
      
  def addItem(self, item):
    self.currentItems[item] = self.possibleItems.get(item)