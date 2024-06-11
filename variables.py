import customtkinter as ctk
from PIL import Image, ImageTk


vidas = 3
pregunta = 1

imagen = ctk.CTkImage(light_image=Image.open("descartes.png"), 
                                dark_image=Image.open("descartes.png"),
                                size = (300,300)
                                )
imagen_tipos_funciones = ctk.CTkImage(light_image=Image.open("tipos_funciones.png"), 
                                dark_image=Image.open("tipos_funciones.png"),
                                size = (800,600))

funcion_inyectiva = ctk.CTkImage(light_image=Image.open("funcion_inyectiva.png"), 
                                dark_image=Image.open("funcion_inyectiva.png"),
                                size = (800,600))

funcion_sobreyectiva = ctk.CTkImage(light_image=Image.open("funcion_sobreyectiva.png"),
                                dark_image=Image.open("funcion_sobreyectiva.png"),
                                size = (800,560))
funcion_biyectiva = ctk.CTkImage(light_image=Image.open("funcion_biyectiva.png"),
                                dark_image=Image.open("funcion_biyectiva.png"),
                                size = (800,560))
metodo_resolucion_cuadratica = ctk.CTkImage(light_image=Image.open("metodo_resolucion_cuadratica.png"),
                                dark_image=Image.open("metodo_resolucion_cuadratica.png"),
                                size = (400,250))
imagen_2_cuadratica = ctk.CTkImage(light_image=Image.open("imagen_2_cuadratica.png"), 
                                   dark_image=Image.open("imagen_2_cuadratica.png"),
                                   size = (400,250))
imagen_3_cuadratica = ctk.CTkImage(light_image=Image.open("imagen_3_cuadratica.png"), 
                                   dark_image=Image.open("imagen_3_cuadratica.png"),
                                   size = (400,250))
imagen_4_cuadratica = ctk.CTkImage(light_image=Image.open("imagen_4_cuadratica.png"), 
                                   dark_image=Image.open("imagen_4_cuadratica.png"),
                                   size = (400,250))
imagen_1_raiz = ctk.CTkImage(light_image=Image.open("imagen_1_raiz.png"), 
                                   dark_image=Image.open("imagen_1_raiz.png"),
                                   size = (400,250))
imagen_2_raiz = ctk.CTkImage(light_image=Image.open("imagen_2_raiz.png"), 
                                   dark_image=Image.open("imagen_2_raiz.png"),
                                   size = (400,250))
imagen_3_raiz = ctk.CTkImage(light_image=Image.open("imagen_3_raiz.png"), 
                                   dark_image=Image.open("imagen_3_raiz.png"),
                                   size = (400,250))
imagen_1_exponencial = ctk.CTkImage(light_image=Image.open("imagen_1_exponencial.png"), 
                                   dark_image=Image.open("imagen_1_exponencial.png"),
                                   size = (400,250))
imagen_1_logaritmica = ctk.CTkImage(light_image=Image.open("imagen_1_logaritmica.png"), 
                                   dark_image=Image.open("imagen_1_logaritmica.png"),
                                   size = (400,250))
imagen_1_seno = ctk.CTkImage(light_image=Image.open("imagen_1_seno.png"), 
                                   dark_image=Image.open("imagen_1_seno.png"),
                                   size = (400,250))
imagen_2_seno = ctk.CTkImage(light_image=Image.open("imagen_2_seno.png"), 
                                   dark_image=Image.open("imagen_2_seno.png"),
                                   size = (400,250))
imagen_3_seno = ctk.CTkImage(light_image=Image.open("imagen_3_seno.png"), 
                                   dark_image=Image.open("imagen_3_seno.png"),
                                   size = (400,250))

definicion_funcion ="""DEFINICIÓN DE UNA FUNCIÓN

La función de un conjunto X en un conjunto Y es una correspondencia que le asigna 
a cada elemento de X uno y sólo un elemento en Y. 

El conjunto X es el dominio de la función, el Y es el rango. 
Se denota con una letra f o g.

DOMINIO
Son valores que se le permiten ingresar a una función (valores de x). 
Es el conjunto de todas las entradas reales que dan resultados reales.

RANGO 
Es el conjunto de valores que responden o se generan en una función (valores de y).
"""
inyectiva = """CLASES DE FUNCIONES

Funciones Inyectivas, Sobreyectivas y Biyectivas

INYECTIVAS

Una función es inyectiva cuando no hay dos elementos del dominio que tengan la misma imagen.
Es decir, para cualesquiera dos elementos a y b, pertenecientes al dominio de la función Domf, 
si sus imágenes f(a) y f(b) son iguales, los elementos son necesariamente iguales.
"""
sobreyectiva = """ SOBREYECTIVAS

Una función es sobreyectiva, también llamada suprayectiva o exhaustiva,
cuando el rango y el recorrido coinciden. 
Es decir, para cualquier elemento Y del rango existe otro elemento X del dominio
tal que Y es la imagen de X por f."""

biyectiva = """BIYECTIVAS

Una función es biyectiva, cuando es inyectiva y sobreyectiva al mismo tiempo.
Es decir, para cualquier elemento Y del rango existe un único elemento X del dominio
tal que y es la imagen de x por f."""

lineal = """FUNCIÓN LINEAL

Una función lineal es una función cuyo dominio y rango 
son todos los números reales y cuya expresión analítica 
es un polinomio de primer grado.

Por ejemplo, son funciones lineales: 
1)f(x) = 2x + 5                                           
2)g(x) = -3x + 7


ECUACIONES:
1)Canónica: y = mx + b
2)Ecuación punto pendiente: y – y1 = m(x – x1)
3)Ecuación general: Ax + By + C = 0
4)Para hallar la pendiente: m = (y2 – y1) / (x2 – x1)

La pendiente es el valor que adopte “m” o el que acompaña
a la variable “x” la cual determina el grado de inclinación
de la gráfica y si la función es creciente o decreciente. 
“b” es el corte con el eje de las ordenadas.
Si m > 0, la función es creciente, si m < 0, la función es decreciente 
y en caso de que m = 0, la función no tendrá pendiente y será constante.

Las funciones lineales poseen una gráfica determinada
por una recta y analíticamente son ecuaciones de primer grado. 
Esta función además cumple que el incremento de los valores 
de los elementos del dominio es proporcional al incremento 
de los valores en el rango, siempre y cuando la pendiente no sea igual a 0.


¿QUÉ SE NECESITA PARA GRAFICARLA?
1)	Dos puntos en el plano cartesiano.
2)	Un punto en el plano cartesiano y la pendiente.
"""
cuadratica_1 = """FUNCIÓN CUADRÁTICA

En álgebra, una función cuadrática es una función polinómica con una o más variables
en la que el término de grado más alto es de segundo grado (2).

Por ejemplo, son funciones cuadráticas:
f(x) = x^2+x+2
f(x) = 2x^2++4x+8


ECUACIONES:
Forma general:  〖ax〗^2+bx+c=0   siendo a ≠ 0
Forma de vértice: y = a ( x – h ) 2 + k
Forma factorizada:  y=a(x-x_1)(x+x_2)

La gráfica de una función cuadrática es una parábola, una curva de 2 dimensiones
en forma de U. Una característica importante del gráfico es que tiene un punto 
extremo, denominado vértice. Si la parábola se abre hacia arriba, el vértice 
representa el punto más bajo en el gráfico o el valor mínimo de la función 
cuadrática. Si abre hacia abajo el vértice representa el punto más alto de la parábola.

El punto de corte con el eje de ordenadas viene dado por el punto (0, c). 
Esto quiere decir que el término independiente es el punto en donde la parábola 
corta el eje y.

MÉTODO DE RESOLUCIÓN
El método que se utiliza para la resolución de funciones cuadráticas es el siguiente:
"""

cuadratica_2 = """
El eje de simetría es una recta vertical, paralela al eje y,
que atraviesa la gráfica de manera que cada rama de ésta, separada por el eje,
es el “reflejo” de la otra, asumiendo la idea de que éste simula un espejo. 
El eje de simetría intersecta a la parábola en el vértice y al eje X en el 
valor x que es la abscisa del vértice. La fórmula del valor x mencionado,
conocida como Ecuación del Eje de Simetría es:

x=  (-b)/2a



VÉRTICE
Al esbozar la gráfica de la función cuadrática: 
f(x) = ax2 + bx + c, a ≠ 0, a, b, c ∈ IR, observamos que, dependiendo de la
orientación de la parábola, esta presenta un punto en el plano cartesiano,
que es mínimo si se abre hacia arriba (cóncava), o máximo si se abre 
hacia abajo (convexa), este punto se denomina vértice de la parábola y se puede
determinar a través de la expresión:
"""

cuadratica_3 = """PROCESO ALGEBRAICO PARA DETERMINAR SI UNA FUNCIÓN
POSEE INTERSECCIONES CON EL EJE x

Algebraicamente, se puede determinar rápidamente si una función tiene, o no,
intersecciones con el eje x. Para ello, basta analizar el signo del DISCRIMINANTE.
"""
raiz_cuadrada_1 = """FUNCIÓN RAÍZ CUADRADA

La función raíz cuadrada está dada por la ecuación f(x)= √x, y solo tiene sentido 
para los valores de x que cumplan con la condición, ya que en el conjunto de los 
números reales las raíces de índice par con radicando negativo, no están definidas. 
Su expresión analítica es algebraica irracional, su curva es la mitad de una parábola.

Ejemplos:
	f(x)= √(x-3)
	f(x)= √(2x+3)
	f(x)= √(x+2)+1

Dominio: Formado por los x ≥ 0
Rango: Formado por los y ≥ 0
Punto de corte con el eje x: x = 0


El gráfico de la función raíz cuadrada es:
"""
raiz_cuadrada_2 = """A este gráfico se pueden aplicar traslaciones horizontales, hacia 
la derecha si hacemos x − 1 y hacia la izquierda si hacemos x + 1. También se pueden 
aplicar traslaciones verticales, se desplaza hacia arriba si se suman constantes positivas, 
mientras que se desplaza hacia abajo si se suman constantes negativas."""


raiz_cuadrada_3 = """Si se multiplica la función por una constante negativa, la función raíz 
cuadrada se refleja con respecto al eje 𝑥."""

exponencial_1 = """FUNCIÓN EXPONENCIAL

Las funciones exponenciales son aquellas que tienen la variable independiente x en el exponente 
de una potencia. Es decir, son de la siguiente forma:

f(x)=a^x
Donde a es un número real positivo y diferente de 1.

Algunos ejemplos de funciones exponenciales: 
f(x)=3^x
f(x)=4^(-x)
f(x)=〖(1/2)〗^x


PROPIEDADES
El dominio de una función exponencial son todos los números reales o, dicho con otras 
palabras, una función exponencial existe por cualquier valor de x.


La función solo toma valores positivos, por lo tanto, el rango de una función exponencial 
son todos los números reales positivos.

Toda función exponencial es una función continua e inyectiva a la vez.

Si la función no está trasladada, cualquier función exponencial pasa por el punto (0,1). 
Porque la función evaluada en el cero siempre da como resultado uno.

Asimismo, el valor de una función exponencial en x=1 es igual a la base.

La inversa de la función exponencial es la función logarítmica. Por tanto, las gráficas 
de una función exponencial y una función logarítmica son simétricas respecto de la recta 
y=x si ambas poseen la misma base.

GRÁFICA
"""
exponencial_2 = """La función por la derecha sigue creciendo hasta el infinito, en cambio, la función por la 
izquierda va decreciendo, pero nunca llega a 0. Aunque se acerca mucho, nunca lo llega a tocar. 
Eso quiere decir que la recta y=0 (el eje de las abscisas) es una asíntota horizontal."""


logaritmica_1 = """FUNCIÓN LOGARÍTMICA
Una función logarítmica es aquella que se expresa como log_a⁡x, siendo a la base de esta función, 
que ha de ser positiva y distinta de 1.


Ejemplos: 
log_3⁡〖(2x+4)〗
log⁡x
log_(1/2)⁡〖(x+2)〗


PROPIEDADES
Las propiedades generales de la función logarítmica se deducen a partir de las de su inversa, 
la función exponencial. Así, se tiene que:

La función logarítmica sólo existe para valores de x positivos, sin incluir el cero. Por tanto, 
su dominio son los números reales positivos mayores que 0.

El dominio pertenece a cualquier elemento del conjunto de los números reales.

En el punto x = 1, la función logarítmica se anula, ya que loga 1 = 0, en cualquier base.

La función logarítmica de la base es siempre igual a 1.

Finalmente, la función logarítmica es continua, y es creciente para a > 1 y decreciente 
para a < 1.


GRÁFICA
"""

logaritmica_2 = """Esta es la gráfica de la función logarítmica y = log 10 x


La función logarítmica, puede ser cambiada en k unidades verticalmente y h unidades 
horizontalmente con la ecuación y = log b ( x + h ) + k .


CAMBIO VERTICAL
Si k > 0, la gráfica se desplazaría k unidades hacia arriba.
Si k < 0, la gráfica se desplazaría k unidades hacia abajo.

CAMBIO HORIZONTAL
Si h > 0, la gráfica se desplazaría h unidades a la izquierda.
Si h < 0, la gráfica se desplazaría h unidades a la derecha.
"""
seno_1  = """FUNCIÓN SENO

La función seno de un ángulo α es una función trigonométrica cuya fórmula se define como la 
razón entre el cateto opuesto y la hipotenusa de un triángulo rectángulo 
(triángulo con un ángulo recto).

Ejemplos:

〖F(x)= 2sin〗⁡x
〖F(x)= sin〗⁡x
〖F(x)= sin〗⁡2x

El signo de la función seno depende del cuadrante en el que se encuentre el ángulo: si el ángulo 
está dentro del primero o segundo cuadrantes el seno será positivo, por contra, si el ángulo 
cae en el tercero o cuarto cuadrante el seno será negativo.
"""
seno_2 = """REPRESENTACIÓN GRÁFICA
Al representar la función seno gráficamente se obtiene:"""

seno_3 = """
Como se puede ver en la gráfica, los valores de las imágenes de la función seno siempre 
están entre +1 y -1, es decir, está acotada superiormente por +1 e inferiormente por -1. Además, 
los valores se van repitiendo cada 360 grados (2π radianes), por lo que se trata de una función 
periódica cuyo periodo es 360º.


PROPIEDADES DE LA FUNCIÓN SENO
La función seno tiene las siguientes características:

El dominio de la función seno son todos los números reales ya que, como se ve en la gráfica, 
la función existe por cualquier valor de la variable independiente x.

El recorrido o rango de la función seno va desde -1 hasta 1 (ambos incluidos).

Este tipo de función trigonométrica tiene un único punto de corte con el eje de las ordenadas 
(eje Y) en el punto (0,0).


PERIODO Y AMPLITUD
La función seno es una función periódica, o sea, sus valores se van repitiendo según una frecuencia. 
Además, los valores máximos y mínimos entre los que oscila depende de su amplitud. 
Por lo tanto, dos rasgos que determinan la función seno son su periodo y su amplitud: 
Este tipo de función trigonométrica tiene un único punto de corte con el eje de las ordenadas 
(eje Y) en el punto (0,0).

El periodo de la función seno es la distancia entre dos puntos en los que se repite la gráfica.

La amplitud de la función seno es equivalente al coeficiente de delante del término seno.
"""

