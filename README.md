# LeakDetectPi
let Raspberry Pi watch variable sensors to detect water leakage, power loss and toilet tank waterlevel. Alarm if they went wrong with LED and e-mailing.

place detect.py in your RaspberryPi somewhere you want and place detect.service at /etc/systemd/system/ and let systemd do the 'watchdog'
* you need to modify detect.service if you place detect.py anywhere else from home/pi/

GPIO 21,23,24 is for sensors (connect another end to 3.3v pin, shortage of the circuit means detection)
GPIO 25 and any Ground pin for detection LED. 

