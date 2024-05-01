from interfaz.expresion import expresion


class atributo_declarado(expresion):
    def __init__(self,nombre,valor,linea,columna):
        self.nombre=nombre
        self.valor=valor
        self.linea=linea
        self.columna=columna
    def execute(self,Entorno):
         return self.valor.execute(Entorno)