from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from entorno.entornos import entornos

class funcion(instruccion):
    def __init__(self, id, parametros, instrucciones, tipo, linea, columna):
        self.id = id
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.Entorno = None

    def execute(self, Entorno):
      
        nuevo_entorno = entorno("funcion", Entorno)
       
        
        self.Entorno = nuevo_entorno
        entornos.agregar_entorno(self.Entorno)
        if self.parametros != None:
         for par in self.parametros:
             self.Entorno.agregar_simbolo(par.id, 'var', par.tipo, None, par.linea, par.columna)
        
        Entorno.agregar_funcion(self.id,self)
        
        return None