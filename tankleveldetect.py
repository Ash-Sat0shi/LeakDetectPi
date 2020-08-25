#!/usr/bin python3
# -*- coding: utf-8 -*-
# before use, do
# sudo apt-get -y install python3-dev
# sudo apt-get -y install python3-pip

import RPi.GPIO as GPIO
import time

# for send Gmail
import smtplib
import netifaces as ni
from email.utils import formatdate
# for Japanese content
from email.mime.text import MIMEText

ni.ifaddresses('eth0')
myip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

	# Gmail Account Settings
gmail_addr = "leakdetectpi@gmail.com"
gmail_pass = "shinshuleak"
SMTP = "smtp.gmail.com"
PORT = 587
		
	# Sending mail

from_addr = gmail_addr				# sender addr
to_addr = "satoshi.yatabe@shin-shu.co.jp"
subject = "水位上昇検知システム　LeakDetectPi-PROTOTYPE"
body = "水位上昇を検知しました！！ \n RasPi IP Address is : {0}".format(myip)

msg = MIMEText(body, "plain", "utf-8")
        # prevent 'ascii' codec can't encode characters in position 0-14: ordinal not in range(128) というエラーがでる
msg["From"] = from_addr
msg["To"] = to_addr
msg["Date"] = formatdate()
msg["Subject"] = subject

# -- main --

PIN_IN = 21
PIN_OUT = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_OUT, GPIO.OUT)

try:
    while True:
        flag = GPIO.input(PIN_IN) == GPIO.HIGH
        GPIO.output(PIN_OUT, flag)
        if flag == True:
            print(flag)
            print(myip)
    # -------------------------------------------------------------------------------------------------------------
	# send mail
            try:
                print("sending mail...")
                #send = smtplib.SMTP(SMTP, PORT)		# create SMTP object
                #send.ehlo()
                #send.starttls()
                #send.ehlo()
                #send.login(gmail_addr, gmail_pass)	# Login to Gmail
                #send.send_message(msg)
                #send.close()
            except Exception as e:
                print("except: " + str(e))		# in case of error
            else:
                print("Successfully sent mail to {0}".format(to_addr))	# when succeed
            time.sleep(30)
     # -------------------------------------------------------------------------------------------------------------
        
        else:
            print("FALSE")
            time.sleep(3)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

# -- main end --





