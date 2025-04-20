import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(17, GPIO.LOW)
GPIO.output(27,GPIO.LOW)

pwm = GPIO.PWM(18,1000)
pwm.start(0)

# GPIO.output(18, GPIO.LOW)

GPIO.output(17, GPIO.HIGH)
GPIO.output(27,GPIO.LOW)
pwm.ChangeDutyCycle(75)

time.sleep(5)
pwm.stop()
GPIO.cleanup()
