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
        numeroHabitaciones = 0
        for hab in self.hijos:
            if hab.esHabitacion:
                numeroHabitaciones += 1
        return numeroHabitaciones


    def agregarHabitacion(self, unaHabitacion):
        self.agregarHijo(unaHabitacion)



    pass
