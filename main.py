import random
from personajes import carlos, haru, misuzu
from enemigos import BASE_DE_DATOS_ENEMIGOS

def iniciar_combate(jugador, enemigo_data):
    e_nombre = enemigo_data["nombre"]
    e_hp = enemigo_data["hp"]
    e_atk = enemigo_data["atk"]
    
    print(f"\n--- ¡PELIGRO! Aparece {e_nombre} ---")
    
    while jugador.hp > 0 and e_hp > 0:
        print(f"\n{jugador.stats()}")
        print(f"{e_nombre} | HP: {e_hp}")
        print("1. Atacar | 2. Usar Especial")
        
        opc = input("Elige tu movimiento: ")
        if opc == "1":
            danio = jugador.atk + random.randint(0, 5)
            e_hp -= danio
            print(f"¡Golpeas al {e_nombre} causando {danio} de daño!")
        elif opc == "2" and jugador.ki >= 20:
            jugador.ki -= 20
            danio = jugador.atk * 3
            print(f"¡{jugador.especial.upper()}! {jugador.desc_esp}")
            e_hp -= danio
        
        if e_hp > 0:
            d_e = e_atk + random.randint(-3, 3)
            jugador.hp -= d_e
            print(f"El {e_nombre} contraataca y te quita {d_e} HP.")

    if jugador.hp > 0: print(f"¡Has vencido al {e_nombre}!")
    else: print("Has caído en batalla...")

# Simulación rápida
if __name__ == "__main__":
    print("--- BIENVENIDO AL ESPECTRO-VERSO RPG ---")
    iniciar_combate(carlos, random.choice(BASE_DE_DATOS_ENEMIGOS))
