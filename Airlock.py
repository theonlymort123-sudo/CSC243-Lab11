# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:34:06 2026

@author: guestuser
"""

class Airlock:
    def __init__(self, code, sealed):
        self.code = code
        self.__sealed = sealed
    def is_sealed(self):
        return self.__sealed
    def __lock_bolts(self):
        print("Bolts locked.")
    def __unlock_bolts(self):
        print("Bolts unlocked")
    def seal(self):
        if self.__sealed:
            print("Already sealed.")
        else:
            self.__lock_bolts()
            self.__sealed = True
            print("Airlock sealed")
    def unseal(self):
        if not self.__sealed:
            print("Already open.")
        else:
            self.__unlock_bolts()
            self.__sealed = False
            print("Airlock open.")
    def __str__(self):
        if self.__sealed:
            return f"Airlock {self.code}: sealed"
        else:
            return f"Airlock {self.code}: open"