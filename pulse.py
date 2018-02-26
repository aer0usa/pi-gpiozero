from gpiozero import PWMLED, Button
from signal import pause
from time import sleep

print("Here we go!")

led = PWMLED(17)
button = Button(21)

def ledPulse(howLong = 5):
    print("Pulse")
    led.pulse()
    sleep(howLong)
    led.value = 0

def ledRamp(howMany = 1):
    print("Ramp")
    sleepTime = 0.1
    for j in range(howMany):
        for i in range(10):
            led.value = i / 10
            print(i / 10)
            sleep(sleepTime)
        for i in range(10, 0, -1):
            led.value = i / 10
            print(i / 10)
            sleep(sleepTime)
    led.value = 0

button.when_pressed = ledRamp

print("Start.")
# ledPulse()
ledRamp(3)
led.value = 0
print("Done")

pause()
