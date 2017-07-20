#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import os
import context
import sys

#ローカルのディレクトリ存在確認(なければ作成)
if not os.path.isdir(context.LOCAL_PATH):
    os.mkdir(context.LOCAL_PATH)

# タクトスイッチPIN番号
TACT_SWITCH = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(TACT_SWITCH, GPIO.IN)

with context.set_raw_mode():
    while True:
        if GPIO.input(TACT_SWITCH) == GPIO.HIGH:
            print "take a picture ..",
            sys.stdout.flush()
            # GPIOのスイッチON or 1入力
            context.take_picture()
            print "ok"
        else:
            pass

GPIO.cleanup()
