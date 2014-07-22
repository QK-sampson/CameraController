#!/usr/bin/env python
# -- coding: utf-8 --
"""
CameraControllerWebcam.py script by Mikel

Copied my code from CameraController.py, and modifying it to work with webcam.

"""
import subprocess, sys, time
import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)

pir_pin=18
io.setup(pir_pin, io.IN)

webcamconfig = '/home/pi/CameraController/fswebcam.conf'
filepath = '/home/pi/CameraController/lvl1/lvl1_'
maxpictures = 10

def main():    
    keepGoing = True
    while keepGoing:         
        choice = input("What do you want to do? Select 1 for single photo, 2 for motion sensor trigger, 3 for TimeLapse. ")
        if choice == "1":
            takeOnePhoto()
            print("done!")
            keepGoing = False        
        elif choice == "2":
            checkMotionSensor()
            print("done!")
            keepGoing = False
        elif choice == "3":
            takeTimeLapse(20,1)
            print("done!")
            keepGoing = False
        else:
            print ("You have not chosen a valid option. Try again.")


def takeOnePhoto():
    global webcamconfig, filepath
    try:
        #take one picture and download it to the folder containing the script
        #Need to add code to specify the name of the photo to avoid file name conflicts
        subprocess.check_output(['sudo','fswebcam','-c',webcamconfig,filepath + str(time.time()) + '.jpeg'])
        
    except:
        print ("Oops something went wrong taking a single photo! ")
 

def takeTimeLapse(frames,intervalSeconds):
    global webcamconfig, filepath
    try:
        #take one picture and download it to the folder containing the script
        #Need to add code to specify the name of the photo to avoid file name conflicts
        #This command takes a time lapse but keeps overwritting the same filename.
        #subprocess.check_output(['sudo','fswebcam', '-l', str(frames), '--offset', str(intervalSeconds),'-c',webcamconfig,filepath + str(time.time()) + '.jpeg'])
        count = 0
        while count < frames:
            takeOnePhoto()
            time.sleep(intervalSeconds)
            count += 1
    except:
        print ("Oops something went wrong taking a single photo! ")
       

def checkMotionSensor():
    #TODO: build in a way to camcel motion sensor monitering by pressing a key
    global pir_pin,maxpictures
    maxphotos = input("What is the maximum number of picture you want to be triggered by the motion sensor? ")
    maxpictures = int(maxphotos)
    count = 0
    print('10 second delay')
    time.sleep(10)
    keeplooping = True
    while keeplooping:
        if io.input(pir_pin): 
            #print("Smile for the camera!")
            takeOnePhoto()
            count += 1
            print('Photo count '+str(count))
        if count >= maxpictures:
            keeplooping = False        
    io.cleanup()
    

if __name__ == '__main__':
    main()



