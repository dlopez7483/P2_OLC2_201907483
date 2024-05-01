from interfaz.expresion import expresion
from entorno.simbolo import simbolo
from entorno.types import Tipo
from estructuras.errores import errores
from entorno.value import Value
class arreglo(expresion):
 def __init__(self,nombre,dimension,tipo,tipo_dato,expresiones,linea,columna):
     self.expresiones=expresiones
     self.tipo=tipo
     self.nombre=nombre
     self.dimension=dimension
     self.tipo_dato=tipo_dato
     self.linea=linea
     self.columna=columna
     self.elementos=[]
     
 
             
 def traducir(self,Entorno,gen):
     tmp=gen.new_temp()
     if self.expresiones != None:
         if isinstance(self.expresiones,list):
             if len(self.expresiones)>0:
                 
                 for exp in self.expresiones:
                     valor=exp.execute(Entorno,gen)
                     if valor!=None:
                         if self.tipo_dato==valor.type:
                    
                             self.elementos.append(valor.value)
     nameID="arr_"+str(tmp)
     gen.variable_data(nameID, 'word', ', '.join(self.elementos) )
     gen.variable_data('size_arr_'+nameID,'word',str(len(self.elementos)))           
     Entorno.agregar_simbolo(self.nombre,self.tipo,self.tipo_dato,self.elementos,nameID,self.linea, self.columna)
             
 def crear_matriz_n_dimensiones(self,expresiones,Entorno):
     for i in range(len(expresiones)):
         exp=expresiones[i]
         if isinstance(exp,list):
             self.crear_matriz_n_dimensiones(exp,Entorno)
             expresiones[i]=exp
         else:
                valor=exp.execute(Entorno)
                if valor!=None:
                    if self.tipo_dato=="NUMBER":
                        if isinstance(valor,int):
                            expresiones[i]=valor
                        else:
                            errores.agregar_error("El valor "+str(valor)+" no es de tipo numerico","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                            return None
                    elif self.tipo_dato=="FLOAT":
                            if isinstance(valor,float):
                                expresiones[i]=valor
                            elif isinstance(valor,int):
                                expresiones[i]=float(valor)
                            else:
                                errores.agregar_error("El valor "+str(valor)+" no es de tipo flotante","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                                return None
                    elif self.tipo_dato=="STRING":
                            if isinstance(valor,str):
                                expresiones[i]=valor
                            else:
                                errores.agregar_error("El valor "+str(valor)+" no es de tipo string","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                                return None
                    elif self.tipo_dato=="BOOLEAN":
                            if isinstance(valor,bool):
                                expresiones[i]=valor
                            else:
                                errores.agregar_error("El valor "+str(valor)+" no es de tipo booleano","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                                return None
                    elif self.tipo_dato=="CHAR":
                            if isinstance(valor,str):
                                if len(valor)==1:
                                 expresiones[i]=valor
                                else:
                                    errores.agregar_error("El valor "+str(valor)+" no es de tipo caracter","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                                    return None
                            else:
                                errores.agregar_error("El valor "+str(valor)+" no es de tipo caracter","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                                return None
             
 def execute(self,Entorno):
     print(self.dimension)
     if self.expresiones != None:
         if isinstance(self.expresiones,list):
             if len(self.expresiones)>0:
                 if (self.dimension==1):
                     print(len(self.expresiones))
                     for exp in self.expresiones:
                         valor=exp.execute(Entorno)
                         if valor!=None:
                             if self.tipo_dato=="NUMBER":
                                 if isinstance(valor,int):
                                     self.elementos.append(valor)
                                 else:
                                     errores.agregar_error("El valor "+str(valor)+" no es de tipo numerico","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                                     return None
                             elif self.tipo_dato=="FLOAT":
                                     if isinstance(valor,float):
                                         self.elementos.append(valor)
                                     elif isinstance(valor,int):
                                         self.elementos.append(float(valor))
                                     else:
                                         errores.agregar_error("El valor "+str(valor)+" no es de tipo flotante","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                                         return None
                             elif self.tipo_dato=="STRING":
                                     if isinstance(valor,str):
                                         self.elementos.append(valor)
                                     else:
                                         errores.agregar_error("El valor "+str(valor)+" no es de tipo string","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                                         return None
                             elif self.tipo_dato=="BOOLEAN":
                                     if isinstance(valor,bool):
                                         self.elementos.append(valor)
                                     else:
                                         errores.agregar_error("El valor "+str(valor)+" no es de tipo booleano","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                                         return None
                             elif self.tipo_dato=="CHAR":
                                     if isinstance(valor,str):
                                         if len(valor)==1:
                                             self.elementos.append(valor)
                                         else:
                                             errores.agregar_error("El valor "+str(valor)+" no es de tipo caracter","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                                             return None
                                     else:
                                         errores.agregar_error("El valor "+str(valor)+" no es de tipo caracter","Arreglo "+self.nombre,exp.linea,exp.columna,"Semantico")
                                         return None
                 elif (self.dimension>1):
                     self.crear_matriz_n_dimensiones(self.expresiones,Entorno)
                     self.elementos=self.expresiones
         elif isinstance(self.expresiones,str):
                simbolo=Entorno.buscar_simbolo(self.expresiones)
                if simbolo!=None:
                    if simbolo.tipo_dato==self.tipo_dato:
                        self.elementos=simbolo.valor
                    else:
                        errores.agregar_error("El simbolo "+self.expresiones+" no es de tipo "+self.tipo_dato,"Arreglo "+self.nombre,self.linea,self.columna,"Semantico")
                        return None
                else:
                    errores.agregar_error("El simbolo "+self.expresiones+" no existe","Arreglo "+self.nombre,self.linea,self.columna,"Semantico")
                    
     Entorno.agregar_simbolo(self.nombre,self.tipo,self.tipo_dato,self.elementos,self.linea, self.columna)