import Adafruit_BBIO.PWM as PWM
import time
#PWM.start(channel, duty, freq=2000, polarity=0)
#PWM.start("P9_14", 50, 2000000)


if __name__ == "__main__":


	#PWM.start(channel, duty, freq=2000, polarity=0)
	print "Wait"
	time.sleep(30)
	print "Go!"
	PWM.start("P8_36", 100, 200000)

	time.sleep(30)	

	PWM.stop("P8_36")
	PWM.cleanup()
