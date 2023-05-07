#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self,lado1,lado2):
        self.abierta= false
        self.lado1 = lado1
        self.lado2 = lado2

    def esPuerta(self):
        return True

    def estaCerrada(self):
        return not self.abierta

    def abrir(self):
        self.abierta=True

