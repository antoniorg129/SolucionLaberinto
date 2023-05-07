#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        self.activa = False
    def activar(self):
        self.activa = True
    def desactivar(self):
        self.activa = False

    def esBomba(self):
        return True

    def entrar(self):
        if self.activa:
            print("La bomba ha explotado")
            self.activa = False
        else:
            print("La bomba esta desactivada")

    pass
