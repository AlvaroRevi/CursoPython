"""
main.py - Archivo principal del juego Pong

Este módulo contiene el bucle principal del juego y la configuración inicial.
Coordina todos los elementos del juego: pantalla, paletas, pelota y marcador.

Controles:
- Jugador derecho: Flechas Arriba/Abajo
- Jugador izquierdo: Teclas W/S
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# =============================================================================
# CONFIGURACIÓN DE LA PANTALLA
# =============================================================================
screen = Screen()
screen.bgcolor("black")  # Fondo negro estilo arcade
screen.setup(width=800, height=600)  # Tamaño de la ventana del juego
screen.title("Pong")  # Título de la ventana
screen.tracer(0)  # Desactiva las actualizaciones automáticas para mejor rendimiento

# =============================================================================
# CREACIÓN DE OBJETOS DEL JUEGO
# =============================================================================
# Crear las paletas en sus posiciones iniciales (derecha e izquierda)
r_paddle = Paddle((350, 0))   # Paleta derecha
l_paddle = Paddle((-350, 0))  # Paleta izquierda

# Crear la pelota y el marcador
ball = Ball()
scoreboard = Scoreboard()

# =============================================================================
# CONFIGURACIÓN DE CONTROLES
# =============================================================================
screen.listen()  # Activa la escucha de eventos del teclado

# Controles para la paleta derecha (flechas)
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# Controles para la paleta izquierda (W y S)
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# =============================================================================
# BUCLE PRINCIPAL DEL JUEGO
# =============================================================================
game_is_on = True
while game_is_on:
    screen.update()  # Actualiza la pantalla manualmente
    ball.move()  # Mueve la pelota en cada iteración

    # Detectar colisión con las paredes superior e inferior
    # Si la pelota toca el borde (±280 píxeles), rebota en Y
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detectar colisión con las paletas
    # Comprueba si la pelota está cerca de alguna paleta (distancia < 50)
    # y si está en la zona de la paleta (x > 320 para derecha, x < -320 para izquierda)
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detectar cuando la paleta derecha falla
    # Si la pelota pasa de x=380, punto para el jugador izquierdo
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detectar cuando la paleta izquierda falla
    # Si la pelota pasa de x=-380, punto para el jugador derecho
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Mantiene la ventana abierta hasta que se haga clic
screen.exitonclick()