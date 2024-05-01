from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from clases.Return import Return
from estructuras.instrucciones import salida_instrucciones
from clases.Break import Break
from clases.Continue import Continue
from clases.primitivo import primitivo
from estructuras.errores import errores
from clases.id import id
class llamado(instruccion):
 def __init__ (self,nombre,expresiones,linea,columna):
     self.nombre = nombre
     self.expresiones = expresiones
     self.linea = linea
     self.columna = columna
     self.Entorno=None
 def execute(self,Entorno):
     
     funcion=Entorno.buscar_funcion(self.nombre)
     
     if funcion!=None:
         entorno_funcion=funcion.Entorno
         if funcion.parametros!=None and self.expresiones!=None:
             if len(funcion.parametros)==len(self.expresiones):
                 i=0
                 for par in funcion.parametros:
                     valor=self.expresiones[i].execute(entorno_funcion)
                     if isinstance(valor,int) and par.tipo=="NUMBER":
                         entorno_funcion.buscar_simbolo(par.id).valor=valor
                     elif isinstance(valor,str) and par.tipo=="STRING":
                         entorno_funcion.buscar_simbolo(par.id).valor=valor
                     elif isinstance(valor,bool) and par.tipo=="BOOLEAN":
                         entorno_funcion.buscar_simbolo(par.id).valor=valor
                     elif isinstance(valor,float) and par.tipo=="FLOAT":
                         entorno_funcion.buscar_simbolo(par.id).valor=valor
                     elif isinstance(valor,str) and par.tipo=="CHAR":
                         entorno_funcion.buscar_simbolo(par.id).valor=valor
                     elif isinstance(valor,int) and par.tipo=="FLOAT":
                         entorno_funcion.buscar_simbolo(par.id).valor=float(valor)
                     elif isinstance(valor,dict):
                         entorno_funcion.buscar_simbolo(par.id).valor=valor
                     elif isinstance(valor,list):
                         entorno_funcion.buscar_simbolo(par.id).valor=valor
                     else:
                         errores.agregar_error("El valor "+par.id+" no es de tipo "+par.tipo,"Llamado "+Entorno.nombre,self.linea,self.columna,"Semantico")
                         return None
                
                        
                     i+=1
                 print("---------------------")
             else:
                 errores.agregar_error("El numero de parametros no coincide con la funcion","Llamado "+Entorno.nombre,self.linea,self.columna,"Semantico")
                 return None
         
         for inst in funcion.instrucciones:
             
             ins=inst.execute(entorno_funcion)
             
             if isinstance(ins,Break):
                 errores.agregar_error("Error en la ejecucion del break","Break",self.linea,self.columna,"Semantico")
                 return None
             elif isinstance(ins,Continue):
                 errores.agregar_error("Error en la ejecucion del continue","Continue",self.linea,self.columna,"Semantico")
                 return None
             elif isinstance(ins,Return):
                 val=ins.expresion.execute(entorno_funcion)

                 if (val!=None and funcion.tipo!=None):
                     if isinstance(val,int) and funcion.tipo=="NUMBER":
                         return val
                     elif isinstance(val,str) and funcion.tipo=="STRING":
                            return val
                     elif isinstance(val,bool) and funcion.tipo=="BOOLEAN":
                            return val
                     elif isinstance(val,float) and funcion.tipo=="FLOAT":
                            return val
                     elif isinstance(val,str) and funcion.tipo=="CHAR":
                         return val
                     elif isinstance(val,int) and funcion.tipo=="FLOAT":
                         return float(val)
                     elif isinstance(val,dict):
                         return val
                     elif isinstance(val,list):
                         return val
                     else:
                         errores.agregar_error("El valor de retorno no es de tipo "+funcion.tipo,"Return "+Entorno.nombre,self.linea,self.columna,"Semantico")
                 else:
                     errores.agregar_error("Error en la ejecucion del return","Return "+Entorno.nombre,self.linea,self.columna,"Semantico")
                     return None    
                 