from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from clases.asignacion import asignacion
from clases.Break import Break
from clases.Continue import Continue
from clases.Return import Return
from entorno.entornos import entornos
from estructuras.errores import errores
class For_each(instruccion):
    def __init__(self,variable,arreglo,instrucciones,linea,columna):
        self.variable=variable
        self.arreglo=arreglo
        self.instrucciones=instrucciones
        self.linea=linea
        
        self.columna=columna
        self.Entorno=None
    def execute(self,Entorno):
        self.Entorno=entorno("for",Entorno)
        entornos.agregar_entorno(self.Entorno)
        self.Entorno.agregar_simbolo(self.variable, 'var', '', None, self.linea, self.columna)
        arr=self.Entorno.buscar_simbolo(self.arreglo).valor
        if isinstance(arr,list):
            for a in arr:
               self.Entorno.buscar_simbolo(self.variable).valor=a
               for instruccion in self.instrucciones:
                     ins=instruccion.execute(self.Entorno)
                     if isinstance(ins,asignacion):
                         if ins.id!=self.variable:
                             ins.execute(self.Entorno)
                         else:
                             errores.agregar_error("Error en la ejecucion del for each","No se puede asignar el valor de la variable del for each",self.linea,self.columna,"Semantico")
                   
                     elif isinstance(ins,Break):
                         return None
                     elif isinstance(ins,Continue):
                         continue
                     elif isinstance(ins,Return):
                         valor=ins.execute(self.Entorno)
                         if valor!=None:
                             return ins
                         else:
                             errores.agregar_error("Error en la ejecucion del return","Return "+self.Entorno.nombre,self.linea,self.columna,"Semantico")
                             return None  
                     else:
                         ins.execute(self.Entorno)
        else:
            errores.agregar_error("El valor "+self.arreglo+" no es de tipo lista","For each "+self.Entorno.nombre,self.linea,self.columna,"Semantico")
            return None
        
        
       