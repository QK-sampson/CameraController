#!/usr/bin/env python
"""
CameraController script by Mikel
"""

import subprocess

#subprocess.call(['gphoto2','--auto-detect']) #0 is success, not 0 is exception
#subproccess.check_output returns the text that you would see in the terminal
cameraAvailable = False

def main():
    checkCamera()
    print cameraAvailable


def checkCamera():
    global cameraAvailable #<-- don't forget the global variables!
    
    cameraCheck = subprocess.check_output(['sudo','gphoto2','--auto-detect'])
#but...what if the return of 0 only means the call completed correctly
#not that the camera is actually available? 
    
    print cameraCheck
    if cameraCheck.find('Nikon DSC D5100') >= 0: #not found results in -1
        cameraAvailable = True
        print "Nikon DSC D5100 found"
    else :
        cameraAvailable = False #right now, checking only for my Nikon DSLR camera. More checks later maybe.


if __name__ == '__main__':
    main()


