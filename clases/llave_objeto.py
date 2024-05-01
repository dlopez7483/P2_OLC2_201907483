from interfaz.expresion import expresion
from estructuras.errores import errores
class llave_objeto(expresion):
 def __init__(self, id, atributo,linea, columna):
     self.id = id
     self.atributo = atributo
     self.linea = linea
     self.columna = columna
 def traducir(self, Entorno):
     return None
 def execute(self, Entorno):
     simbolo = Entorno.buscar_simbolo(self.id)
     if simbolo != None:
         if len(self.atributo)==1:
             if self.atributo[0] in simbolo.valor:
                 return simbolo.valor[self.atributo[0]]
             else:
                 errores.agregar_error("El atributo no existe en el objeto","Llave_Objeto "+Entorno.nombre,self.linea,self.columna,"Semantico")
                 return None
         elif len(self.atributo)>1:
                if self.atributo[0] in simbolo.valor:
                    obj=simbolo.valor[self.atributo[0]]
                    if obj==None:
                     return None
                    for a in self.atributo[1:]:
                        if a in obj:
                            obj=obj[a]
                        else:
                            errores.agregar_error("El atributo no existe en el objeto","Llave_Objeto "+Entorno.nombre,self.linea,self.columna,"Semantico")
                            return None
                    return obj
                else:
                    errores.agregar_error("El atributo no existe en el objeto","Llave_Objeto "+Entorno.nombre,self.linea,self.columna,"Semantico")
                    return None
     else:   
            errores.agregar_error("El objeto no existe o no es un objeto","Llave_Objeto "+Entorno.nombre,self.linea,self.columna,"Semantico")
            return None