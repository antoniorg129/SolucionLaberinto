#!/usr/bin/python
#-*- coding: utf-8 -*-


class Bicho():
    def __init__(self):
        self.vidas = 50 
        self.poder = 1
        self.modo = None

    def esAgresivo(self):
        return self.modo.esAgresivo
    
    def esPerezoso(self):
        return self.modo.esPerezoso

    def estaVivo(self):
        return self.vidas > 0