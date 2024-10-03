from Paquete_Grupo5.persona import Persona

class Futbolista(Persona):
    """
    Clase que representa a un futbolista, hereda de Persona.
    """
    def __init__(self, persona_id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(persona_id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion
        
    def jugar_partido(self):
        """
        Método que representa que el futbolista está jugando un partido.
        """
        return f"{self.nombre} está jugando un partido en la demarcación de {self.demarcacion}."
   
    def entrenar(self):
        """
        Método que representa que el futbolista está entrenando.
        """
        print(f"{self.nombre} está entrenando.")