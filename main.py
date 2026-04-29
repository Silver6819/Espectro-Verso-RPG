import random
import time
import sys
from personajes import LISTA_HEROES
from enemigos import BASE_DE_DATOS_ENEMIGOS

# --- FUNCIÓN DE NARRACIÓN ESTILO NOVELA ---
def narrar(texto):
    print("\n[HISTORIA]: ", end="")
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(0.02) # Velocidad de lectura
    print("\n")

# --- MOTOR DE COMBATE MEJORADO ---
def iniciar_combate(jugador, enemigo_data):
    e_nombre = enemigo_data["nombre"]
    e_hp = enemigo_data["hp"]
    e_atk = enemigo_data["atk"]
    e_desc = enemigo_data["desc"]
    
    narrar(f"El aire se vuelve pesado... {e_desc}")
    print(f"--- ¡PELIGRO! Aparece {e_nombre} ---")
    
    while jugador.hp > 0 and e_hp > 0:
        print(f"\n{jugador.stats()}")
        print(f"{e_nombre} | HP: {e_hp}")
        print("-" * 30)
        print("1. Atacar (Básico) | 2. ESPECIAL (20 KI) | 3. Inventario")
        
        opc = input("Selecciona tu acción: ")
        
        if opc == "1":
            danio = jugador.atk + random.randint(0, 5)
            e_hp -= danio
            print(f"¡{jugador.nombre} conecta un golpe certero! Causa {danio} de daño.")
        
        elif opc == "2":
            if jugador.ki >= 20:
                jugador.ki -= 20
                danio = jugador.atk * 3
                print(f"¡{jugador.especial.upper()}!")
                print(f"-> {jugador.desc_esp}")
                e_hp -= danio
            else:
                print("¡No tienes suficiente KI para el especial!")
        
        elif opc == "3":
            print("El inventario está vacío por ahora...")
            continue # No gasta turno

        # Turno del enemigo
        if e_hp > 0:
            d_e = e_atk + random.randint(-3, 3)
            jugador.hp -= d_e
            print(f"El {e_nombre} contraataca violentamente y te quita {d_e} HP.")

    if jugador.hp > 0:
        print(f"\n¡Has vencido al {e_nombre}!")
        narrar("El portal blanco brilla a lo lejos... una nueva aventura aguarda.")
    else:
        print("\nHas caído en batalla...")
        narrar("Tu alma regresa al flujo del Espectro-verso para intentarlo una vez más.")

# --- INICIO DEL JUEGO ---
if __name__ == "__main__":
    narrar("Bienvenido al Espectro-Verso RPG, Silver Breaker.")
    narrar("Una batalla se encontraba realizando en un mundo de magia y hechicería...")
    
    print("\n--- SELECCIONA TU HÉROE ---")
    for i, heroe in enumerate(LISTA_HEROES):
        print(f"{i+1}. {heroe.nombre} ({heroe.especial})")
    
    try:
        eleccion = int(input("\nElige el número de tu héroe: ")) - 1
        mi_heroe = LISTA_HEROES[eleccion]
        
        narrar(f"Has elegido a {mi_heroe.nombre}. El destino del multiverso está en tus manos.")
        
        # Encuentro aleatorio
        enemigo_al_azar = random.choice(BASE_DE_DATOS_ENEMIGOS)
        iniciar_combate(mi_heroe, enemigo_al_azar)
        
    except (ValueError, IndexError):
        print("Elección inválida. El vacío te ha consumido.")
