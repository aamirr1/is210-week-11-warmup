#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Warp-up task 4"""

import car


class CustomCar(car.Car):
    """This is a new class called CustomCar """

    def __init__(self, color='red', tires=None):
    
        car.Car.__init__(self, color)
        if tires is None:
            self.tires = []
            list_tires = ['a', 'b', 'c', 'd']
            for each in list_tires:
                each = CustomTire()
                self.tires.append(each)
        else:
            self.tires = tires


class CustomTire(car.Tire):
    """This is a class called CistomTire"""

    def __init__(self, miles=0):
    
        car.Tire.__init__(self, miles)
        self.__maximum_miles = 500
