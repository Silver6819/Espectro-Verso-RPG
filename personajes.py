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
        self.items = []  # Para el sistema de inventario
        self.forma_final = False # Atributo especial para la evolución de Smort

    def stats(self):
        return f"{self.nombre} | HP: {self.hp}/{self.hp_max} | KI: {self.ki}/{self.ki_max}"

# --- HÉROES ORIGINALES ---

# 1. Carlos Téllez - Poder Espectral
carlos = Personaje(
    "Carlos Téllez", 150, 25, 60, 
    "Corte Espectral", 
    "Tajo dimensional masivo que utiliza energía del vacío.", 
    "IMG-20241015-WA0017.jpg"
)

# 2. Haru - Ninja Médium
haru = Personaje(
    "Haru", 120, 30, 50, 
    "Kunai Telequinético", 
    "Kunai giratorio de múltiples puntas que ataca a gran velocidad.", 
    "Haru_antes.png"
)

# 3. Misuzu Carpo - Médium
misuzu = Personaje(
    "Misuzu Carpo", 100, 15, 80, 
    "Aura Azul", 
    "Luz azulina sanadora que restaura los puntos de vida.", 
    "Misuzu.png"
)

# 4. Clave - Monje Budista
clave = Personaje(
    "Clave", 140, 18, 90, 
    "Mantra de Ki", 
    "Meditación profunda que restaura la energía del equipo.", 
    "Clave_el_monje.png"
)

# 5. Ente (Smort) - Forma inicial (humana)
# Nota: Su especial es la evolución a su forma final de zorro/ente.
smort = Personaje(
    "Ente (Smort)", 110, 20, 70, 
    "Evolución Final", 
    "Transformación a su forma definitiva, duplicando su fuerza de ataque.", 
    "Ente_es_Smort_y_sus_dos_fases.png"
)

# Lista maestra para la selección en el archivo main.py
LISTA_HEROES = [carlos, haru, misuzu, clave, smort]
