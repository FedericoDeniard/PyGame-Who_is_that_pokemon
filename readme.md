# ¿Quien es ese pokemon?

## Requisitos:
### Windows / Linux: pip install -r requirements.txt

<img src='https://github.com/FedericoDeniard/PyGame-Who_is_that_pokemon/assets/icon.png' alt='game_logo' width='300'>

## Inicio del juego

El juego inicia con una pantalla en donde el jugador puede seleccionar la dificultad y generacion/es con las que quiere jugar. En cuyo caso el usuario no seleccione alguno de los mismos, se asume que se desea jugar con todos (es decir, todas las dificultades/generaciones).
Adicionalmente, un menu en la parte superior derecha ofrece la posibilidad de configurar el sonido del juego si es que el jugador prefiere otra pista (todas originales de los juegos), aumentar o reducir el volumen, o pausar la misma.

<img src='https://github.com/FedericoDeniard/PyGame-Who_is_that_pokemon/assets/readme_images/game_start' alt='game_start' width='300'>
Juego iniciado con configuraciones predeterminadas

<img src='https://github.com/FedericoDeniard/PyGame-Who_is_that_pokemon/assets/readme_images/game_start_alternate' alt='game_start' width='300'>
Dificultad Facil y generaciones 1 y 2 seleccionadas

## Juego Principal

Al usuario se le presenta la silueta de un pokemon y una caja de texto donde debe escribir el que cree es el nombre del mismo, y, adivine o no, se le va a presentar el pokemon revelado con sus nombres en varios idiomas. Si es que adivina correctamente pasa al siguiente, pero si falla vuelve al menu. Dentro de la partida ademas se puede ver cuanto se tardó en adivinar el ultimo pokemon, el adivinado mas rapido (con el nombre del mismo) y cuanto se tardó en promedio en adivinar esta partida.

<img src='https://github.com/FedericoDeniard/PyGame-Who_is_that_pokemon/assets/readme_images/game_guessing' alt='game_guessing' width='300'>
Inicio del juego principal

<img src='https://github.com/FedericoDeniard/PyGame-Who_is_that_pokemon/assets/readme_images/game_guessed' alt='game_guessed' width='300'>
Pokemon adivinado

Al ganar aparece una imagen diciendo lo mismo, y se regresa al inicio.

<img src='https://github.com/FedericoDeniard/PyGame-Who_is_that_pokemon/assets/readme_images/game_start_won' alt='game_won' width='300'>
Juego terminado