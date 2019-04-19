import time

#mock game so that functions can be defined correctly and globals don't have to be used
def game():
  isMusicOn = True
  gs = GameSounds()
  if isMusicOn:
    gs.startMusic()
    
  #simulates game loop and game actions
  while True:
    userCmd = requestString("What do you want to do next?")
    
    #this should be called every time that game loop comes around to ensure that the music continues
    #if the user wants it on. It will be on by default every game
    if isMusicOn:
      gs.continueMusic()
    
    #here are examples of how each of the sound effects are used
    #as well as how the music start and stop are used
    if userCmd == "jump":
      gs.jumpSound()
    elif userCmd == "jump on bed":
      gs.jumpingOnBedSound()
    elif userCmd == "fall":
      gs.fallSound()
    elif userCmd == "dance":
      gs.danceSound()
    elif userCmd == "run":
      gs.runningSound()
    elif userCmd == "cry":
      gs.cryingSound()
    elif userCmd == "scream":
      gs.screamSound()
    elif userCmd == "laugh":
      gs.laughingSound()
    elif userCmd == "jump scare":
      gs.stopMusic() #maybe stop the music for effect?
      gs.jumpScare()
    elif userCmd == "stop music":
      #if this isn't called, then the music will continue until it finishes
      gs.stopMusic()
      isMusicOn = False
    elif userCmd == "start music" and isMusicOn == False: #checking to see that the music isn't already on will help prevent stacking of music
      isMusicOn = True
      #needs to call startMusic() instead of continueMusic() when restarting after stopping
      #beware of calling this twice, the music will stack up if you do, and stopMusic() wont stop all instances
      gs.startMusic()
    elif userCmd == "exit" or userCmd == "quit":
      gs.stopMusic()
      break
    
class GameSounds:
  bGTimeStarted = 0
  
  def __init__(self, bGTrack = makeEmptySound(1)):
    self.bGTrack = bGTrack
    self.setMediaPathToCurrentDir()
    
  #SOUND EFFECTS
  #================================================================================================
  #================================================================================================
  #these will be cleaned up more later, this section is a work in progress
  def jumpSound(self):
    trackPath = getMediaPath() + "jump.wav"
    track = makeSound(trackPath)
    play(track)
  
  def jumpingOnBedSound(self):
    trackPath = getMediaPath() + "jumping_on_a_bed.wav"
    track = makeSound(trackPath)
    play(track)
    
  def fallSound(self):
    trackPath = getMediaPath() + "fall.wav"
    track = makeSound(trackPath)
    play(track)
    
  def jumpScare(self):
    trackPath = getMediaPath() + "jump_scare.wav"
    track = makeSound(trackPath)
    play(track)
    
  def danceSound(self):
    trackPath = getMediaPath() + "dance.wav"
    track = makeSound(trackPath)
    play(track)
    
  def runningSound(self):
    trackPath = getMediaPath() + "running.wav"
    track = makeSound(trackPath)
    play(track)
    
  def cryingSound(self):
    trackPath = getMediaPath() + "crying.wav"
    track = makeSound(trackPath)
    play(track)
  
  def screamSound(self):
    trackPath = getMediaPath() + "scream.wav"
    track = makeSound(trackPath)
    play(track)
   
  def laughingSound(self):
    trackPath = getMediaPath() + "laughing.wav"
    track = makeSound(trackPath)
    play(track)
  
  #BACKGROUND MUSIC FUNCTIONS
  #================================================================================================
  #================================================================================================
  #This will actually do the playing of the music, but doesn't need to be called by game()
  def startMusic(self):
    trackPath = getMediaPath() + "detuned_piano.wav"
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
  #================================================================================================
  
  #to allow mediaPath to be correct an linux, macos and windows.
  def setMediaPathToCurrentDir(self):
    fullPathToFile = os.path.abspath(__file__)
    if fullPathToFile.startswith('/'):
      setMediaPath(os.path.dirname(fullPathToFile))
    else:
      setMediaPath(os.path.dirname(fullPathToFile) + '\\')