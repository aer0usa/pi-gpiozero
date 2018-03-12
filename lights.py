from gpiozero import PWMLED, Button
from signal import pause
from time import sleep

led = [PWMLED(17), PWMLED(27), PWMLED(22)]
button = Button(21)

def testLeds():
    print("--------------------")
    sleepTime = 1.0
    for index, thisLed in enumerate(led):
        print("    Led ", index)
        thisLed.on()
        sleep(sleepTime)
        thisLed.off()
    print("Done\n")

button.when_pressed = testLeds

testLeds()

pause()
