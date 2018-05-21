import numpy as np
import cv2
import time
import argparse
from pynput.keyboard import Key,Listener
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
import smtplib

#mail info
user='user@gmail.com'
pwd='password'
From='user@gmail.com'
To='receipient@gmail.com'

parser = argparse.ArgumentParser(description='facesent - face detecting sentinel')

parser.add_argument('-d', '--delay', default=3, type=int,
                    help="delay before start (default 3s)", metavar="S")
parser.add_argument('-u', '--unlock-period', default=5, type=int,
                    help="period before locking (default 5s)", metavar="S")
parser.add_argument('-p', '--password', default='asdf',
                    help="delay before start (default \"asdf\")", metavar="P")
parser.add_argument('-i', '--image', default='tmpimage.jpg',
                    help="file name of the output image (default \"tmpimage.jpg\")", metavar="F")
parser.add_argument('-c', '--classifier', default='haarcascade_frontalface_alt.xml',
                    help="file name of the classifier (default \"haarcascade_frontalface_alt.xml\")", metavar="F")

args = parser.parse_args()
print(args)

# TODO split operations into functions
# TODO add to argparse:
# - email and related
# - detect mode (password, mouse location)
# - reaction mode (email, track, lock, shut down)
# - read cofig file with the same as the above settings

# delay before start
print("Sleeping for {}s".format(args.delay))
time.sleep(args.delay)


currently_pressed_key = None
start_time= time.time()
inp=[]
#Take user keystrokes, if 5 seconds pass or space is pressed key pressed are
#compared with testinp at the end of this function to check if it is the
#required password, if not we start the face recognition part

while True:
    def on_press(key):
        if key == Key.space or int(time.time()-start_time) > args.unlock_period:
            return False
        print('{0} pressed'.format(key))
        if hasattr(key, 'char'):
            inp.append(key.char)
    with Listener(
        on_press=on_press) as listener:
        listener.join()
    if int(time.time()-start_time) > int(0):
        break

# TODO move input check inside the loop
inp=''.join(inp)
#katagrafi eikonas an to password einai lathos
if inp != args.password:
#face recognition using opencv and haarcascade classifier
    face_cascade = cv2.CascadeClassifier(args.classifier)
    #capture image from camera (0)
    cap = cv2.VideoCapture(0)
    framecounter=0
    
    # TODO collect more than one images
    
    while framecounter ==0:
        ret, frame = cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray, 1.3, 5)
#if a face is detected we capture the image and send the mail. Then the camera
#and mailserver connection are closed and the script is terminated
        for (x,y,w,h) in faces:
            cv2.imwrite(args.image, frame)
            framecounter=1

            print("Skipped email!")
            break
            img_data = open(args.image,'rb').read()
            msg= MIMEMultipart()
            msg['Subject'] = 'Laptop Login'
            msg['From']='mail@gmail.com'
            msg['To']='mail@gmail.com'
            text = MIMEText('Someone has your laptop')
            msg.attach(text)
            image=MIMEImage(img_data, name= os.path.basename(args.image))
            msg.attach(image)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(user, pwd)
            server.sendmail(From, To, msg.as_string())
            server.close()

    cap.release()
    cv2.destroyAllWindows()

#TODO:
#script runs when computer wakes up or comes out of idle mode
