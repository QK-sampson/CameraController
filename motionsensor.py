import time
import pygame
import RPi.GPIO as io
io.setmode(io.BCM)

pir_pin = 18
#door_pin = 23
motioncounter = 0
#doorcounter = 0

io.setup(pir_pin, io.IN)
#io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)

pygame.mixer.init()
pygame.mixer.music.load("sounds/dontblink2.mp3")


while True:
    if io.input(pir_pin):
        #motioncounter = motioncounter + 1
        print("Don't Blink!")
        pygame.mixer.music.play()
        time.sleep(3)
    #if io.input(door_pin):
    #    doorcounter = doorcounter + 1 
    #    print("DOOR ALARM" + str(doorcounter))
    time.sleep(0.5)
        
