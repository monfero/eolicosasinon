# #eolicosAsiNon
Ferramentas para a defensa do territorio contra os macroparques eolicos

**eolicos xlsx2kmz.ipynb** - Notebook python versión Colab.

O script serve para crear unha visualización dos diferentes elementos dun parque eólico (aeroxeneradores, liñas de alta tensión (LAAT), poligonais, ...) a partir dos datos publicados no BOE. Os datos extráense de xeito manual desde a publicación do BOE e gárdanse nunha folla de cálculo. O script traduce as coordenadas dos diferentes elementos, en formato EPSG:25829/30, a formato EPSG:4326, e crea un ficheiro KMZ que se pode importar en ferramentas como Google Maps ou Google Eearth.


**procesar_todo.py** - Versión (obsoleta) previa do script que procesaba ficheiros CSV. [+info](legacy.md)

## Requirimentos

1. Conta en Google e activación de Drive e Colab
2. Experiencia en uso de Colab
3. Git: recomandable para descargar o código

## Uso

1. Utiliza a folla de cálculo modelo para almacenar todos os datos de coordenadas do parque.
2. Sube a folla de cálculo ao teu Google Drive.
3. Configura o script co nome da folla de cálculo.
4. Executa o script e obtén o ficheiro KMZ.

## Configuración do equipo

Para executar o script python debes activar o servizo Colab nunha conta de Google e abrir o Notebook xlsx2kmz.ipynb desde Colab.

Crea unha carpeta no teu Drive destinada aos ficheiros cos que vas traballar. Nesa carpeta, onde colocarás as follas de cálculo a procesar, tamén debes engadir os ficheiros de imaxe que encontrarás no repositorio (laat.png, molino.png, sub.png, torremet.png e untitled.dae).
