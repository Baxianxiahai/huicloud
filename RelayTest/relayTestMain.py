'''
Created on 2018/4/17

@author: WY
'''

#!/opt/bin/python3.6
# -*- coding: UTF-8 -*-

import datetime
import string
import sys
import time
import json
import os
import re
import socket
import ctypes 
import re
import random
import RPi.GPIO as GPIO


def func_raspy_gpio_init():
    #GPIO.setmode(GPIO.BOARD) #板子索引号
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
def func_gpio_test(pinNbr, delay):
    GPIO_PIN = pinNbr
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    #while True:
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(GPIO_PIN, GPIO.LOW)
    time.sleep(delay)
    time.sleep(delay)

#SYSTEM ENTRY
if __name__ == '__main__':
    print("[RELAY TEST] ", time.asctime(), ", Starting...\n" );
    GPIO_PWM = 17
    GPIO_RELAY1 = 27
    func_raspy_gpio_init()
    while True:
        #func_gpio_test(GPIO_PWM, 0.33)
        func_gpio_test(GPIO_RELAY1, 5)


    
    
    
    
    
    
    
    
    
    
    
    
