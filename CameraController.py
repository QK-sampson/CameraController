#!/usr/bin/env python
"""
CameraController script by Mikel

07/18/2014
Initial writing of script. I successfully called GPhoto2 from Python
to confirm that my (specific) camera is connected. I am thinking though
how a test harness would be written for the checkCamera function, and
I need to doublecheck what exceptions that the subprocess call might throw
and add exception handling. 
"""

import subprocess

#subprocess.call(['gphoto2','--auto-detect']) #0 is success, not 0 is exception
#subproccess.check_output returns the text that you would see in the terminal
cameraAvailable = False

def main():
    global cameraAvailable
    cameraAvailable = checkCamera()


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

if __name__ == '__main__':
    main()


