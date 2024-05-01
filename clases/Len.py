from interfaz.expresion import expresion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from estructuras.errores import errores
from entorno.value import Value
class Len (expresion):
 def __init__(self,id,linea,columna):
        self.id=id
        self.linea=linea
        self.columna=columna
 def traducir(self,entorno,gen):
        gen.comment('Len')
        simbolo_=entorno.buscar_simbolo(self.id)
        if simbolo_==None:
               errores.append(nodo_error(self.linea,self.columna,'Semantico','No existe el arreglo '+self.id))
               return None
        simb_value_size="size_arr_"+str(simbolo_.value)
        gen.add_la('t0',simb_value_size)
        return Value('t0',True,'NUMBER',[],[],[])
 def execute(self,entorno):
        simb=entorno.buscar_simbolo(self.expresion)
        print(self.expresion)
        if simb!=None:
            if (isinstance(simb.valor,list)):
                return len(simb.valor)
            else:
                errores.agregar_error("El valor no es de tipo lista","Len "+entorno.nombre,self.linea,self.columna,"Semantico")
                return None
        else:
            errores.agregar_error("El valor no existe","Len "+entorno.nombre,self.linea,self.columna,"Semantico")
            return None
        
        
        
        