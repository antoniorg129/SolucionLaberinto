#!/usr/bin/python
#-*- coding: utf-8 -*-

class ElementoMapa:
    def __init__(self):
        self.padre=None
        pass

    #def entrar(self):
    #    pass

    def esArmario(self):
        return False
    
    def esBomba(self):
        return False
    
    def esHabitacion(self):
        return False
    
    def esPared(self):
        return False
    
    def esPuerta(self):
        return False
