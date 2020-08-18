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

from_addr = gmail_addr	# sender addr
to_addr = "satoshi.yatabe@shin-shu.co.jp"
subject1 = "漏水検知システム　DetectPi-PROTOTYPE"
subject2 = "停電検知システム　DetectPi-PROTOTYPE"
body1 = "漏水を検知しました！！ \n RasPi IP Address is : {0} \n ※電源を入れた初回のメールはテストメールです。".format(myip)
body2 = "停電を検知しました！！ \n RasPi IP Address is : {0} \n ※電源を入れた初回のメールはテストメールです。".format(myip)


msg = MIMEText(body1, "plain", "utf-8")
        # prevent 'ascii' codec can't encode characters in position 0-14: ordinal not in range(128) というエラーがでる
msg["From"] = from_addr
msg["To"] = to_addr
msg["Date"] = formatdate()
msg["Subject"] = subject1


# -- main --

PIN_IN1 = 24
PIN_IN2 = 23
PIN_OUT = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_IN2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_OUT, GPIO.OUT)

try:
    while True:
        flag1 = GPIO.input(PIN_IN1) == GPIO.HIGH
        GPIO.output(PIN_OUT, flag1)
        if flag1 == True:
            print("WATER DETECTED!! 漏水を検知しました！！")
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
                print("Successfully sent  WATER LEAKAGE mail to {0}".format(to_addr))	# when succeed
            time.sleep(3)
     # -------------------------------------------------------------------------------------------------------------
        
        else:
            print("NO WATER LEAKAGE")
            
            msg = MIMEText(body2, "plain", "utf-8")
            msg["Subject"] = subject2
            flag2 = GPIO.input(PIN_IN2) == GPIO.HIGH
            GPIO.output(PIN_OUT, flag2)
            if flag2 == True:
                print(" BLACKOUT DETECTED!! 停電を検知しました！！")
                # -------------------------------------------------------------------------------------------------------------
                # send mail
                try:
                    print("sending BLACKOUT mail...")
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
                    time.sleep(3)
                # -------------------------------------------------------------------------------------------------------------

            print("NO BLACKOUT")
            time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

# -- main end --
