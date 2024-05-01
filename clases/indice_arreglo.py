from interfaz.expresion import expresion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from estructuras.errores import errores
from entorno.value import Value
class indice_arreglo(expresion):
 def __init__(self,id,expresion,linea,columna):
     self.id=id
     self.expresion=expresion
     self.incrementador=0
     self.linea=linea
     self.columna=columna 
     
 def traducir(self,entorno,gen):
     simbolo_=entorno.buscar_simbolo(str(self.id))
     if simbolo_!=None:
         
         index=self.expresion[0][0].execute(entorno,gen)
         if index.type!="NUMBER":
                errores.append(nodo_error(self.linea,self.columna,'Semantico','El indice del arreglo debe ser de tipo NUMBER'))
                return None
         gen.add_br()
         gen.comment('Acceso a un arreglo')
         if 't' in str(index.value):
             gen.add_move('t3', str(index.value))
         else:
             gen.add_li('t3', str(index.value))
         gen.add_lw('t1', '0(t3)')
         gen.add_move('t0', 't1')
         gen.add_slli('t0', 't0', '2')
         gen.add_la('t1',simbolo_.value)

         gen.add_lw('t1', '0(t1)')

         gen.add_operation('add', 't2', 't1', 't0')
         return Value('t2', True, simbolo_.tipo_dato, [], [], [])
         
     else:
         print('No se encontro el simbolo')
         return None
 def retornar_valor_arreglo(self,entorno,simbolo,indice,tamanio_llamado):
     if (self.incrementador<tamanio_llamado-1 and isinstance(simbolo,list)):
         self.incrementador+=1
         nuevo_arreglo=simbolo[indice]
         return self.retornar_valor_arreglo(entorno,nuevo_arreglo,self.expresion[self.incrementador][0].execute(entorno),tamanio_llamado)
     elif (self.incrementador==tamanio_llamado-1):
         if (indice>=0 and indice<len(simbolo)):
             return simbolo[indice]
     
 def execute(self,entorno):
     if self.expresion!=None:
         simbolo=entorno.buscar_simbolo(self.id)
         
         if simbolo!=None:
             if len(self.expresion)==1:
                 valor=self.expresion[0][0].execute(entorno)
                 if (isinstance(valor,int)):
                     if valor>=0 and valor<len(simbolo.valor):
                         return simbolo.valor[valor]
                     else:
                         errores.agregar_error("El indice "+str(valor)+" esta fuera de rango","Indice "+entorno.nombre,self.linea,self.columna,"Semantico")
                 else:
                     errores.agregar_error("El valor no es de tipo entero","Indice "+entorno.nombre,self.linea,self.columna,"Semantico")
             elif len(self.expresion)>1:
                 try:
                      return self.retornar_valor_arreglo(entorno,simbolo.valor,self.expresion[self.incrementador][0].execute(entorno),len(self.expresion))
                 except:
                     errores.agregar_error("El indice esta fuera de rango","Indice "+entorno.nombre,self.linea,self.columna,"Semantico")
                     return None
                 
         else:
             errores.agregar_error("El valor "+self.id+" no existe","Indice "+entorno.nombre,self.linea,self.columna,"Semantico")
             return None
         
                 