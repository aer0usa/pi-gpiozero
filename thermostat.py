from gpiozero import LED, MCP3008
from time import sleep

def convert_temp(gen):
    for value in gen:
        yield (value * 3.3 - 0.5) * 100

def fahrenheit(celcius=22):
    return (celcius * (9/5) + 32)

def activate(state=False):
    if (state):
        led.on()
    else:
        led.off()

adc = MCP3008(channel=1)
led = LED(21)
target = 80.0

for temp in convert_temp(adc.values):
    print('The temperature is', round(temp, 1), 'C, ', round(fahrenheit(temp), 1), 'F')
    activate(fahrenheit(temp) < target)
    sleep(1)
