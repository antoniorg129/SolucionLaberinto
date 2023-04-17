#!/usr/bin/python
#-*- coding: utf-8 -*-

class Juego:
    def __init__(self,laberinto):
        self.bichos = []
        self.laberinto=laberinto
        self.hilos = {}

        return self

    def fabricarHabitacion(self, unNum):
        hab = Habitacion()
        hab.num = unNum
        
        #hab.ponerEn(self.fabricarNorte(), self.fabricarPared())
        #hab.ponerEn(self.fabricarEste(), self.fabricarPared())
        #hab.ponerEn(self.fabricarOeste(), self.fabricarPared())
        #hab.ponerEn(self.fabricarSur(), self.fabricarPared())
        #
        #hab.agregarOrientacion(self.fabricarNorte())
        #hab.agregarOrientacion(self.fabricarSur())
        #hab.agregarOrientacion(self.fabricarEste())
        #hab.agregarOrientacion(self.fabricarOeste())
        
        return hab

    def fabricarNorte(self):
        return Norte()
    def fabricarSur(self):
        return Sur()
    def fabricarOeste(self):
        return Oeste()
    def fabricarEste(self):
        return Este()
    def fabricarPuerta(self,unaHab,otraHab):
        puerta=Puerta()
        puerta.lado1=unaHab
        puerta.lado2=otraHab
        return puerta


    pass
