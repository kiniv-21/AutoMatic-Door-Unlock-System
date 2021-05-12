import RPi.GPIO as GPIO
import time
import cv2

button = 16


def setup():
       GPIO.setmode(GPIO.BOARD)
       GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
       

def loop():
        while True:
              button_state = GPIO.input(button)
              if  button_state == False:  
                  capture()

def endprogram():
         
       GPIO.cleanup()

         
def capture():
# initialize the camera
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()
    cv2.imshow('SnapshotTest',image)
    #cv2.waitKey(0)
    cv2.destroyWindow('SnapshotTest')
    cv2.imwrite('/home/pi/SnapshotTest.jpg',image)
    
    cam.release()


if __name__ == '__main__':
          
          setup()
          
          try:
                 loop()
          
          except KeyboardInterrupt:
                 print ('keyboard interrupt detected') 
                 endprogram()
