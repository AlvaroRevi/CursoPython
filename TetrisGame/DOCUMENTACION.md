# 📚 Documentación del Juego Tetris

Esta documentación explica cómo está estructurado el juego Tetris para que puedas entenderlo y aprender a crear juegos similares.

---

## 🗂️ Estructura del Proyecto

```
TetrisGame/
├── main.py          # Punto de entrada y bucle principal
├── game.py          # Lógica del juego (coordina todo)
├── board.py         # Tablero de juego
├── tetromino.py     # Definición de las piezas
└── DOCUMENTACION.md # Este archivo
```

---

## 🎯 Conceptos Clave

### ¿Qué es Pygame?
**Pygame** es una biblioteca de Python para crear juegos 2D. Proporciona:
- Ventanas gráficas
- Manejo de eventos (teclado, ratón)
- Dibujo de formas y texto
- Control de tiempo (FPS)

### Patrón de Diseño: Clases por Responsabilidad
Cada archivo tiene una **única responsabilidad**:
| Archivo | Responsabilidad |
|---------|-----------------|
| `tetromino.py` | Sabe qué forma tiene cada pieza |
| `board.py` | Sabe dónde están los bloques fijos |
| `game.py` | Coordina las reglas del juego |
| `main.py` | Maneja la ventana y los eventos |

---

## 📄 Archivo: `main.py`

### Propósito
Es el **punto de entrada** del programa. Contiene el bucle principal que:
1. Captura eventos del teclado
2. Actualiza el estado del juego
3. Dibuja todo en pantalla

### Estructura Básica de un Juego Pygame

```python
import pygame

# 1. INICIALIZACIÓN
pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
reloj = pygame.time.Clock()

# 2. BUCLE PRINCIPAL
ejecutando = True
while ejecutando:
    reloj.tick(60)  # Limitar a 60 FPS
    
    # 2.1 Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            # Manejar teclas...
    
    # 2.2 Actualizar lógica
    juego.actualizar()
    
    # 2.3 Dibujar
    pantalla.fill(COLOR_FONDO)
    juego.dibujar(pantalla)
    pygame.display.flip()

# 3. CIERRE
pygame.quit()
```

### Conceptos Importantes

| Concepto | Explicación |
|----------|-------------|
| `pygame.init()` | Inicializa todos los módulos de Pygame |
| `set_mode()` | Crea la ventana del juego |
| `Clock.tick(60)` | Limita el juego a 60 FPS |
| `pygame.KEYDOWN` | Evento cuando se presiona una tecla |
| `display.flip()` | Actualiza la pantalla con lo dibujado |

---

## 📄 Archivo: `tetromino.py`

### Propósito
Define las **7 piezas del Tetris** (llamadas tetrominós) y cómo rotan.

### Las 7 Piezas

```
I: ████      O: ██      T:  █       S:  ██      Z: ██
             ██         ███          ██           ██

J: █         L:   █
   ███          ███
```

### Cómo se Representan las Formas

Cada pieza se guarda como una **matriz 2D** donde:
- `1` = hay un bloque
- `0` = vacío

```python
# Ejemplo: La pieza T
'T': [
    [[0, 1, 0], [1, 1, 1]],  # Rotación 0 (T arriba)
    [[1, 0], [1, 1], [1, 0]],  # Rotación 90°
    [[1, 1, 1], [0, 1, 0]],  # Rotación 180°
    [[0, 1], [1, 1], [0, 1]]   # Rotación 270°
]
```

### Clase `Tetromino`

```python
class Tetromino:
    def __init__(self, tipo=None):
        # Si no se especifica, elegir pieza aleatoria
        self.tipo = tipo or random.choice(['I', 'O', 'T', 'S', 'Z', 'J', 'L'])
        self.color = COLORES[self.tipo]
        self.rotacion_actual = 0
        self.x = 3  # Posición inicial centrada
        self.y = 0
    
    @property
    def forma(self):
        # Devuelve la matriz de la rotación actual
        return self.rotaciones[self.rotacion_actual]
    
    def rotar(self):
        # Pasa a la siguiente rotación (vuelve a 0 si llega al final)
        self.rotacion_actual = (self.rotacion_actual + 1) % len(self.rotaciones)
    
    def obtener_bloques(self):
        # Devuelve las coordenadas absolutas de cada bloque
        bloques = []
        for fila_idx, fila in enumerate(self.forma):
            for col_idx, celda in enumerate(fila):
                if celda == 1:
                    bloques.append((self.x + col_idx, self.y + fila_idx))
        return bloques
```

### ¿Por qué usar `@property`?
El decorador `@property` permite acceder a un método como si fuera un atributo:
```python
pieza.forma  # En lugar de pieza.forma()
```

---

## 📄 Archivo: `board.py`

### Propósito
Representa el **tablero de 10x20 celdas** donde caen las piezas.

### La Matriz del Tablero

```python
# Tablero vacío (None = celda vacía)
self.grid = [[None for _ in range(10)] for _ in range(20)]

# Cuando una pieza se fija, se guarda su color:
self.grid[5][3] = (255, 0, 0)  # Bloque rojo en fila 5, columna 3
```

### Métodos Principales

#### `es_posicion_valida(tetromino)`
Verifica si la pieza puede estar en su posición actual:

```python
def es_posicion_valida(self, tetromino):
    for x, y in tetromino.obtener_bloques():
        # ¿Está fuera del tablero?
        if x < 0 or x >= 10 or y >= 20:
            return False
        # ¿Hay un bloque ahí?
        if y >= 0 and self.grid[y][x] is not None:
            return False
    return True
```

#### `limpiar_lineas()`
Elimina las filas completas y baja las de arriba:

```python
def limpiar_lineas(self):
    lineas_eliminadas = 0
    fila = 19  # Empezar desde abajo
    
    while fila >= 0:
        # ¿Está la fila completa?
        if all(celda is not None for celda in self.grid[fila]):
            lineas_eliminadas += 1
            # Mover todo hacia abajo
            for f in range(fila, 0, -1):
                self.grid[f] = self.grid[f - 1].copy()
            self.grid[0] = [None] * 10  # Nueva fila vacía arriba
        else:
            fila -= 1
    
    return lineas_eliminadas
```

### Dibujando con Pygame

```python
def dibujar(self, pantalla):
    for fila in range(20):
        for col in range(10):
            x = 50 + col * 30  # Posición en píxeles
            y = 10 + fila * 30
            
            color = self.grid[fila][col] or COLOR_VACIO
            
            # Dibujar rectángulo relleno
            rect = pygame.Rect(x, y, 30, 30)
            pygame.draw.rect(pantalla, color, rect)
            
            # Dibujar borde
            pygame.draw.rect(pantalla, COLOR_BORDE, rect, 1)
```

---

## 📄 Archivo: `game.py`

### Propósito
**Coordina todo el juego**: tablero, piezas, puntuación, estados.

### Estados del Juego

```python
self.game_over = False  # ¿Terminó el juego?
self.pausado = False    # ¿Está en pausa?
```

### Flujo Principal

```
┌─────────────┐
│  ACTUALIZAR │ ← Se llama cada frame
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────┐
│ ¿Ha pasado suficiente tiempo?   │
│ (según velocidad del nivel)     │
└──────┬──────────────────────────┘
       │ SÍ
       ▼
┌─────────────┐
│ Mover pieza │
│ hacia abajo │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────┐
│ ¿Posición válida?               │
└──────┬──────────────────────────┘
       │ NO
       ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Fijar pieza │───▶│ Limpiar     │───▶│ Nueva pieza │
│ en tablero  │    │ líneas      │    │             │
└─────────────┘    └─────────────┘    └─────────────┘
```

### Sistema de Puntuación

```python
PUNTOS_POR_LINEA = {
    1: 100,   # 1 línea
    2: 300,   # 2 líneas
    3: 500,   # 3 líneas
    4: 800    # Tetris (4 líneas)
}

# Los puntos se multiplican por el nivel actual
puntos = PUNTOS_POR_LINEA[lineas] * self.nivel
```

### Sistema de Niveles

```python
# Subir de nivel cada 10 líneas
nuevo_nivel = (self.lineas // 10) + 1

# Aumentar velocidad (menor intervalo = más rápido)
self.velocidad = max(100, 500 - (self.nivel - 1) * 50)
```

### "Wall Kick" (Ajuste de Rotación)

Cuando una pieza rota pero queda en posición inválida, intenta ajustarse:

```python
def rotar(self):
    self.pieza_actual.rotar()
    
    if not self.tablero.es_posicion_valida(self.pieza_actual):
        # Intentar mover a la izquierda
        self.pieza_actual.x -= 1
        if not self.tablero.es_posicion_valida(self.pieza_actual):
            # Intentar mover a la derecha
            self.pieza_actual.x += 2
            if not self.tablero.es_posicion_valida(self.pieza_actual):
                # No funciona, deshacer rotación
                self.pieza_actual.x -= 1
                self.pieza_actual.rotar_inverso()
```

---

## 🧠 Conceptos de Programación Usados

### 1. Programación Orientada a Objetos (POO)

```python
class Tetromino:          # Definición de clase
    def __init__(self):   # Constructor
        self.x = 0        # Atributo de instancia
    
    def mover(self):      # Método
        self.x += 1
```

### 2. Herencia (en PongGame)

```python
class Ball(Turtle):       # Ball hereda de Turtle
    def __init__(self):
        super().__init__() # Llama al constructor del padre
```

### 3. Propiedades

```python
@property
def forma(self):
    return self.rotaciones[self.rotacion_actual]
```

### 4. List Comprehensions

```python
# Crear lista de 10 elementos None
[None for _ in range(10)]

# Crear matriz 20x10
[[None for _ in range(10)] for _ in range(20)]
```

### 5. Operador Módulo para Ciclos

```python
# Rotar entre 0, 1, 2, 3, 0, 1, 2, 3...
rotacion = (rotacion + 1) % 4
```

---

## 🚀 Cómo Crear tu Propio Juego

### Paso 1: Planifica
- ¿Qué objetos necesitas? (jugador, enemigos, items)
- ¿Cómo interactúan?
- ¿Cuáles son las reglas?

### Paso 2: Estructura
```
MiJuego/
├── main.py       # Bucle principal
├── player.py     # Clase del jugador
├── enemy.py      # Clase de enemigos
└── game.py       # Lógica del juego
```

### Paso 3: Bucle Principal
```python
while ejecutando:
    manejar_eventos()
    actualizar()
    dibujar()
```

### Paso 4: Itera
1. Haz que algo aparezca en pantalla
2. Haz que se mueva
3. Añade colisiones
4. Añade puntuación
5. Añade efectos visuales

---

## 📖 Recursos para Seguir Aprendiendo

- **Pygame**: [pygame.org/docs](https://www.pygame.org/docs/)
- **Tutoriales**: Busca "pygame tutorial español" en YouTube
- **Práctica**: Intenta modificar este juego:
  - Añade efectos de sonido
  - Cambia los colores
  - Añade un sistema de récords
  - Crea nuevas piezas

---

¡Buena suerte con tu aprendizaje! 🎮🐍
