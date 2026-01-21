#imports
import pygame       
import time            
import random          

#initializes pygame
pygame.init()
#screen
breedte = 800       
hoogte = 600           
screen = pygame.display.set_mode((breedte, hoogte))


def Mainscreen():
  
  background = pygame.image.load("Pictures/THumbnail.png") 
  screen.blit(background, (-50, 0))

  pygame.mixer.music.load("Music/Forestm.wav")
  pygame.mixer.music.play(-1)

  startbutton = pygame.image.load("Pictures/Startbutton.png")
  startbuttonrect = startbutton.get_rect()

  exitbutton = pygame.image.load("Pictures/Exitbutton.png")
  exitbuttonrect = exitbutton.get_rect()

  while True:
      startbuttonrect.center = (400, 350)
      screen.blit(startbutton, startbuttonrect)
  
      exitbuttonrect.center = (400, 500)
      screen.blit(exitbutton, exitbuttonrect)
      pygame.display.flip()
    

      pygame.event.get()
      locatie_muis = pygame.mouse.get_pos()
      knoppen = pygame.mouse.get_pressed()
    
      if knoppen[0] == 1:
        if startbuttonrect.collidepoint(locatie_muis):
           Maingame()
        if exitbuttonrect.collidepoint(locatie_muis):
          exit()
def Maingame():
  
  background2 = pygame.image.load("Pictures/Forest.png")
  background2 = pygame.transform.scale(background2, (1000, 700))
  background3 = pygame.image.load("Pictures/THumbnail.png")
  pygame.mixer.music.load("Music/Forestm.wav")
  pygame.mixer.music.play(-1)

#loads the Dragon + makes a rect
  FDPA_origineel = pygame.image.load("Pictures/FDPA.png")
  FDPA_origineel = pygame.transform.rotozoom(FDPA_origineel, 0, 0.3)
  FDPA = pygame.image.load("Pictures/FDPA.png")
  FDPA_rechthoek = FDPA.get_rect()
  FDPA_rechthoek.center = (300,150)

  #loads the DF + makes a rect
  DF = pygame.image.load("Pictures/DF.jpg")
  DF = pygame.transform.scale(DF, (100, 100))
  DF.get_rect()
  DF_rechthoek = DF.get_rect()
  DF_rechthoek.center = (100,100)
  #Speed
  snelheid = [-1, -1]

  #Variables
  draak_leeft = True      
  honger = 0            
  spring_teller = 0

  #Main Game
  while draak_leeft:
    spring_teller = spring_teller + 1   #+1
    font = pygame.font.SysFont(None,30)
    honger_tekst = font.render(f"Honger:{int(honger)}",True, (0,0,0))
    screen.blit(honger_tekst,(10,10))
    # draws the rect of the dragon
    pygame.draw.rect(screen, (100,100,100), FDPA_rechthoek, -1)

    # updates the screen
    pygame.display.flip()
    # makes the screen empty with the background colour

    #draws the dragon and the dragonfruit on there places.
    screen.blit(background2, (-50, 0))
    screen.blit(FDPA, FDPA_rechthoek)
    screen.blit(DF, DF_rechthoek)

    #Placement
    if spring_teller == 10:
      sla_x = random.randint(100,400) 
      sla_y = random.randint(100,200)  
      DF_rechthoek.center = (sla_x, sla_y)
      spring_teller = 0                 

    #hunger is comming
    honger = honger + 0.5
    if honger < 0:
      honger = 0
    

    #kills the dragon
    if honger > 100:
      draak_leeft = False
      screen.blit(background2, (-50, 0))
      Mainscreen()
      
    # events
    pygame.event.get()
    locatie_muis = pygame.mouse.get_pos()
    knoppen = pygame.mouse.get_pressed()

    #hunger -
    if knoppen[0] == 1:
      if DF_rechthoek.collidepoint(locatie_muis):
        honger = honger - 5 

    # save the middle of the dragon
    midden = FDPA_rechthoek.center

    #make the dragon bigger when eating
    FDPA = pygame.transform.rotozoom(
        FDPA_origineel, 0, (100-honger)/100
    )

    #size, placement, movement
    FDPA_rechthoek = FDPA.get_rect()
    FDPA_rechthoek.center = midden
    FDPA_rechthoek = FDPA_rechthoek.move(snelheid)

    #flip the picture
    if FDPA_rechthoek.right > breedte or FDPA_rechthoek.left < 0:
      snelheid[0] = -snelheid[0]
      FDPA_origineel = pygame.transform.flip(
        FDPA_origineel, True, False
    )

    #Bounce mechanic
    if FDPA_rechthoek.bottom > hoogte or FDPA_rechthoek.top < 0:
      snelheid[1] = -snelheid[1]
  
    time.sleep(0.1)
  #Game over
  print('Helaas, je Draak is overleden')

Mainscreen()