#!/usr/bin/python
#-*- coding: utf-8 -*-

from Juego import Juego

if __name__ == "__main__":
    juego = Juego()
    juego.laberinto4Hab()
    for i in range(0, juego.numeroHabitaciones()):
        aux = juego.obtenerHabitacion(i)
        print("Habitacion ", i)

    habitacion2 = juego.obtenerHabitacion(1)
    print("\n Habitación numero 2")
    for aux in habitacion2.hijos:
        for j in aux.hijos:
            print("¿Contiene una bomba?", j.esBomba())

    print("La bomba esta en la habitación 2")
    habitacion2 = juego.obtenerHabitacion(1)
    for aux in habitacion2.hijos:
        for j in aux.hijos:
                if j.esBomba():
                    j.activar()
                    print("Bomba activada")
                j.entrar()
    for aux in habitacion2.hijos:
        for j in aux.hijos:
                if j.esBomba():
                    j.desactivar()
                    print("Bomba desactivada")
                j.entrar()
