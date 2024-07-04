# ¿Quien es ese pokemon?

## Requisitos:
### Windows / Linux: pip install -r requirements.txt

<img src='assets/icon.png' alt='game_logo' width='300'>

## Inicio del juego

El juego inicia con una pantalla en donde el jugador puede seleccionar la dificultad y generacion/es con las que quiere jugar. En cuyo caso el usuario no seleccione alguno de los mismos, se asume que se desea jugar con todos (es decir, todas las dificultades/generaciones).
Adicionalmente, un menu en la parte superior derecha ofrece la posibilidad de configurar el sonido del juego si es que el jugador prefiere otra pista (todas originales de los juegos), aumentar o reducir el volumen, o pausar la misma.

<figure>
  <figcaption><sub>Juego iniciado con configuraciones predeterminadas</sub></figcaption>
  <img src='assets/readme_images/game_start.png' alt='game_start' width='600'>
</figure>

<figure>
  <figcaption><sub>Dificultad Facil y generaciones 1 y 2 seleccionadas</sub></figcaption>
  <img src='assets/readme_images/game_start_alternate.png' alt='game_start' width='600'>
</figure>

## Juego Principal

Al usuario se le presenta la silueta de un pokemon y una caja de texto donde debe escribir el que cree es el nombre del mismo, y, adivine o no, se le va a presentar el pokemon revelado con sus nombres en varios idiomas. Si es que adivina correctamente pasa al siguiente, pero si falla vuelve al menu. Dentro de la partida ademas se puede ver cuanto se tardó en adivinar el ultimo pokemon, el adivinado mas rapido (con el nombre del mismo) y cuanto se tardó en promedio en adivinar esta partida.

<figure>
  <figcaption><sub>Inicio del juego principal</sub></figcaption>
  <img src='assets/readme_images/game_guessing.png' alt='game_guessing' width='600'>
</figure>

<figure>
  <figcaption><sub>Pokemon adivinado</sub></figcaption>
  <img src='assets/readme_images/game_guessed.png' alt='game_guessed' width='600'>
</figure>

Al ganar aparece una imagen diciendo lo mismo, y se regresa al inicio.

<figure>
  <figcaption><sub>Juego terminado</sub></figcaption>
  <img src='assets/readme_images/game_won.png' alt='game_won' width='600'>
</figure>

### Video del Juego
- https://youtu.be/QlWORAMBiMY
