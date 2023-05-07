#!/usr/bin/python
#-*- coding: utf-8 -*-


from ElementoMapa import ElementoMapa

class Contenedor(Decorator):
    def __init__(self):
        self.activa = False
    
    def agregarHijo(self, unEm):
        unEm.padre = self
        self.hijos.append(unEm)

    def agregarOrientacion(self, unaOr):
        self.orientaciones.append(unaOr)

    def ponerElemento(self, unaOr, unEm):
        unaOr.ponerElemento(unEm, self)

    pass
