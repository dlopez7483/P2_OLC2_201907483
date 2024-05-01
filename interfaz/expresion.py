from abc import ABC, abstractmethod

class expresion(ABC):
 @abstractmethod
 def execute(self, entorno):
     pass 
 def traducir(self,entorno,gen):
     pass