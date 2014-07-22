What I want my Camera script to do:

1. Control my DSLR though GPhoto2 commands. --done

2. Take a timelapse photo series. --done

3. Trigger the camera to take a picture using the Raspberry Pi motion sensor.

4. Use error handling for any cases where the camera does not take a store the image for any reason. --partially done

5. Have built-in tests to verify each of these functions. (According to TDD the code writing should start with the tests.)

6. New idea: Upload photos to Dropbox as they are taken. I have installed the dropbox package for Python, and next need to read the tutorial and documentation to learn how to use it. 
 
7. Fun ideas for future enhancement:
	Get a Raspberry Pi GPS unit and geotag the pictures.
	Connect a battery pack to make everything portable.
	Make a carry-able case for the entire unit.

Note at 04:48 Tuesday July 22: So far, attempts at doing an overnight timelapse from the office window have failed with the DSLR, due partly to low light conditions (though I add an extra lamp for lighting outside) and short battery life. With the webcam, even when it is set to maximum sensitivity in the config file, and with the lamp, overnight is still too dark. I am still hopeful that I might get some good shots at sunup. The webcam is continuing reliably even when the images are black from insufficient light, unlike the DSLR. 

