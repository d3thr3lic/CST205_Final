#Nick Saunders
#This project is my test area for
#Visual ascepts of our final project

import os

def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  if fullPathToFile.startswith('/'):
    setMediaPath(os.path.dirname(fullPathToFile))
  else:
    setMediaPath(os.path.dirname(fullPathToFile) + '\\')
#Global Variables
ROOM1Image = getMediaPath() + "Room1.jpeg"
ROOM2Image = getMediaPath() + "Room2.jpeg"
ROOM3Image = getMediaPath() + "Room3.jpeg"
  
canvas = makeEmptyPicture(640,480)
room1 = makePicture(ROOM1Image)
room2 = makePicture(ROOM2Image) 
room3 = makePicture(ROOM3Image)
             
                         
                                     
                                                             
def background():
  setMediaPathToCurrentDir()
  global canvas
  global room1
  global room2
  global room3
  
  print(type(room1))
  userInput = requestString("Input function")
  
  if userInput == "room1":
    room1Fun()
  elif userInput == "room2":
    room2Fun()
  elif userInput == "room3":
    room3Fun()
  
  copyInto(room1,canvas,0,0)
  repaint(canvas)
  
def room1Fun():
  copyInto(room1,canvas,0,0)
  repaint(canvas)
  userInput = requestString("Input function")
  
  if userInput == "room1":
    showInformation("You are already in Room 1")
  elif userInput == "room2":
    room2Fun()
  elif userInput == "room3":
    room3Fun()

def room2Fun():
  copyInto(room2,canvas,0,0)
  repaint(canvas)
  userInput = requestString("Input function")
  
  if userInput == "room1":
    room1Fun()
  elif userInput == "room2":
    showInformation("You are already in Room 1")
  elif userInput == "room3":
    room3Fun()

def room3Fun():
  copyInto(room3,canvas,0,0)
  repaint(canvas)
  userInput = requestString("Input function")
  
  if userInput == "room1":
    room1Fun()
  elif userInput == "room2":
    room2Fun()
  elif userInput == "room3":
    showInformation("You are already in Room 1")

def textbox():
  return true