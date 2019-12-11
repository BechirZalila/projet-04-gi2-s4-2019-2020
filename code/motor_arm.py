from read_RPM import reader
from time import sleep
from I2C_LCD_driver import *
import pigpio
import recommended_frequency as R_F
import RPi.GPIO as GPIO

pi = pigpio.pi()
mylcd = I2C_LCD_driver.lcd()
ESC_GPIO = 23
RPM_GPIO = 22

while 1:
    recommended_number_turns= int(input("enter the desired number of turns (speed) : "))
    if(recommended_number_turns<7131 and recommended_number_turns>400):
        break
    

print(("you said  ") , (recommended_number_turns) )
inp= input("press enter to confirm ")
print(" =====> i got it :) " , recommended_number_turns )
sleep(1)
print("....\n")
print("...\n")
print("..\n.")
pi.set_servo_pulsewidth(ESC_GPIO, 0)
sleep(1)
inp = (input ("turn on 12 v and press enter ") )
pi.set_servo_pulsewidth(ESC_GPIO, 2500) # Maximum throttle.
sleep(5)
print("got max")
pi.set_servo_pulsewidth(ESC_GPIO, 1000) # Minimum throttle.
sleep(5)
print("got min")
sleep(2)
print("___GREAT___ : successful calibration ")
tach = reader(pi, RPM_GPIO)
try:
    speed = R_F.get_speed(recommended_number_turns)
    n=0
    while True:
        pi.set_servo_pulsewidth(ESC_GPIO, speed)

        n+=1
        if(n==18):
            print("please wait until I reach the desired speed ")
        if(n==38):
            print("thank you for waiting a little more i'm close")
        if(n==46):
            print("great i gather the recommended speed ")
        if(n>55):
            if(n%2==0):
                print("My current speed is :" , rpm )
                mylcd.lcd_display_string(str(rpm))
                time.sleep(1)
                mylcd.lcd_clear()
        rpm = int(tach.RPM())
        test=(rpm>recommended_number_turns)
        test1=(rpm<recommended_number_turns)
        rpm = int(tach.RPM())
        if(test):
            speed-=0.10
            pi.set_servo_pulsewidth(ESC_GPIO, speed)
            sleep(0.5)
            test=False
        if test1:
            speed+=0.05
            pi.set_servo_pulsewidth(ESC_GPIO, speed)
            sleep(0.5)
            test1=False
        rpm = int(tach.RPM())
        sleep(0.5)
            
    pi.set_servo_pulsewidth(ESC_GPIO, 0)
    pi.stop()
finally:
    pi.set_servo_pulsewidth(ESC_GPIO, 0)
    print("stop")
    pi.stop()
