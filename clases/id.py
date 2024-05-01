from interfaz.expresion import expresion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from estructuras.errores import errores
from entorno.value import Value
class id(expresion):
 def __init__(self,id,linea,columna):
     self.id=id
     self.linea=linea
     self.columna=columna
 def traducir(self,Entorno,gen):
     temp=gen.new_temp()
     simbolo_=Entorno.buscar_simbolo(self.id)
     if simbolo_!=None:
         if simbolo_.tipo_dato=="NUMBER":
             gen.comment('agregando ID')
             gen.add_br()
             gen.add_la('t0', str(self.id))
             gen.add_lw('t0', '0(t0)')
             gen.add_li('t3', str(temp))
             gen.add_sw('t0', '0(t3)')
             return Value(str(temp), True, "NUMBER", [], [], [])
         elif simbolo_.tipo_dato=="STRING":
                gen.add_br()
                return Value(str(self.id), False, "STRING", [], [], [])
         elif simbolo_.tipo_dato=="BOOLEAN":
             gen.comment('agregando ID')
             gen.add_br()
             gen.add_la('t0', str(self.id))
             gen.add_lw('t0', '0(t0)')
             gen.add_li('t3', str(temp))
             gen.add_sw('t0', '0(t3)')
             return Value(str(temp), True, "BOOLEAN", [], [], [])
         elif simbolo_.tipo_dato=="CHAR":
              gen.add_br()
              gen.add_la('t0', str(self.id))
              gen.add_li('t3', str(temp))
              gen.add_sw('t0', '0(t3)')
              return Value(str(temp), True, "CHAR", [], [], [])
 def execute(self,Entorno):
     
     simbolo = Entorno.buscar_simbolo(self.id)
     if simbolo != None and simbolo.valor!=None:
         print("id",self.id)
         print("simbolo",simbolo.valor)
         return simbolo.valor
     else:
         print("Su id no existe")
         errores.agregar_error("El valor "+self.id+" no existe","id "+Entorno.nombre,self.linea,self.columna,"Semantico")
         return None
               