#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):
    def __init__(self):
        
    def esHabitacion(self):
        return True

    def entrar(self):
        print("Estas en la habitacion", self.num)


    pass
