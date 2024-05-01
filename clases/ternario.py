from interfaz.expresion import expresion
from entorno.simbolo import simbolo
from estructuras.errores import errores
class ternario(expresion):
    def __init__(self,condicion,exp1,exp2,linea,columna):
        self.condicion=condicion
        self.exp1=exp1
        self.exp2=exp2
        self.linea=linea
        self.columna=columna
    def execute(self,entorno):
        condicion = self.condicion.execute(entorno)
        if condicion!=None:
            if (isinstance(condicion,bool)):
                if condicion:
                    return self.exp1.execute(entorno)
                else:
                    return self.exp2.execute(entorno)
            else:
                errores.agregar_error('La condicion no es booleana','Ternario',self.linea,self.columna,'Semantico')
                return None
        else:
            return None
    def traducir(self,entorno,gen):
     return None