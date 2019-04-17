import time

#mock game so that functions can be defined correctly and globals don't have to be used
def game():
  #thie list contains two items, an empty sound, and the time that the sound was started
    #this will need to be added in the main game function
  bgMusicInfo = [makeEmptySound(1), 0]
  
  startBgMusic(bgMusicInfo)
  
  #simulates game loop and game actions
  while True:
    userCmd = requestString("What do you want to do next?")
    continueBgMusic(bgMusicInfo)


#SOUND EFFECTS
#================================================================================================
#================================================================================================
#these will be cleaned up more later, this section is a work in progress
def jumpSound(versionNum):
  setMediaPathToCurrentDir()
  trackPath = getMediaPath() + "jump" + str(versionNum) + ".wav"
  track = makeSound(trackPath)
  play(track)
  #explore(track)

def jumpingOnBedSound():
  setMediaPathToCurrentDir()
  trackPath = getMediaPath() + "jumping_on_a_bed.wav"
  track = makeSound(trackPath)
  play(track)
  
def fallSound(versionNum):
  setMediaPathToCurrentDir()
  trackPath = getMediaPath() + "fall" + str(versionNum) + ".wav"
  track = makeSound(trackPath)
  play(track)



#BACKGROUND MUSIC FUNCTIONS
#================================================================================================
#================================================================================================
#call this to initiate the bg music. This should only get called once at the beginning of the game
def startBgMusic(bgMusicInfo):
  #sets the media path to the current working dir
  setMediaPathToCurrentDir()
  trackPath = getMediaPath() + "jumping_on_a_bed.wav"
  #sets the bgMusicInfo information
  bgMusicInfo[0] = makeSound(trackPath)
  bgMusicInfo[1] = time.time()
  play(bgMusicInfo[0])

#uses the music info stored in the game to continue the bg music if it is still playing
def continueBgMusic(bgMusicInfo):
  if not isSongStillPlaying(bgMusicInfo):
    startBgMusic(bgMusicInfo)

#checks the song duration and the last time that it was started
#returns if the song is still playing
def isSongStillPlaying(bgMusicInfo):
  songDuration = getDuration(bgMusicInfo[0])
  now = time.time()
  timePassed = now - bgMusicInfo[1]
  if timePassed > songDuration:
    return False
  else:
    return True
#================================================================================================



















#to allow mediaPath to be correct an linux, macos and windows.
def setMediaPathToCurrentDir():
  fullPathToFile = os.path.abspath(__file__)
  if fullPathToFile.startswith('/'):
    setMediaPath(os.path.dirname(fullPathToFile))
  else:
    setMediaPath(os.path.dirname(fullPathToFile) + '\\')