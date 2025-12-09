"""
tetromino.py - Definición de las piezas del Tetris (Tetrominós)

Este módulo contiene la clase Tetromino y las definiciones de todas
las piezas del juego. Cada pieza está formada por 4 bloques.

Las 7 piezas estándar del Tetris son:
- I: Línea recta (cian)
- O: Cuadrado (amarillo)
- T: Forma de T (púrpura)
- S: Forma de S (verde)
- Z: Forma de Z (rojo)
- J: Forma de J (azul)
- L: Forma de L (naranja)
"""

import random

# =============================================================================
# DEFINICIÓN DE LAS FORMAS DE LOS TETROMINÓS
# =============================================================================
# Cada forma se define como una lista de rotaciones.
# Cada rotación es una matriz donde 1 indica un bloque y 0 indica vacío.

FORMAS = {
    'I': [
        [[1, 1, 1, 1]],  # Horizontal
        [[1], [1], [1], [1]]  # Vertical
    ],
    'O': [
        [[1, 1], [1, 1]]  # El cuadrado no cambia al rotar
    ],
    'T': [
        [[0, 1, 0], [1, 1, 1]],  # T hacia arriba
        [[1, 0], [1, 1], [1, 0]],  # T hacia la derecha
        [[1, 1, 1], [0, 1, 0]],  # T hacia abajo
        [[0, 1], [1, 1], [0, 1]]  # T hacia la izquierda
    ],
    'S': [
        [[0, 1, 1], [1, 1, 0]],  # S horizontal
        [[1, 0], [1, 1], [0, 1]]  # S vertical
    ],
    'Z': [
        [[1, 1, 0], [0, 1, 1]],  # Z horizontal
        [[0, 1], [1, 1], [1, 0]]  # Z vertical
    ],
    'J': [
        [[1, 0, 0], [1, 1, 1]],  # J hacia arriba
        [[1, 1], [1, 0], [1, 0]],  # J hacia la derecha
        [[1, 1, 1], [0, 0, 1]],  # J hacia abajo
        [[0, 1], [0, 1], [1, 1]]  # J hacia la izquierda
    ],
    'L': [
        [[0, 0, 1], [1, 1, 1]],  # L hacia arriba
        [[1, 0], [1, 0], [1, 1]],  # L hacia la derecha
        [[1, 1, 1], [1, 0, 0]],  # L hacia abajo
        [[1, 1], [0, 1], [0, 1]]  # L hacia la izquierda
    ]
}

# =============================================================================
# COLORES DE LOS TETROMINÓS (RGB)
# =============================================================================
COLORES = {
    'I': (0, 255, 255),     # Cian
    'O': (255, 255, 0),     # Amarillo
    'T': (128, 0, 128),     # Púrpura
    'S': (0, 255, 0),       # Verde
    'Z': (255, 0, 0),       # Rojo
    'J': (0, 0, 255),       # Azul
    'L': (255, 165, 0)      # Naranja
}


class Tetromino:
    """
    Clase que representa una pieza del Tetris (Tetrominó).
    
    Cada tetrominó tiene una forma, color, posición y puede rotar.
    La posición (x, y) indica la esquina superior izquierda de la
    matriz que contiene la pieza.
    
    Atributos:
        tipo (str): Tipo de pieza ('I', 'O', 'T', 'S', 'Z', 'J', 'L')
        color (tuple): Color RGB de la pieza
        rotaciones (list): Lista de todas las rotaciones posibles
        rotacion_actual (int): Índice de la rotación actual
        x (int): Posición horizontal en el tablero (columna)
        y (int): Posición vertical en el tablero (fila)
    """

    def __init__(self, tipo=None):
        """
        Inicializa un nuevo tetrominó.
        
        Args:
            tipo (str, opcional): Tipo de pieza. Si es None, se elige aleatoriamente.
        """
        # Si no se especifica tipo, elegir uno aleatorio
        if tipo is None:
            tipo = random.choice(list(FORMAS.keys()))
        
        self.tipo = tipo
        self.color = COLORES[tipo]
        self.rotaciones = FORMAS[tipo]
        self.rotacion_actual = 0
        
        # Posición inicial: centrado horizontalmente, arriba del tablero
        self.x = 3  # Columna inicial (centrado en tablero de 10 columnas)
        self.y = 0  # Fila inicial (arriba del todo)

    @property
    def forma(self):
        """
        Obtiene la forma actual de la pieza según su rotación.
        
        Returns:
            list: Matriz 2D representando la forma actual de la pieza.
        """
        return self.rotaciones[self.rotacion_actual]

    def rotar(self):
        """
        Rota la pieza 90 grados en sentido horario.
        
        Cambia al siguiente estado de rotación, volviendo al primero
        si se supera el último.
        """
        self.rotacion_actual = (self.rotacion_actual + 1) % len(self.rotaciones)

    def rotar_inverso(self):
        """
        Rota la pieza 90 grados en sentido antihorario.
        
        Útil para deshacer una rotación si resulta inválida.
        """
        self.rotacion_actual = (self.rotacion_actual - 1) % len(self.rotaciones)

    def obtener_bloques(self):
        """
        Obtiene las coordenadas absolutas de todos los bloques de la pieza.
        
        Returns:
            list: Lista de tuplas (x, y) con las coordenadas de cada bloque.
        """
        bloques = []
        for fila_idx, fila in enumerate(self.forma):
            for col_idx, celda in enumerate(fila):
                if celda == 1:  # Si hay un bloque en esta posición
                    bloques.append((self.x + col_idx, self.y + fila_idx))
        return bloques

    def clonar(self):
        """
        Crea una copia de este tetrominó.
        
        Útil para probar movimientos sin modificar la pieza original.
        
        Returns:
            Tetromino: Nueva instancia con los mismos valores.
        """
        clon = Tetromino(self.tipo)
        clon.rotacion_actual = self.rotacion_actual
        clon.x = self.x
        clon.y = self.y
        return clon
