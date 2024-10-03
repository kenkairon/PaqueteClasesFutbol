
class Persona:
    """
    Clase que representa a una persona con un ID, nombre, apellidos y edad.
    """
    def __init__(self, persona_id, nombre, apellidos, edad):
        self.persona_id = persona_id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    def concentrarse(self):
        """
        Método que representa que la persona se está concentrando.
        """
        print(f"{self.nombre} se está concentrando.")
        
    def viajar(self):
        """
        Método que representa que la persona está viajando.
        """
        print(f"{self.nombre} está viajando.")