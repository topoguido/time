from machine import RTC
from machine import sleep
import network
import ntptime
import gc

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Pochoclo-4G', 'laclavees1981') #replace with your WiFi ssid and password
while not wlan.isconnected():
    pass

if wlan.isconnected():
    print(f'conectado a red con IP {wlan.ipconfig("addr4")}')

rtc = RTC()
ntptime.settime()

year, month, day, weekday, hour, minutes, seconds, subsecond = rtc.datetime()

while True:
    year, month, day, weekday, hour, minutes, seconds, subsecond = rtc.datetime()
    if hour == 0:
        hour = 21
    elif hour == 1:
        hour = 22
    elif hour == 2:
        hour = 23
    elif hour == 3:
        hour = 0
    
    print(f'{day}/{month}/{year} - {hour}:{minutes}:{seconds}' )
    sleep(1000)
    gc.collect()