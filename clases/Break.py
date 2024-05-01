from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from estructuras.errores import errores

class Break(instruccion):
    def __init__(self,linea,columna):
        self.linea=linea
        self.columna=columna
    def execute(self,Entorno):
     if (Entorno.encontrar_entorno("while")==None and Entorno.encontrar_entorno("for")==None):
         errores.agregar_error("Break fuera de ciclo","Break",self.linea,self.columna,"Semantico")
         return None
     else:
         return self