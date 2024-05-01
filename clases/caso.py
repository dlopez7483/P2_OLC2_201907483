from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from estructuras.instrucciones import salida_instrucciones
from entorno.entornos import entornos
from clases.Break import Break
class caso(instruccion):
 def __init__(self,expresion,instrucciones,linea,columna):
     self.expresion=expresion
     self.instrucciones=instrucciones
     self.linea=linea
     self.columna=columna
     self.Entorno=None
 def traducir(self,Entorno,gen):
     gen.comment('Inicio caso')
     for ins in self.instrucciones:
         i=ins.execute(Entorno,gen)
 def execute(self,Entorno):
     nuevo_entorno = entorno("caso",Entorno)
     self.Entorno=nuevo_entorno
     entornos.agregar_entorno(self.Entorno)
     resultado=""
     for instruccion in self.instrucciones:
         instruccion.execute(self.Entorno)