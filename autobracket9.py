from sh import gphoto2 as gp
import signal, os, subprocess
from time import sleep

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

photos = True
shots = 1
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

def captureImages():
    captureCommand
    

def bracket9():
    exCo1 = 6
    expoComp1 = ["--set-config", "exposurecompensation""=""{}".format(exCo1)]
    step = 1
    while exCo1 <=24:
        print("Step {} of 7".format(step))
        expoComp1 = ["--set-config", "exposurecompensation""=""{}".format(exCo1)]
        gp(expoComp1)
        gp(captureCommand)
        exCo1 += 3
        step +=1
def room_photos():
    global shots
    while shots <=4:
        print("Location {}".format(shots))
        x= input("Are you ready to take the photos: 'y' or 'n' ")
        if x[0].lower() == 'y':
            bracket9()
            shots += 1
        else:
            print('Please try again')
            continue

killGphotoProcess()
gp(clearCommand)
while True:
    global roomNumber
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
        


