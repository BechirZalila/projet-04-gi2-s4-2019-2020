import pigpio
import RPi.GPIO as GPIO
from time import sleep
from read_RPM import reader

pi = pigpio.pi()

ESC_GPIO = 23
RPM_GPIO = 22
SAMPLE_TIME = 2

file = open("freq", "a")
print ("turn on 12 v and press enter")
inp=input()
pi.set_servo_pulsewidth(ESC_GPIO, 2500) # Maximum throttle.
sleep(5)
print("got max")
pi.set_servo_pulsewidth(ESC_GPIO, 1000) # Minimum throttle.
sleep(5)
print("got min")
# Set up RPM reader

tach = reader(pi, RPM_GPIO)
try:
    speed = 1010
    while True :
        pi.set_servo_pulsewidth(ESC_GPIO, speed)
        sleep(5)
        rpm = int(tach.RPM())
        
        
        file.write(str(rpm)+"/"+str(speed))
        file.write("\n")
        
        pi.set_servo_pulsewidth(ESC_GPIO, speed)
        sleep(5)
        rpm = int(tach.RPM())

        file.write(str(rpm)+"/"+str(speed))

        
        file.write("\n")
        file.write("\n")
        file.write("\n")
        
        if(speed>=2496):
            file.close()
            print("file est bien fermée")
            print("------------------------finish--------don't forget to disable the over clock--------------------")
            break
        speed+=2
    try:
        file.close()
    except:
        print("deja file est fermée")
finally:
    try:
        file.close()
    except:
        print("deja file est fermée")
    pi.set_servo_pulsewidth(ESC_GPIO, 0) # Stop servo pulses.
    print("stop")
    pi.stop() # Disconnect pigpio.
