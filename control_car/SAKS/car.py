#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

class Wheel(object):
    def __init__(self, in_pin1, in_pin2):
        self.pin1 = in_pin1
        self.pin2 = in_pin2

        gpio.setup(self.pin1, gpio.OUT)
        gpio.setup(self.pin2, gpio.OUT)

    def forward(self):
        gpio.output(self.pin1, True)
        gpio.output(self.pin2, False)

    def backward(self):
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, True)

    def stop(self):
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, False)

class HCSRO4(object):
    def __init__(self, Trig_pin, Echo_pin):
        self.Trig = Trig_pin
        self.Echo = Echo_pin

        gpio.setup(self.Trig, gpio.OUT, initial = gpio.LOW)
        gpio.setup(self.Echo, gpio.IN)

    def dist(self):
        gpio.output(self.Trig, gpio.HIGH)
        time.sleep(0.00002)
        gpio.output(self.Trig, gpio.LOW)
        while not gpio.input(self.Echo):
            pass
        t1 = time.time()
        while gpio.input(self.Echo):
            pass
        t2 = time.time()
        return (t2 - t1) * 34000 / 2
                 
class Car(object):
    def __init__(self):
        gpio.setmode(gpio.BCM)

        self.left_wheel = Wheel(23, 24)
        self.right_wheel = Wheel(27, 17)
        self.range_monit = HCSRO4(7, 22)
    
    def forward(self):
        self.left_wheel.forward()
        self.right_wheel.forward()

    def backward(self):
        self.left_wheel.backward()
        self.right_wheel.backward()

    def left(self):
        self.left_wheel.stop()
        self.right_wheel.forward()

    def right(self):
        self.left_wheel.forward()
        self.right_wheel.stop()

    def close(self):
        self.left_wheel.stop()
        self.right_wheel.stop()
    
    def checkdist(self):
        return self.range_monit.dist()
