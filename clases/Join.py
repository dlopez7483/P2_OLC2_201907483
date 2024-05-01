from interfaz.expresion import expresion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from estructuras.errores import errores


class Join(expresion):
 def __init__(self,id,linea,columna):
     self.id=id
     self.linea=linea
     self.columna=columna
 def execute(self,Entorno):
     simb=Entorno.buscar_simbolo(self.id)
     if simb!=None:
         if (isinstance(simb.valor,list)):
             elementos=simb.valor
             for i in range(len(elementos)):
                 elementos[i]=str(elementos[i])
             return ",".join(elementos)
         else:
                errores.agregar_error("El valor "+self.id+" no es de tipo lista","Join "+Entorno.nombre,self.linea,self.columna,"Semantico")
                return None
     else:
            errores.agregar_error("El valor "+self.id+" no existe","Join "+Entorno.nombre,self.linea,self.columna,"Semantico")
            return None
     
    
     