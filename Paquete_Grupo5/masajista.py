from Paquete_Grupo5.persona import Persona

class Masajista(Persona):
    """
    Clase que representa a un masajista, hereda de Persona.
    """
    def __init__(self, persona_id, nombre, apellidos, edad, titulacion, anos_experiencia):
        super().__init__(persona_id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.anos_experiencia = anos_experiencia
        
    def dar_masajes(self):
        """
        Método que representa que el masajista está dando masajes.
        """
        return f"{self.nombre} está dando masajes."