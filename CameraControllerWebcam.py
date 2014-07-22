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
filepath = '/media/3BAA-1848/webcam/python/'
maxpictures = 10

def main():    
    keepGoing = True
    while keepGoing:         
        choice = input("What do you want to do? Select 1 for single photo, 2 for motion sensor trigger. ")
        if choice == "1":
            takeOnePhoto()
            print("done!")
            keepGoing = False        
        elif choice == "2":
            checkMotionSensor()
            print("done!")
            keepGoing = False
        else:
            print ("You have not chosen a valid option. Try again.")

def checkCamera():
    global cameraCheck
    isCameraConnected = False
    cameraCheck = subprocess.check_output(['sudo','gphoto2','--auto-detect'])
    print (cameraCheck)
    #encoding the find string as UTF seems to have resolve the TypeError when I run with Python 3
    if cameraCheck.find(('Nikon DSC D5100').encode("utf-8")) >= 0: #not found results in -1        
        print ('Nikon DSC D5100 found')
        isCameraConnected = True
    else:
        print ('Nikon DSC D5100 NOT found')
        isCameraConnected = False   

    #return isCameraConnected
    return True #disabling the cameracheck to test the rest of the script

def takeOnePhoto():
    global webcamconfig, filepath
    try:
        #take one picture and download it to the folder containing the script
        #Need to add code to specify the name of the photo to avoid file name conflicts
        subprocess.check_output(['sudo','fswebcam','-c',webcamconfig,filepath + str(time.time()) + '.jpeg'])
        
    except:
        print ("Oops something went wrong taking a single photo! ")
        print (sys.exc_info())
        print (sys.exc_type)


def checkMotionSensor():
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



