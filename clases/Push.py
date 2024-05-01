from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.errores import errores
class Push (instruccion):
 def __init__(self,id,expresion,linea,columna):
        self.id=id
        self.expresion=expresion
        self.linea=linea
        self.columna=columna
 def traducir(self,Entorno,gen):
        simb=Entorno.buscar_simbolo(str(self.id))
        if simb!=None and simb.tipo!="CONST":
               op=self.expresion.execute(Entorno,gen)
               if (op.type==simb.tipo_dato):
                      arreglo_tamanio=len(simb.valor)
                      tamanio=arreglo_tamanio
                     ##gen.variable_data('size_arr_'+str(simb.value),'word',str(tamanio))
                      gen.add_br()
                      gen.comment('PUSH')
                      gen.add_la('t0',simb.value)
                      gen.add_lw('t1','size_arr_'+str(simb.value))
                      gen.add_slli('t2','t1','2')
                      gen.add_operation('add','t3','t0','t2')
                      if 't' in str(op.value):
                             gen.add_move('t4',str(op.value))
                      else:
                             gen.add_li('t4',str(op.value))
                      gen.add_sw('t4','0(t3)')
                      gen.add_operation('addi','t1','t1','1')
                      
                      gen.add_la('t0','size_arr_'+str(simb.value))
                      gen.add_sw('t1','0(t0)')
                      
                     
                 
 def execute(self,Entorno):
     simbolo=Entorno.buscar_simbolo(self.id)
     valor=self.expresion.execute(Entorno)
     if simbolo!=None:
         if (isinstance(simbolo.valor,list)):
             if (simbolo.tipo_dato=='NUMBER' and isinstance(valor,int)):
                 simbolo.valor.append(valor)
             elif (simbolo.tipo_dato=='STRING' and isinstance(valor,str)):
                    simbolo.valor.append(valor)
             elif (simbolo.tipo_dato=='BOOLEAN' and isinstance(valor,bool)):
                    simbolo.valor.append(valor)
             elif (simbolo.tipo_dato=='FLOAT' and isinstance(valor,float)):
                    simbolo.valor.append(valor)
             elif (simbolo.tipo_dato=='CHAR' and isinstance(valor,str)):
                    simbolo.valor.append(valor)
             elif (simbolo.tipo_dato=='FLOAT' and isinstance(valor,int)):
                 simbolo.valor.append(float(valor))
         else:
               errores.agregar_error("El valor no es una lista","Push",self.linea,self.columna,"Semantico")
     else:
         errores.agregar_error("La variable no existe","Push",self.linea,self.columna,"Semantico")
         return None     
         
     
    