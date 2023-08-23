#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self._name = name
        self._breed = breed

    def bark(self):
        print('Woof!')
    
    def sit(self):
        print("The dog is sitting.")