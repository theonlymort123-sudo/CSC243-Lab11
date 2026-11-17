# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:51:36 2026

@author: guestuser
"""

class ScubaTank:
    def __init__(self, label, bar):
        self.label = label
        self.__bar = bar
    def get_bar(self):
        return self.__bar
    def set_bar(self, bar):
        if 0 <= bar <= 300:
            self.__bar = bar
        else:
            print("Invalid pressure.")
    def fill(self, amount):
        if amount > 0:
            self.__bar += amount
        else:
            print("Invalid amount.")
    def release(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.__bar:
            print("Not enough air.")
        else:
            self.__bar -= amount
    def __str__(self):
        return f"Tank {self.label}: {self.__bar} bar"

def transfer_air(source, target, amount):
    pressure = source.get_bar()
    source.release(amount)
    if amount == 0 and source.get_bar == pressure - amount:
        target.fill(amount)