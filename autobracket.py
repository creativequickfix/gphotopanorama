from typing import List

from sh import gphoto2 as gp
import signal, os, subprocess

# kill gphoto2 process that starts
# whenever the camera is connected

def killGphotoProcess():
    p = subprocess.Popen(['ps','-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    # search for the line that has the process
    # we want to kill
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            # kill the process
            pid = int(line.split(None,1) [0])
            os.kill(pid, signal.SIGKILL)
    print('Application killed')

exposures = {0:["--set-config", "exposurecompensation""=""-5"],1:["--set-config", "exposurecompensation""=""-4.6"],
            2:["--set-config", "exposurecompensation""=""-4.3"],3:["--set-config", "exposurecompensation""=""-4"],
            4:["--set-config", "exposurecompensation""=""-3.6"],5:["--set-config", "exposurecompensation""=""-3.3"],
            6:["--set-config", "exposurecompensation""=""-3"],7:["--set-config", "exposurecompensation""=""-2.6"],
            8:["--set-config", "exposurecompensation""=""-2.3"],9:["--set-config", "exposurecompensation""=""-2"],
            10:["--set-config", "exposurecompensation""=""-1.6"],11:["--set-config", "exposurecompensation""=""-1.3"],
            12:["--set-config", "exposurecompensation""=""-1.0"],13:["--set-config", "exposurecompensation""=""-0.6"],
            14:["--set-config", "exposurecompensation""=""-0.3"],15:["--set-config", "exposurecompensation""=""0"],
            16:["--set-config", "exposurecompensation""=""0.3"],17:["--set-config", "exposurecompensation""=""0.6"],
            18:["--set-config", "exposurecompensation""=""1.0"],19:["--set-config", "exposurecompensation""=""1.3"],
            20:["--set-config", "exposurecompensation""=""1.6"],21:["--set-config", "exposurecompensation""=""2"],
            22:["--set-config", "exposurecompensation""=""2.3"],23:["--set-config", "exposurecompensation""=""2.6"],
            24:["--set-config", "exposurecompensation""=""3"],25:["--set-config", "exposurecompensation""=""3.3"],
            26:["--set-config", "exposurecompensation""=""3.6"],27:["--set-config", "exposurecompensation""=""4"],
            28:["--set-config", "exposurecompensation""=""4.3"],29:["--set-config", "exposurecompensation""=""4.6"],
            30:["--set-config", "exposurecompensation""=""5"]}
photos = True
clearCommand = ["--folder","/store_00020001/DCIM/100CANON", \
                "-R", "--delete-all-files"]
captureCommand = ["--capture-image"]
downloadCommand = ["--get-all-files"]
roomNumber = 1
currentExpoComp = ["--get-config", "exposurecompensation"]

def createSaveFolder():
    global roomNumber
    folder_name = 'Room - ' + '{}'.format(roomNumber)
    save_location = '/home/pi/Desktop/gphoto/images/' + folder_name
    try:
        os.makedirs(save_location)
    except:
        print('Failed to create new directory.')
    os.chdir(save_location)
    
def set_exposure():
    gp(exposures[exco])

def bracket7():
    exco = 3
    step = 1
    while exco <=27:
        print("Step {} of 7".format(step))
        gp(exposures[exco])
        gp(captureCommand)
        exco += 3
        step +=1

def room_photos():
    shots = 1
    while shots <=4:
        print("Location {}".format(shots))
        x= input("Are you ready to take the photos: 'y' or 'n' ")
        if x[0].lower() == 'y':
            bracket7()
            shots += 1
        else:
            print('Please try again')
            continue

killGphotoProcess()
gp(clearCommand)
while True:
    shots = 1
    while photos:
        print("Taking Photos, Please Wait")
        room_photos()
        print("Creating Folder")
        createSaveFolder()
        print("Downloading Photos. This my take a min")
        gp(downloadCommand)
        print("Deleting Photos from Camera")
        gp(clearCommand)
        print("Room Complete")
        roomNumber +=1
        break

    new_room = input("Continue to next Room? 'y' or 'n' ")
    if new_room[0].lower() == 'y':
        shots = 1
        photos = True
        
    else:
        print("Photo Shoot Complete!")
        break
        


