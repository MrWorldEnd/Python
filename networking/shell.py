import os
interface = "wlan0"

x = os.popen("ifconfig " + interface).read()

print(x)

