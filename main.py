"""
Este módulo define clases para representar a personas, futbolistas, entrenadores y masajistas.
Cada clase contiene métodos que representan acciones específicas de estas personas.
"""

from Paquete_Grupo5 import Futbolista, Entrenador, Masajista



futbolista = Futbolista(1, "Lionel", "Messi", 35, 10, "Delantero")
entrenador = Entrenador(2, "Pep", "Guardiola", 52, "12345")
masajista = Masajista(3, "Juan", "Pérez", 40, "Fisioterapia", 15)

print(futbolista.jugar_partido())
entrenador.dirigir_entrenamiento()
print(masajista.dar_masajes())