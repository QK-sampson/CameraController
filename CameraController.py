#!/usr/bin/env python
# -- coding: utf-8 --
"""
CameraController.py script by Mikel

07/18/2014
Initial writing of script. I successfully called GPhoto2 from Python
to confirm that my (specific) camera is connected. I am thinking though
how a test harness would be written for the checkCamera function, and
I need to doublecheck what exceptions that the subprocess call might throw
and add exception handling.

07/19/2014
Added the "takeOnePhoto" method and tested sucessfully.
Added takeTimeLapse method. 
As of 10:37, successful test of both takeOnePhoto and takeTimeLapse

Nikon DSC D5100 found
['sudo', 'gphoto2', '--capture-image', '-F', '2', '-I', '10']
Time-lapse mode enabled (interval: 10s).
Capturing frame #1/2...
'New file is in location /store_00010001/capt0000.jpg on the camera
Waiting for next capture slot 0 seconds...
Capturing frame #2/2...
New file is in location /store_00010001/capt0001.jpg on the camera

Note: Gphoto2 stops working at times and is fixed by reboot. Would like to find a way to
check and reset the process from within this script. 

"""
#TODO: add configuration values as global variables


import subprocess, sys, time
import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)

pir_pin=18
io.setup(pir_pin, io.IN)

def main():    
    keepGoing = True
    while keepGoing:
        if checkCamera():            
            choice = input("What do you want to do? Select 1 for single photo, 2 for timelapse, 3 for motion sensor trigger. ")
            if choice == "1":
                takeOnePhoto()
                keepGoing = False
            elif choice == "2":
                takeTimeLapse()
                keepGoing = False
            elif choice == "3":
                checkMotionSensor()               
                keepGoing = False
            else:
                print ("You have not chosen a valid option. Try again.")
        else:
            keepGoing = False
                


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
    
    try:
        #take one picture and download it to the folder containing the script
        #Need to add code to specify the name of the photo to avoid file name conflicts
        subprocess.check_output(['sudo','gphoto2','--capture-image-and-download', '--force-overwrite'])
        
    except:
        print ("Oops something went wrong taking a single photo! ")
        print (sys.exc_info())
        print (sys.exc_type)

def takeTimeLapseArgs(numOfFrames, intervalInSecs):
    output = ''
    try:
        #there is a problem if there is already a file with the default filename in the save location
        #The subprocess output shows that the process is trying to propmt the user to see if they want to overwrite
        #the existing file, but right now there is not a way to communicate back to the process. Look into this later.
        #Need to add code to specify the name of the photo to avoid file name conflicts
        gphotocommand = ['sudo','gphoto2','--capture-image', '-F', str(numOfFrames), '-I', str(intervalInSecs)]
        #print gphotocommand
        output = subprocess.check_output(gphotocommand)
        print (output)
        
    except:
        print ('Oops something went wrong with your timelapse command! ') 
        

def takeTimeLapse():
    frames = input("How many frames do you want for your timelapse? Type an integer and press enter ")
    interval = input("How many seconds between shots for your timelapse? Type an integer and press enter" )
    #later, add validation to make sure the inputs are integers
    takeTimeLapseArgs(int(frames), int(interval))


def checkMotionSensor():
    global pir_pin
    #getting "no access to /dev/mem, try running as root!" even when I open IDLE under sudo.
    #to resolve later. (I updated GPIO to the latest, and moved from Python 2.7 to 3.2)

    #RuntimeError: You must setup() the GPIO channel first <-- this is the next error to address. Tomorrow.
    #I was missing this line of code: io.setup(pir_pin, io.IN)
    while True:
        if io.input(pir_pin): 
            print("Don't Blink!")
            #takeOnePhoto() #comment this line to test without the camera
            time.sleep(1)
        
    io.cleanup()
    

if __name__ == '__main__':
    main()



