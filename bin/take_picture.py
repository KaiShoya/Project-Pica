#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import os
import context
import sys

#ローカルのディレクトリ存在確認(なければ作成)
if not os.path.isdir(context.LOCAL_PATH+context.SAVE_DIRECTORY):
    os.mkdir(context.LOCAL_PATH+context.SAVE_DIRECTORY)

# タクトスイッチPIN番号
TACT_SWITCH = 14
LED = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(TACT_SWITCH, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        if GPIO.input(TACT_SWITCH) == GPIO.HIGH:
            # タクトスイッチON
            GPIO.output(LED, GPIO.LOW)
            print "take a picture ..",
            sys.stdout.flush()
            context.take_picture()
            print "ok"
        else:
            pass
except:
    print sys.exc_info()
finally:
    GPIO.cleanup()
