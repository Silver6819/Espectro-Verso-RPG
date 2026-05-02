import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Espectro-Verso RPG: Visual Alpha")

# Colores
AZUL_ESPECTRAL = (0, 100, 255)
BLANCO = (255, 255, 255)

# Intentar cargar la imagen de Carlos
try:
    # Usamos el nombre del archivo que ya tienes en GitHub
    imagen_carlos = pygame.image.load("IMG-20241015-WA0017.jpg")
    imagen_carlos = pygame.transform.scale(imagen_carlos, (150, 200))
except:
    # Si la imagen no carga, usamos un rectángulo azul como respaldo
    imagen_carlos = None
    print("No se encontró la imagen, usando marcador.")

# Posición inicial de Carlos
carlos_x = 100
carlos_y = 300
velocidad = 5

# Bucle principal del juego
ejecutando = True
while ejecutando:
    pantalla.fill((30, 30, 30)) # Fondo oscuro
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Movimiento con teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: carlos_x -= velocidad
    if teclas[pygame.K_RIGHT]: carlos_x += velocidad
    if teclas[pygame.K_UP]: carlos_y -= velocidad
    if teclas[pygame.K_DOWN]: carlos_y += velocidad

    # Dibujar a Carlos
    if imagen_carlos:
        pantalla.blit(imagen_carlos, (carlos_x, carlos_y))
    else:
        pygame.draw.rect(pantalla, AZUL_ESPECTRAL, (carlos_x, carlos_y, 50, 100))

    # Texto de ayuda
    fuente = pygame.font.SysFont("Arial", 24)
    texto = fuente.render("Usa las flechas para mover a Carlos Téllez", True, BLANCO)
    pantalla.blit(texto, (20, 20))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
