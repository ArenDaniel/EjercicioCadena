#!/usr/bin/env python
# -*- coding: utf-8 -*-

from creacionales.abstract_factory.ejemplo_abstract_factory import EjemploAbstractFactory
from creacionales.singleton.ejemplo_singleton import EjemploSingleton
from creacionales.prototype.ejemplo_prototype import EjemploPrototype
from estructurales.adapter.ejemplo_adapter import EjemploAdapter
from estructurales.bridge.ejemplo_bridge import EjemploBridge
from estructurales.Composite.ejemplo_composite import EjemploComposite
from estructurales.decorator.ejemplo_decorator import EjemploDecorator
from estructurales.proxy.ejemplo_proxy import EjemploProxy
from estructurales.fachada.ejemplo_fachada import EjemploFachada
from estructurales.flyweight.ejemplo_flyweight import EjemploFlyweight
from comportamiento.chain_of_resposability.ejemplo_cadena import EjemploCadena
from comportamiento.command.ejemplo_command import EjemploCommand
from comportamiento.interpreter.ejemplo_interpreter import EjemploInterpreter
from abc import ABC,abstractmethod

class Manejador():
    def __init__(self):
        self.sucesor = None
    def DefinirSucesor(self, sucesor):
        self.sucesor = sucesor
    def Manejador_Request(self, opt):
        pass

class ManejadorUno(Manejador):

    def Manejador_Request(self,opt):
        if opt == 1:
            EjemploSingleton().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorDos(Manejador):

    def Manejador_Request(self,opt):
        if opt == 2:
            EjemploAbstractFactory().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorTres(Manejador):

    def Manejador_Request(self,opt):
        if opt == 3 :
            EjemploPrototype().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorCuatro(Manejador):

    def Manejador_Request(self,opt):
        if opt == 4:
            EjemploAdapter().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorCinco(Manejador):

    def Manejador_Request(self,opt):
        if opt == 5:
            EjemploDecorator().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorSeis(Manejador):

    def Manejador_Request(self,opt):
        if opt == 6:
            EjemploProxy().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorSiete(Manejador):

    def Manejador_Request(self,opt):
        if opt == 7:
            EjemploBridge().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorOcho(Manejador):

    def Manejador_Request(self,opt):
        if opt == 8:
            EjemploComposite().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorNueve(Manejador):

    def Manejador_Request(self,opt):
        if opt == 9:
            EjemploDecorator().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorDiez(Manejador):

    def Manejador_Request(self,opt):
        if opt == 10:
            EjemploProxy().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorOnce(Manejador):

    def Manejador_Request(self,opt):
        if opt == 11:
            EjemploFachada().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorDoce(Manejador):

    def Manejador_Request(self,opt):
        if opt == 12:
            EjemploFlyweight().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
class ManejadorTrece(Manejador):

    def Manejador_Request(self,opt):
        if opt == 13:
            EjemploCommand().operacion()
        else:
            self.sucesor.Manejador_Request(opt)            
class ManejadorCatroce(Manejador):

    def Manejador_Request(self,opt):
        if opt == 14:
            EjemploInterpreter().operacion()
        else:
            self.sucesor.Manejador_Request(opt)
if __name__ == '__main__':
    opciones = [ManejadorUno(), ManejadorDos(),ManejadorTres(),ManejadorCuatro(),ManejadorCinco(), ManejadorSeis(),
                ManejadorSiete(), ManejadorOcho(), ManejadorNueve(),ManejadorDiez(),ManejadorOnce(),ManejadorDoce(),
                ManejadorTrece(),ManejadorCatroce()]
    for i in range(len(opciones)-1):
            opciones[i].DefinirSucesor(opciones[i+1])
    op =int(input("Seleccione: "))
    opciones[0].Manejador_Request(op)
