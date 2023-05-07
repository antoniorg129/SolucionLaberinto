#!/usr/bin/python
#-*- coding: utf-8 -*-

from Laberinto import Laberinto
from Habitacion import Habitacion
from Pared import Pared
from Puerta import Puerta
from Armario import Armario
from Norte import Norte
from Sur import Sur
from Este import Este
from Oeste import Oeste
from Bomba import Bomba

class Juego:
    def __init__(self,laberinto):
        self.bichos = []
        self.hilos = {}

        return self

    def fabricarHabitacion(self, unNum):
        hab = Habitacion(unNum)
        
        hab.ponerEn(self.fabricarNorte(), self.fabricarPared())
        hab.ponerEn(self.fabricarEste(), self.fabricarPared())
        hab.ponerEn(self.fabricarOeste(), self.fabricarPared())
        hab.ponerEn(self.fabricarSur(), self.fabricarPared())
        
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarSur())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarOeste())
        
        return hab

    def laberinto2HabitacionesFM(self):
        self.laberinto = self.fabricarLaberinto()
    
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuertaLado1(hab1, hab2)
        
        hab1.ponerEn(self.fabricarSur(), puerta)
        hab2.ponerEn(self.fabricarNorte(), puerta)
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

        def laberinto4Hab(self):
        laberinto = self.fabricarLaberinto()
        
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)
        
        
        pt12 = self.fabricarPuertaLado1(hab1, hab2)
        pt13 = self.fabricarPuertaLado1(hab1, hab3)
        pt34 = self.fabricarPuertaLado1(hab3, hab4)
        pt24 = self.fabricarPuertaLado1(hab2, hab4)
        
        
        hab1.ponerEn(self.fabricarEste(), pt12)
        hab1.ponerEn(self.fabricarSur(), pt13)
        
        hab2.ponerEn(self.fabricarOeste(), pt12)
        hab2.ponerEn(self.fabricarSur(), pt24)
        
        self.fabricarArmario(hab2)
    
        hab3.ponerElemento(self.fabricarEste(), pt34)
        hab3.ponerElemento(self.fabricarNorte(), pt13)
    
        self.fabricarArmario(hab3)
        
        hab4.ponerElemento(self.fabricarNorte(), pt24)
        hab4.ponerElemento(self.fabricarOeste(), pt34)

        for j in hab2.hijos:
            if j.esArmario():
                j.agregarHijo(self.fabricarBomba())
        
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)


    def fabricarNorte(self):
        return Norte()
    def fabricarSur(self):
        return Sur()
    def fabricarOeste(self):
        return Oeste()
    def fabricarEste(self):
        return Este()
    def fabricarPuerta(self,unaHab,otraHab):
        puerta=Puerta(unaHab,otraHab)
        return puerta

    def fabricarPared(self):
        return Pared()

    def fabricarArmarioEn(self, unCont):
        unNum = unCont.hijos.size + 1
        arm = Armario(unNum)
        arm.ponerEn(self.fabricarNorte(), self.fabricarPared())
        arm.ponerEn(self.fabricarEste(), self.fabricarPared())
        arm.ponerEn(self.fabricarOeste(), self.fabricarPared())
        arm.agregarOrientacion(self.fabricarNorte())
        arm.agregarOrientacion(self.fabricarSur())
        arm.agregarOrientacion(self.fabricarEste())
        arm.agregarOrientacion(self.fabricarOeste())
        puerta = self.fabricarPuertaLado1(arm, unCont)
        arm.ponerEn(self.fabricarSur(), puerta)
        unCont.agregarHijo(arm)

    def fabricarBomba(self):
        return Bomba()

    def obtenerHabitacion(self, unNum):
        return self.laberinto.obtenerHabitacion(unNum)



    pass
