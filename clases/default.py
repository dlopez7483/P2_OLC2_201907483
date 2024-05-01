from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.instrucciones import salida_instrucciones
from clases.Return import Return
from clases.Break import Break
from clases.Continue import Continue
from entorno.entornos import entornos
from estructuras.errores import errores
class default (instruccion):
 def __init__(self,instrucciones,linea,columna):
     self.instrucciones=instrucciones
     self.linea=linea
     self.columna=columna
     self.Entorno=None
 def execute(self,Entorno):
     nuevo_entorno = entorno("default",Entorno)
     self.Entorno=nuevo_entorno
     entornos.agregar_entorno(self.Entorno)
     resultado=""
     for inst in self.instrucciones:
         instruccion=inst.execute(self.Entorno)
         if isinstance(instruccion,Break):
              valor=instruccion.execute(self.Entorno)
              if valor!=None:
                  return instruccion
              else:
                  errores.agregar_error("Error en la ejecucion del break","Break "+self.Entorno.nombre,self.linea,self.columna,"Semantico")
                  return None
         elif isinstance(instruccion,Continue):
             valor=instruccion.execute(self.Entorno)
             if valor!=None:
                  return instruccion
             else:
                  errores.agregar_error("Error en la ejecucion del continue","Continue "+self.Entorno.nombre,self.linea,self.columna,"Semantico")
                  return None
         elif isinstance(instruccion,Return):
                 valor=instruccion.execute(self.Entorno)
                 if valor!=None:
                        return instruccion
                 else:
                        errores.agregar_error("Error en la ejecucion del return","Return "+self.Entorno.nombre,self.linea,self.columna,"Semantico")
                        return None
 def traducir(self,Entorno,gen):
     return None    
        
         