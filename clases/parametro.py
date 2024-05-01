class parametro:
 def __init__(self, tipo, id, linea, columna):
        self.tipo = tipo
        self.id = id
        self.linea = linea
        self.columna = columna
 def get_tipo(self):
     return self.tipo