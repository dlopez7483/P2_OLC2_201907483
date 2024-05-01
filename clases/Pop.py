from interfaz.instruccion import instruccion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from entorno.entorno import entorno
from estructuras.errores import errores
from entorno.value import Value

class Pop(instruccion):
 def __init__(self,id,linea,columna):
     self.id=id
    
     self.linea=linea
     self.columna=columna
 def traducir(self,Entorno,gen):
     gen.comment('Pop')
     simbolo_=Entorno.buscar_simbolo(self.id)
     gen.add_la('t0',simbolo_.value)
     simb_value_size="size_arr_"+str(simbolo_.value)
     gen.add_lw('t1',simb_value_size)
     gen.add_slli('t1','t1','2')
     gen.add_operation('add','t4','t0','t1')
     gen.add_lw('t1',simb_value_size)
     gen.add_la('t2',simbolo_.value)
     gen.add_operation('addi','t1','t1','-1')
     gen.add_la('t3',simbolo_.value)
     gen.add_sw('t1','0(t3)')
     '''
     tmp=gen.new_temp()
     gen.add_li('t3',str(tmp))
     gen.add_sw('t4','0(t3)')
     gen.add_lw('t1','0(t3)')

     gen.add_li('t2','0')
     gen.add_sw('t2','0(t4)')
     
     gen.add_lw('t2','0(t1)')
     '''
     return Value('t4',True,simbolo_.tipo_dato,[],[],[])
 def execute(self,Entorno):
        simbolo = Entorno.buscar_simbolo(self.id)
        if simbolo != None:
         if simbolo.tipo!="CONST":
             if (isinstance(simbolo.valor,list)):
                 if len(simbolo.valor)>0:
                     return simbolo.valor.pop()
                 else:
                     return "Null"
             else:
                 errores.agregar_error('Error, el simbolo no es de tipo lista',"Pop",self.linea,self.columna, 'Semantico')
         else:
                errores.agregar_error('Error, el simbolo es de tipo const',"Pop",self.linea,self.columna, 'Semantico')