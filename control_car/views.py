# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse

# Create your views here.

from SAKS.sakshat import SAKSHAT
from SAKS.car import Car 
SAKS = SAKSHAT()
car = Car()

def index(request):
    return render(request, "control_car/index.html")

def Car_act(request, act):
    dist = -1 
    if act == '0':
        dist = car.checkdist()
        if dist < 10:
            SAKS.buzzer.beep(0.1)
            car.close()
        SAKS.digital_display.show('0000')
        SAKS.ledrow.set_row([True, True, True, True, True, True, True, True, ])
    elif act == '1':
        car.forward()
        SAKS.digital_display.show('0110')
        SAKS.ledrow.set_row([True, True, False, False, False, False, False, False, ])
    elif act == '2':
        car.right()
        SAKS.digital_display.show('0011')
        SAKS.ledrow.set_row([False, False, True, True, False, False, False, False, ])
    elif act == '3':
        car.backward()
        SAKS.digital_display.show('1001')
        SAKS.ledrow.set_row([False, False, False, False, True, True, False, False, ])
    elif act == '4':
        car.left()
        SAKS.digital_display.show('1100')
        SAKS.ledrow.set_row([False, False, False, False, False, False, True, True, ])
    elif act == '5':
        car.close()
        SAKS.digital_display.show('1111')
        SAKS.ledrow.set_row([False, False, False, False, False, False, False, False, ])

    return HttpResponse(dist)
