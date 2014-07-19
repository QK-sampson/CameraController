#!/usr/bin/env python
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
New file is in location /store_00010001/capt0000.jpg on the camera
Waiting for next capture slot 0 seconds...
Capturing frame #2/2...
New file is in location /store_00010001/capt0001.jpg on the camera

Note: Gphoto2 stops working at times and is fixed by reboot. Would like to find a way to
check and reset the process from within this script. 

"""
#TODO: add configuration values as global variables


import subprocess, sys


def main():
    keepGoing = True
    while keepGoing:
        if checkCamera():
            choice = raw_input("What do you want to do? Select 1 for single photo, 2 for timelapse. ")
            if choice == "1":
                takeOnePhoto()
                keepGoing = False
            elif choice == "2":
                takeTimeLapse()
                keepGoing = False
            else:
                print "You have not chosen a valid option. Try again."
                


def checkCamera():
    isCameraConnected = False
    cameraCheck = subprocess.check_output(['sudo','gphoto2','--auto-detect'])

    if cameraCheck.find('Nikon DSC D5100') >= 0: #not found results in -1        
        print "Nikon DSC D5100 found"
        isCameraConnected = True
    else:
        print "Nikon DSC D5100 NOT found"
        isCameraConnected = False

    return isCameraConnected


def takeOnePhoto():
    
    try:
        #take one picture and download it to the folder containing the script
        subprocess.check_output(['sudo','gphoto2','--capture-image-and-download'])
        
    except:
        print "Oops something went wrong taking a single photo! " 
        print sys.exc_info()
        print sys.exc_type

def takeTimeLapseArgs(numOfFrames, intervalInSecs):
    output = ''
    try:
        gphotocommand = ['sudo','gphoto2','--capture-image', '-F', str(numOfFrames), '-I', str(intervalInSecs)]
        print gphotocommand
        output = subprocess.check_output(gphotocommand)
        print output
        
    except:
        print "Oops something went wrong with your timelapse command! " 
        print sys.exc_info()
        print sys.exc_type

def takeTimeLapse():
    frames = raw_input("How many frames do you want for your timelapse? Type an integer and press enter ")
    interval = raw_input("How many seconds between shots for your timelapse? Type an integer and press enter" )
    #later, add validation to make sure the inputs are integers
    takeTimeLapseArgs(int(frames), int(interval))
    
    

if __name__ == '__main__':
    main()



