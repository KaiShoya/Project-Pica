#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import os
import context

#ローカルのディレクトリ存在確認(なければ作成)
if not os.path.isdir(context.LOCAL_PATH+context.SAVE_DIRECTORY):
    os.mkdir(context.LOCAL_PATH+context.SAVE_DIRECTORY)

# タクトスイッチPIN番号
TACT_SWITCH = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(TACT_SWITCH, GPIO.IN)

try:
    while True:
        if GPIO.input(TACT_SWITCH) == GPIO.HIGH:
            context.take_picture()
            print "take a picture."
        else:
            pass
except:
    print "error."
GPIO.cleanup()
