from gpiozero import MCP3008
from time import sleep

def convert_temp(gen):
    for value in gen:
        yield (value * 3.3 - 0.5) * 100

adc = MCP3008(channel=1)

for temp in convert_temp(adc.values):
    fahrenheit = temp * (9/5) + 32
    print('The temperature is', round(temp, 1), 'C, ', round(fahrenheit, 1), 'F')
    sleep(1)
