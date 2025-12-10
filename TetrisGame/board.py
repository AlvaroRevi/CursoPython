"""
board.py - Tablero del juego Tetris

Este módulo contiene la clase Board que representa el tablero de juego.
El tablero es una matriz donde se almacenan las piezas que ya han caído.
"""

import pygame

# =============================================================================
# CONSTANTES DEL TABLERO
# =============================================================================
COLUMNAS = 10          # Número de columnas del tablero
FILAS = 20             # Número de filas del tablero
TAMANO_CELDA = 30      # Tamaño de cada celda en píxeles
MARGEN_X = 50          # Margen izquierdo del tablero en la pantalla
MARGEN_Y = 10          # Margen superior del tablero en la pantalla

# Colores
COLOR_BORDE = (100, 100, 100)     # Gris para el borde de las celdas
COLOR_VACIO = (30, 30, 40)        # Gris oscuro para celdas vacías
COLOR_LINEA = (50, 50, 60)        # Color de las líneas de la cuadrícula


class Board:
    """
    Clase que representa el tablero del juego Tetris.
    
    El tablero es una matriz de FILAS x COLUMNAS donde cada celda
    puede estar vacía (None) o contener un color (tupla RGB).
    
    Atributos:
        grid (list): Matriz 2D que almacena el estado del tablero
        columnas (int): Número de columnas
        filas (int): Número de filas
    """

    def __init__(self):
        """Inicializa un tablero vacío."""
        self.columnas = COLUMNAS
        self.filas = FILAS
        # Crear matriz vacía (None indica celda vacía)
        self.grid = [[None for _ in range(COLUMNAS)] for _ in range(FILAS)]

    def es_posicion_valida(self, tetromino):
        """
        Verifica si la posición actual del tetrominó es válida.
        
        Una posición es válida si todos los bloques de la pieza:
        1. Están dentro de los límites del tablero
        2. No colisionan con bloques ya colocados
        
        Args:
            tetromino: La pieza a verificar
            
        Returns:
            bool: True si la posición es válida, False en caso contrario
        """
        for x, y in tetromino.obtener_bloques():
            # Verificar límites horizontales
            if x < 0 or x >= self.columnas:
                return False
            # Verificar límite inferior
            if y >= self.filas:
                return False
            # Verificar colisión con bloques existentes (solo si y >= 0)
            if y >= 0 and self.grid[y][x] is not None:
                return False
        return True

    def fijar_pieza(self, tetromino):
        """
        Fija un tetrominó en el tablero.
        
        Coloca los bloques de la pieza en la matriz del tablero,
        guardando su color en las posiciones correspondientes.
        
        Args:
            tetromino: La pieza a fijar en el tablero
        """
        for x, y in tetromino.obtener_bloques():
            if 0 <= y < self.filas and 0 <= x < self.columnas:
                self.grid[y][x] = tetromino.color

    def limpiar_lineas(self):
        """
        Elimina las líneas completas del tablero.
        
        Una línea está completa cuando todas sus celdas tienen un bloque.
        Las líneas superiores caen para ocupar el espacio vacío.
        
        Returns:
            int: Número de líneas eliminadas
        """
        lineas_eliminadas = 0
        fila = self.filas - 1  # Empezar desde abajo
        
        while fila >= 0:
            # Verificar si la fila está completa
            if all(celda is not None for celda in self.grid[fila]):
                lineas_eliminadas += 1
                # Mover todas las filas superiores hacia abajo
                for f in range(fila, 0, -1):
                    self.grid[f] = self.grid[f - 1].copy()
                # Crear nueva fila vacía arriba
                self.grid[0] = [None for _ in range(self.columnas)]
                # No decrementar fila para verificar la misma posición
                # (podría haber otra línea completa que bajó)
            else:
                fila -= 1
        
        return lineas_eliminadas

    def esta_lleno(self):
        """
        Verifica si el tablero está lleno (game over).
        
        El juego termina cuando hay bloques en la fila superior.
        
        Returns:
            bool: True si hay bloques en la fila 0, False en caso contrario
        """
        return any(celda is not None for celda in self.grid[0])

    def reiniciar(self):
        """Limpia el tablero para empezar una nueva partida."""
        self.grid = [[None for _ in range(self.columnas)] for _ in range(self.filas)]

    def dibujar(self, pantalla, pieza_actual=None):
        """
        Dibuja el tablero y la pieza actual en la pantalla.
        
        Args:
            pantalla: Superficie de Pygame donde dibujar
            pieza_actual: Tetrominó actual en juego (opcional)
        """
        # Dibujar cada celda del tablero
        for fila in range(self.filas):
            for col in range(self.columnas):
                # Calcular posición en píxeles
                x = MARGEN_X + col * TAMANO_CELDA
                y = MARGEN_Y + fila * TAMANO_CELDA
                
                # Obtener color de la celda
                color = self.grid[fila][col]
                if color is None:
                    color = COLOR_VACIO
                
                # Dibujar celda rellena
                rect = pygame.Rect(x, y, TAMANO_CELDA, TAMANO_CELDA)
                pygame.draw.rect(pantalla, color, rect)
                
                # Dibujar borde de la celda
                pygame.draw.rect(pantalla, COLOR_LINEA, rect, 1)
        
        # Dibujar la pieza actual si existe
        if pieza_actual:
            for bx, by in pieza_actual.obtener_bloques():
                if by >= 0:  # Solo dibujar si está dentro del área visible
                    x = MARGEN_X + bx * TAMANO_CELDA
                    y = MARGEN_Y + by * TAMANO_CELDA
                    rect = pygame.Rect(x, y, TAMANO_CELDA, TAMANO_CELDA)
                    pygame.draw.rect(pantalla, pieza_actual.color, rect)
                    pygame.draw.rect(pantalla, COLOR_BORDE, rect, 2)

        # Dibujar borde exterior del tablero
        borde = pygame.Rect(
            MARGEN_X - 2,
            MARGEN_Y - 2,
            self.columnas * TAMANO_CELDA + 4,
            self.filas * TAMANO_CELDA + 4
        )
        pygame.draw.rect(pantalla, (200, 200, 200), borde, 3)
