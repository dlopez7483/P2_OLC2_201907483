from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from estructuras.errores import errores
class Continue(instruccion):
    def __init__(self,linea,columna):
        self.linea=linea
        self.columna=columna
    def execute(self,Entorno):
        if (Entorno.encontrar_entorno("while")==None and Entorno.encontrar_entorno("for")==None):
            errores.agregar_error("No se puede usar continue fuera de un ciclo","Continue",self.linea,self.columna,"Semantico")
            return None
        return self