import Adafruit_BBIO.GPIO as GPIO
import time
 
print "wait"
time.sleep(30)
GPIO.setup("P8_36", GPIO.OUT)
GPIO.output("P8_36", GPIO.HIGH)
print "Go"
time.sleep(30)
GPIO.cleanup()

