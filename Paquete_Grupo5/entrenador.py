from Paquete_Grupo5.persona import Persona

class Entrenador(Persona):
    """
    Clase que representa a un entrenador, hereda de Persona.
    """
    def __init__(self, persona_id, nombre, apellidos, edad, id_federacion):
        super().__init__(persona_id, nombre, apellidos, edad)
        self.id_federacion = id_federacion
        
    def dirigir_partido(self):
        """
        Método que representa que el entrenador está dirigiendo un partido.
        """
        return f"{self.nombre} está dirigiendo un partido."

    def dirigir_entrenamiento(self):
        """
        Método que representa que el entrenador está dirigiendo un entrenamiento.
        """
        print(f"{self.nombre} está dirigiendo un entrenamiento.")