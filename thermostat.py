from gpiozero import LED, MCP3008
from time import sleep

adc = MCP3008(channel=1)
pot = MCP3008(channel=0)
led = LED(21)
currentTemp = 80.0
thermostat_setting = 80.0

def convert_temp(gen):
    for value in gen:
        yield (value * 3.3 - 0.5) * 100

def immediate_temp(rawVal):
    return (rawVal * 3.3 - 0.5) * 100

def immediate_fahrenheit():
    return round(fahrenheit(immediate_temp(adc.value)), 1)

def thermostat_setting():
    return round(thermostat_value(pot.value), 1)

# Set thermostat from 50 to 90 degrees
def thermostat_value(rawVal):
    return ((rawVal * 40) + 50)

def fahrenheit(celcius=22):
    return (celcius * (9/5) + 32)

def activate(state=False):
    if (state):
        led.on()
    else:
        led.off()

# while True:
#     currentTemp = round(fahrenheit(immediate_temp(adc.value)), 1)
#     thermostat_setting = round(thermostat_value(pot.value), 1)
#     print('Temp ', currentTemp, ' / ', thermostat_setting, ' F')
#     activate(currentTemp < thermostat_setting)
#     sleep(1)
