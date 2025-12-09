"""
game.py - Lógica principal del juego Tetris

Este módulo contiene la clase Game que coordina todos los elementos
del juego: tablero, piezas, puntuación y estados del juego.
"""

import pygame
from board import Board, MARGEN_X, COLUMNAS, TAMANO_CELDA
from tetromino import Tetromino

# =============================================================================
# CONSTANTES DEL JUEGO
# =============================================================================
# Velocidad inicial de caída (milisegundos entre movimientos)
VELOCIDAD_INICIAL = 500

# Puntos por líneas eliminadas
PUNTOS_POR_LINEA = {
    1: 100,    # 1 línea = 100 puntos
    2: 300,    # 2 líneas = 300 puntos
    3: 500,    # 3 líneas = 500 puntos
    4: 800     # Tetris (4 líneas) = 800 puntos
}

# Colores para la interfaz
COLOR_TEXTO = (255, 255, 255)
COLOR_GAME_OVER = (255, 50, 50)


class Game:
    """
    Clase principal que maneja la lógica del juego Tetris.
    
    Coordina el tablero, las piezas, la puntuación y los diferentes
    estados del juego (jugando, pausado, game over).
    
    Atributos:
        tablero (Board): El tablero de juego
        pieza_actual (Tetromino): La pieza que está cayendo
        siguiente_pieza (Tetromino): La próxima pieza
        puntuacion (int): Puntuación del jugador
        nivel (int): Nivel actual (afecta la velocidad)
        lineas (int): Total de líneas eliminadas
        game_over (bool): Indica si el juego terminó
        pausado (bool): Indica si el juego está pausado
        ultimo_movimiento (int): Timestamp del último movimiento automático
        velocidad (int): Milisegundos entre caídas automáticas
    """

    def __init__(self):
        """Inicializa una nueva partida de Tetris."""
        self.tablero = Board()
        self.pieza_actual = Tetromino()
        self.siguiente_pieza = Tetromino()
        self.puntuacion = 0
        self.nivel = 1
        self.lineas = 0
        self.game_over = False
        self.pausado = False
        self.ultimo_movimiento = pygame.time.get_ticks()
        self.velocidad = VELOCIDAD_INICIAL
        
        # Cargar fuente para el texto
        pygame.font.init()
        self.fuente = pygame.font.Font(None, 36)
        self.fuente_grande = pygame.font.Font(None, 48)

    def actualizar(self):
        """
        Actualiza el estado del juego en cada frame.
        
        Maneja la caída automática de las piezas según la velocidad
        del nivel actual.
        """
        # No actualizar si está pausado o game over
        if self.pausado or self.game_over:
            return
        
        tiempo_actual = pygame.time.get_ticks()
        
        # Verificar si es momento de mover la pieza hacia abajo
        if tiempo_actual - self.ultimo_movimiento > self.velocidad:
            self._mover_pieza_abajo()
            self.ultimo_movimiento = tiempo_actual

    def _mover_pieza_abajo(self):
        """
        Mueve la pieza actual una posición hacia abajo.
        
        Si la pieza no puede moverse, la fija en el tablero y
        genera una nueva pieza.
        """
        self.pieza_actual.y += 1
        
        # Verificar si el movimiento es válido
        if not self.tablero.es_posicion_valida(self.pieza_actual):
            # Revertir el movimiento
            self.pieza_actual.y -= 1
            # Fijar la pieza en el tablero
            self._fijar_pieza()

    def _fijar_pieza(self):
        """
        Fija la pieza actual en el tablero y genera una nueva.
        
        También verifica si hay líneas completas y actualiza
        la puntuación.
        """
        # Fijar la pieza en el tablero
        self.tablero.fijar_pieza(self.pieza_actual)
        
        # Limpiar líneas completas y obtener puntos
        lineas_eliminadas = self.tablero.limpiar_lineas()
        if lineas_eliminadas > 0:
            self._sumar_puntos(lineas_eliminadas)
        
        # Generar nueva pieza
        self.pieza_actual = self.siguiente_pieza
        self.siguiente_pieza = Tetromino()
        
        # Verificar game over
        if not self.tablero.es_posicion_valida(self.pieza_actual):
            self.game_over = True

    def _sumar_puntos(self, lineas):
        """
        Suma puntos según las líneas eliminadas.
        
        Args:
            lineas (int): Número de líneas eliminadas (1-4)
        """
        # Añadir puntos base
        self.puntuacion += PUNTOS_POR_LINEA.get(lineas, 100 * lineas) * self.nivel
        self.lineas += lineas
        
        # Subir de nivel cada 10 líneas
        nuevo_nivel = (self.lineas // 10) + 1
        if nuevo_nivel > self.nivel:
            self.nivel = nuevo_nivel
            # Aumentar velocidad (reducir el intervalo)
            self.velocidad = max(100, VELOCIDAD_INICIAL - (self.nivel - 1) * 50)

    def mover_izquierda(self):
        """Mueve la pieza actual una posición a la izquierda."""
        if self.pausado or self.game_over:
            return
        
        self.pieza_actual.x -= 1
        if not self.tablero.es_posicion_valida(self.pieza_actual):
            self.pieza_actual.x += 1  # Revertir si es inválido

    def mover_derecha(self):
        """Mueve la pieza actual una posición a la derecha."""
        if self.pausado or self.game_over:
            return
        
        self.pieza_actual.x += 1
        if not self.tablero.es_posicion_valida(self.pieza_actual):
            self.pieza_actual.x -= 1  # Revertir si es inválido

    def mover_abajo(self):
        """Acelera la caída de la pieza actual."""
        if self.pausado or self.game_over:
            return
        
        self._mover_pieza_abajo()
        self.ultimo_movimiento = pygame.time.get_ticks()

    def rotar(self):
        """Rota la pieza actual 90 grados en sentido horario."""
        if self.pausado or self.game_over:
            return
        
        self.pieza_actual.rotar()
        
        # Si la rotación resulta en posición inválida, intentar "wall kick"
        if not self.tablero.es_posicion_valida(self.pieza_actual):
            # Intentar mover a la izquierda
            self.pieza_actual.x -= 1
            if not self.tablero.es_posicion_valida(self.pieza_actual):
                # Intentar mover a la derecha (2 posiciones desde la original)
                self.pieza_actual.x += 2
                if not self.tablero.es_posicion_valida(self.pieza_actual):
                    # Revertir todo
                    self.pieza_actual.x -= 1
                    self.pieza_actual.rotar_inverso()

    def caida_instantanea(self):
        """
        Hace que la pieza caiga instantáneamente hasta el fondo.
        
        También conocido como "hard drop".
        """
        if self.pausado or self.game_over:
            return
        
        # Mover hacia abajo hasta que no sea válido
        while self.tablero.es_posicion_valida(self.pieza_actual):
            self.pieza_actual.y += 1
        
        # Retroceder un paso (última posición válida)
        self.pieza_actual.y -= 1
        self._fijar_pieza()

    def pausar(self):
        """Alterna el estado de pausa del juego."""
        if not self.game_over:
            self.pausado = not self.pausado

    def reiniciar(self):
        """Reinicia el juego para empezar una nueva partida."""
        self.tablero.reiniciar()
        self.pieza_actual = Tetromino()
        self.siguiente_pieza = Tetromino()
        self.puntuacion = 0
        self.nivel = 1
        self.lineas = 0
        self.game_over = False
        self.pausado = False
        self.velocidad = VELOCIDAD_INICIAL

    def dibujar(self, pantalla):
        """
        Dibuja todos los elementos del juego en la pantalla.
        
        Args:
            pantalla: Superficie de Pygame donde dibujar
        """
        # Dibujar el tablero con la pieza actual
        self.tablero.dibujar(pantalla, self.pieza_actual)
        
        # Dibujar información del juego (lado derecho)
        x_info = MARGEN_X + COLUMNAS * TAMANO_CELDA + 30
        
        # Título "SIGUIENTE"
        texto = self.fuente.render("SIGUIENTE:", True, COLOR_TEXTO)
        pantalla.blit(texto, (x_info, 20))
        
        # Dibujar la siguiente pieza
        self._dibujar_siguiente_pieza(pantalla, x_info, 60)
        
        # Puntuación
        texto = self.fuente.render(f"PUNTOS:", True, COLOR_TEXTO)
        pantalla.blit(texto, (x_info, 180))
        texto = self.fuente.render(f"{self.puntuacion}", True, COLOR_TEXTO)
        pantalla.blit(texto, (x_info, 210))
        
        # Nivel
        texto = self.fuente.render(f"NIVEL: {self.nivel}", True, COLOR_TEXTO)
        pantalla.blit(texto, (x_info, 270))
        
        # Líneas
        texto = self.fuente.render(f"LÍNEAS: {self.lineas}", True, COLOR_TEXTO)
        pantalla.blit(texto, (x_info, 310))
        
        # Mostrar mensaje de pausa
        if self.pausado:
            self._dibujar_mensaje_central(pantalla, "PAUSA", "Presiona P para continuar")
        
        # Mostrar mensaje de game over
        if self.game_over:
            self._dibujar_mensaje_central(pantalla, "GAME OVER", "Presiona R para reiniciar")

    def _dibujar_siguiente_pieza(self, pantalla, x, y):
        """
        Dibuja la vista previa de la siguiente pieza.
        
        Args:
            pantalla: Superficie de Pygame
            x: Posición X donde dibujar
            y: Posición Y donde dibujar
        """
        tamano_preview = 20  # Tamaño más pequeño para el preview
        
        for fila_idx, fila in enumerate(self.siguiente_pieza.forma):
            for col_idx, celda in enumerate(fila):
                if celda == 1:
                    rect = pygame.Rect(
                        x + col_idx * tamano_preview,
                        y + fila_idx * tamano_preview,
                        tamano_preview,
                        tamano_preview
                    )
                    pygame.draw.rect(pantalla, self.siguiente_pieza.color, rect)
                    pygame.draw.rect(pantalla, (100, 100, 100), rect, 1)

    def _dibujar_mensaje_central(self, pantalla, titulo, subtitulo):
        """
        Dibuja un mensaje centrado en la pantalla con fondo semitransparente.
        
        Args:
            pantalla: Superficie de Pygame
            titulo: Texto principal del mensaje
            subtitulo: Texto secundario
        """
        # Crear superficie semitransparente
        overlay = pygame.Surface((500, 620))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        pantalla.blit(overlay, (0, 0))
        
        # Dibujar título
        texto = self.fuente_grande.render(titulo, True, COLOR_GAME_OVER)
        rect = texto.get_rect(center=(250, 280))
        pantalla.blit(texto, rect)
        
        # Dibujar subtítulo
        texto = self.fuente.render(subtitulo, True, COLOR_TEXTO)
        rect = texto.get_rect(center=(250, 330))
        pantalla.blit(texto, rect)
