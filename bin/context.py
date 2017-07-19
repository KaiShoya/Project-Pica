#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 画像保存パス
LOCAL_PATH="/home/pi/Picture/"
REMOTE_PATH="foo"
# 拡張子
EXTENSION=".jpg"

import os
import time
import picamera
import RPi.GPIO as GPIO

# TODO:sdカード拡張時用にpathの取得を関数化 USBメモリも対応する
def get_path():
    return LOCAL_PATH

# TODO: 10000枚を超えた場合の対応が必要
# できればもう一つ階層を増やしたい
def get_photoname():
    filelist = os.listdir(get_path())
    if len(filelist) < 1:
        return "0000"+EXTENSION
    else:
        num = '{0:04d}'.format(int((sorted(filelist,reverse=True)[0].split("."))[0]) + 1)
        return get_path()+num+EXTENSION

def take_picture():
    with picamera.PiCamera() as camera:
        # 解像度 最大(2592,1944)
        camera.resolution = (1024, 768)
        camera.start_preview()
        # # カメラ初期化
        # time.sleep(2) # TODO:sleepは必要か？
        #撮影
        camera.capture(get_photoname())


# def take_movie():
#     with picamera.PiCamera() as camera:
#         # #fps(フレームレート)
#         # camera.framerate = 10
#         #LED On
#         camera.led = True
#         #解像度
#         camera.resolution = RESOLUTION
#         # 動画撮影(5秒)
#         camera.start_recording('video.h264')
#         sleep(5)
#         camera.stop_recording()
#         camera.led = False
