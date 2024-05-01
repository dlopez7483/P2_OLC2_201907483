from abc import ABC, abstractmethod


class instruccion(ABC):
 @abstractmethod
 def execute(self,entorno):
     pass
 def traducir(self,entorno,gen):
     pass