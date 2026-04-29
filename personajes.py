import random

class Personaje:
    def __init__(self, nombre, hp, atk, ki, especial, desc, imagen):
        self.nombre = nombre
        self.hp = hp
        self.hp_max = hp
        self.atk = atk
        self.ki = ki
        self.ki_max = ki
        self.especial = especial
        self.desc_esp = desc
        self.imagen = imagen
        self.items = [] # Para el sistema de inventario

    def stats(self):
        return f"{self.nombre} | HP: {self.hp}/{self.hp_max} | KI: {self.ki}/{self.ki_max}"

# Creamos los héroes originales
carlos = Personaje("Carlos Téllez", 150, 25, 60, "Corte Espectral", "Tajo dimensional masivo.", "IMG-20241015-WA0017.jpg")
haru = Personaje("Haru", 120, 30, 50, "Kunai Telequinético", "Kunai giratorio de múltiples puntas.", "Haru_antes.png")
misuzu = Personaje("Misuzu Carpo", 100, 15, 80, "Aura Azul", "Luz azulina que restaura salud.", "Misuzu.png")
# Clave y Smort se pueden añadir siguiendo este mismo formato
