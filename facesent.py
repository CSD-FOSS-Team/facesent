import numpy as np
import cv2
import time
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

image_filename = "tmpimage.jpg"

currently_pressed_key = None
start_time= time.time()
inp=[]
#Take user keystrokes, if 5 seconds pass or space is pressed key pressed are
#compared with testinp at the end of this function to check if it is the
#required password, if not we start the face recognition part
while True:
    def on_press(key):
        if key == Key.space or int(time.time()-start_time) > int(5):
            return False
        print('{0} pressed'.format(key))
        if hasattr(key, 'char'):
            inp.append(key.char)
    with Listener(
        on_press=on_press) as listener:
        listener.join()
    if int(time.time()-start_time) > int(0):
        break

inp=''.join(inp)
#required password to check
testinp='asdf'
#katagrafi eikonas an to password einai lathos
if inp != testinp:
#face recognition using opencv and haarcascade classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    #capture image from camera (0)
    cap = cv2.VideoCapture(0)
    framecounter=0
    while framecounter ==0:
        ret, frame = cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)       
        faces=face_cascade.detectMultiScale(gray, 1.3, 5)
#if a face is detected we capture the image and send the mail. Then the camera
#and mailserver connection are closed and the script is terminated
        for (x,y,w,h) in faces:
            cv2.imwrite(image_filename, frame)
            framecounter=1

            print("Skipped email!")
            break
            img_data = open(image_filename,'rb').read()
            msg= MIMEMultipart()
            msg['Subject'] = 'Laptop Login'
            msg['From']='mail@gmail.com'
            msg['To']='mail@gmail.com'
            text = MIMEText('Someone has your laptop')
            msg.attach(text)
            image=MIMEImage(img_data, name= os.path.basename(image_filename))
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
