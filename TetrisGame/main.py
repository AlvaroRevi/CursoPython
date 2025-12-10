"""
main.py - Archivo principal del juego Tetris

Este módulo inicia el juego Tetris y contiene el bucle principal.
Utiliza la biblioteca Pygame para los gráficos y la interacción.

Controles:
- Flecha Izquierda: Mover pieza a la izquierda
- Flecha Derecha: Mover pieza a la derecha
- Flecha Abajo: Acelerar caída
- Flecha Arriba / Z: Rotar pieza
- Espacio: Caída instantánea (hard drop)
- P: Pausar juego
- R: Reiniciar juego
"""

import pygame
from game import Game

# =============================================================================
# CONSTANTES DEL JUEGO
# =============================================================================
ANCHO_VENTANA = 500      # Ancho total de la ventana en píxeles
ALTO_VENTANA = 620       # Alto total de la ventana en píxeles
FPS = 60                 # Fotogramas por segundo

# Colores (RGB)
COLOR_FONDO = (20, 20, 30)        # Azul oscuro para el fondo
COLOR_TEXTO = (255, 255, 255)     # Blanco para el texto


def main():
    """
    Función principal que inicializa y ejecuta el juego.
    
    Configura Pygame, crea la ventana del juego y ejecuta
    el bucle principal hasta que el jugador cierre la ventana.
    """
    # ==========================================================================
    # INICIALIZACIÓN DE PYGAME
    # ==========================================================================
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Tetris - CursoPython")
    reloj = pygame.time.Clock()
    
    # Crear la instancia del juego
    juego = Game()
    
    # Variable para controlar el bucle principal
    ejecutando = True
    
    # ==========================================================================
    # BUCLE PRINCIPAL DEL JUEGO
    # ==========================================================================
    while ejecutando:
        # Limitar los FPS del juego
        reloj.tick(FPS)
        
        # ---------------------------------------------------------------------
        # MANEJO DE EVENTOS
        # ---------------------------------------------------------------------
        for evento in pygame.event.get():
            # Evento de cerrar ventana
            if evento.type == pygame.QUIT:
                ejecutando = False
            
            # Eventos de teclado (solo cuando se presiona la tecla)
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    juego.mover_izquierda()
                elif evento.key == pygame.K_RIGHT:
                    juego.mover_derecha()
                elif evento.key == pygame.K_DOWN:
                    juego.mover_abajo()
                elif evento.key == pygame.K_UP or evento.key == pygame.K_z:
                    juego.rotar()
                elif evento.key == pygame.K_SPACE:
                    juego.caida_instantanea()
                elif evento.key == pygame.K_p:
                    juego.pausar()
                elif evento.key == pygame.K_r:
                    juego.reiniciar()
        
        # ---------------------------------------------------------------------
        # ACTUALIZACIÓN DEL ESTADO DEL JUEGO
        # ---------------------------------------------------------------------
        juego.actualizar()
        
        # ---------------------------------------------------------------------
        # RENDERIZADO
        # ---------------------------------------------------------------------
        pantalla.fill(COLOR_FONDO)  # Limpiar pantalla con color de fondo
        juego.dibujar(pantalla)      # Dibujar todos los elementos del juego
        pygame.display.flip()        # Actualizar la pantalla
    
    # ==========================================================================
    # CIERRE DEL JUEGO
    # ==========================================================================
    pygame.quit()


# Punto de entrada del programa
if __name__ == "__main__":
    main()
