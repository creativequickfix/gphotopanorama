# gphotopanorama
360 panorama with gphoto2
My Canon 60D only has 3 stops with AEB so I created this to allow for up to 7 brackets.
this script is reliant on a raspberry Pi with gphoto2 and Python 3
to install gphoto2:
sudo apt-get install gphoto2 libgphoto2*
sudo apt-get install python-pip
sudo pip install python-gphoto2
sudo pip3 install sh

to run:
python3 autobracket7.py


This file will ask if you're ready to take the first photo.  You must press 'y' to start.
Next it will take 7 bracketed photos starting at EV-3 going to EV3 in increments or 1......eg EV-3, EV-2, EV-1 etc.
Onces its done with the 7 shots it will prompt you to move to the next stop in your 360 photo.  You must press 'y' to continue.
once all 4 shots are taken it will create a folder on the Raspberry Pi called "Room - 1" and move all photos that were just taken off 
of the camera and into the folder.
next it will prompt you if you have another room to go to.  If 'y' it will then start at the begining asking if you're ready. 
If no it will end.

I am currently using a Canon 60D with the Sigma 8MM F3.5  as well as the Nordal Ninja 6  panohead at a 7.5degree up angle.  
This means I only need 4 shots around in a circle and the program is setup for that.

If you need more than 4 photos to complete a full cirlce you will need to go to the room_photos(): and change "while shots<=4:" to 
desired number of photos needed.

Under createSaveFolder(): is where you find the location the folders will be saved.  Modify this as needed

bracket7(): is where you find how many bracketed photos will be taken.  If you want to modify this 
you will need to run the command "gphoto2 --get-config exposurecompensation" to see what options are available to you.  
