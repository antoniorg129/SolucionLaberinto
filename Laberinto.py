#!/usr/bin/python
#-*- coding: utf-8 -*-

from Juego import Juego

class Laberinto(Juego):
    def obtenerHabitacion(self, unNum):
    for each in self.hijos:
        if each.esHabitacion and each.num == unNum:
            return each
    return None

    def numeroHabitaciones(self):
        hab = [each for each in self.hijos if each.esHabitacion]
        return len(hab)

    def agregarHabitacion(self, unaHabitacion):
        self.agregarHijo(unaHabitacion)



    pass
