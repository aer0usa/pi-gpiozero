from gpiozero import MCP3008

pot = MCP3008(channel=0)

while True:
    print(round(pot.value * 100))
