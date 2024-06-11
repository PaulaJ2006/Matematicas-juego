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
#___________________________imagenes preguntas____________________________________

imagen_pregunta_1_raiz = ctk.CTkImage(light_image=Image.open("imagen_pregunta_1_raiz.png"), 
                                dark_image=Image.open("imagen_pregunta_1_raiz.png"),
                                size = (300,300))

imagen_pregunta_2_raiz = ctk.CTkImage(light_image=Image.open("imagen_pregunta_2_raiz.png"),
                                dark_image=Image.open("imagen_pregunta_2_raiz.png"),
                                size = (300,300))

imagen_pregunta_3_raiz = ctk.CTkImage(light_image=Image.open("imagen_pregunta_3_raiz.png"),
                                dark_image=Image.open("imagen_pregunta_3_raiz.png"),
                                size = (300,300))

imagen_pregunta_2_seno = ctk.CTkImage(light_image=Image.open("imagen_pregunta_2_seno.png"),
                                dark_image=Image.open("imagen_pregunta_2_seno.png"),
                                size = (300,300))

imagen_pregunta_3_seno = ctk.CTkImage(light_image=Image.open("imagen_pregunta_3_seno.png"),
                                dark_image=Image.open("imagen_pregunta_3_seno.png"),
                                size = (300,300))

imagen_pregunta_1_exponencial = ctk.CTkImage(light_image=Image.open("imagen_pregunta_1_exponencial.png"),
                                dark_image=Image.open("imagen_pregunta_1_exponencial.png"),
                                size = (300,300))

imagen_pregunta_2_exponencial = ctk.CTkImage(light_image=Image.open("imagen_pregunta_2_exponencial.png"),
                                dark_image=Image.open("imagen_pregunta_2_exponencial.png"),
                                size = (300,300))

imagen_pregunta_1_logaritmica = ctk.CTkImage(light_image=Image.open("imagen_pregunta_1_logaritmica.png"),
                                dark_image=Image.open("imagen_pregunta_1_logaritmica.png"),
                                size = (300,300))

imagen_pregunta_3_logaritmica = ctk.CTkImage(light_image=Image.open("imagen_pregunta_3_logaritmica.png"),
                                dark_image=Image.open("imagen_pregunta_3_logaritmica.png"),
                                size = (300,300))

#____________________________________textos_________________________________________

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
mientras que se desplaza hacia abajo si se suman constantes negativas.
"""

raiz_cuadrada_3 = """Si se multiplica la función por una constante negativa, la función raíz 
cuadrada se refleja con respecto al eje 𝑥."""

exponencial_1 = """

FUNCIÓN EXPONENCIAL

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

GRÁFICA"""

exponencial_2 = """La función por la derecha sigue creciendo hasta el infinito, en cambio, la función por la 
izquierda va decreciendo, pero nunca llega a 0. Aunque se acerca mucho, nunca lo llega a tocar. 
Eso quiere decir que la recta y=0 (el eje de las abscisas) es una asíntota horizontal.

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
Este tipo de función trigonométrica tiene un único punto de corte con el eje de las ordenadas 
(eje Y) en el punto (0,0).

El periodo de la función seno es la distancia entre dos puntos en los que se repite la gráfica.

La amplitud de la función seno es equivalente al coeficiente de delante del término seno.
"""
#------------------------------pregunta 1 lineal--------------------------------
pregunta_1_lineal = """1. Halle la pendiente y el intersecto de la recta: ax + by + cc =  0"""
opcion_1_lineal = """Pendiente = a, intersecto = cPendiente = a, intersecto = c"""
opcion_2_lineal = """Pendiente = -a/b, intersecto = -c/b"""
opcion_3_lineal = """Pendiente = a/b, intersecto = c/b"""

#------------------------------pregunta 2 lineal--------------------------------
pregunta_2_lineal = """2. Un recipiente vacío comienza a llenarse con agua a ritmo constante.
Al cabo de un minuto la altura del nivel del agua es de 3cm. A los dos minutos, de 6cm, y así,
sucesivamente.
Determine la función que representa la altura del agua en función del tiempo x:"""

opcion_1_2_lineal = """y = 3x """
opcion_2_2_lineal = """y = 3x-2"""
opcion_3_2_lineal = """Datos insuficientes""" 

#------------------------------pregunta 3 lineal--------------------------------
pregunta_3_lineal = """3. Antonio va a comprarse un teléfono móvil y está estudiando la oferta de dos 
compañías distintas: La compañía A le ofrece pagar 0,2$ por el establecimiento de la llamada y 0,15$ 
por cada minuto de llamada. La compañía B le ofrece pagar 0,5$ por el establecimiento de la llamada y 
0,05$ por cada minuto de llamada. Calcular cuándo es más recomendable una compañía u otra en función 
del tiempo de duración de una llamada, e incluso cuando las dos tienen el mismo coste:
"""
opcion_1_3_lineal = """guales con 2 minutos, con menos de 2 minutos conviene A, con más de 2 minutos 
conviene B"""
opcion_2_3_lineal = """Iguales con 4 minutos, con menos de 4 minutos conviene A, con más de 2 minutos 
conviene B"""
opcion_3_3_lineal = """guales con 3 minutos, con menos de 3 minutos conviene A, con más de 3 minutos 
conviene B""" 

#------------------------------pregunta 1 cuadratica--------------------------------

pregunta_1_cuadratica = """1. Determinar dominio, rango y cortes de la función: 
3x^2 - 18x + 10"""
opcion_1_cuadratica = """A)	Dominio: R, Rango: y > -17, Corte y: (0, -10), 
corte x : (9+(51)^(1/2))/ 3),0)"""
opcion_2_cuadratica = """B)	Dominio: R, Rango: y < -17, Corte y: (10, 0), corte x: no tiene"""
opcion_3_cuadratica = """C)	Dominio: R, Rango: y > -17, Corte y: (0, 10), 
Cortes x: (9+(51)^(1/2))/ 3),0) y (9+-(51)^(1/2))/ 3),0)"""

#------------------------------pregunta 2 cuadratica--------------------------------

pregunta_2_cuadratica = """2. En un medio de cultivo se introdujeron 500 bacterias que comenzaron a 
reproducirse al cabo de cierto tiempo se modificó el medio y el número de bacterias comenzó a 
disminuir. Se supone que la cantidad de bacterias, al cabo de x minutos, está dada por la fórmula:
y = -x^2 + 40X + 500

Determinar en cuánto tiempo se alcanzó la población máxima y cuál fue dicha cantidad:"""
opcion_1_2_cuadratica = """Tiempo: 40 minutos, cantidad  de bacterias = 3700"""
opcion_2_2_cuadratica = """Tiempo: 20 minutos, cantidad de  bacterias = 900"""
opcion_3_2_cuadratica = """No se puede calcular"""

#------------------------------pregunta 3 cuadratica--------------------------------

pregunta_3_cuadratica = """
3. En un medio de cultivo se introdujeron 500 bacterias que comenzaron a reproducirse
al cabo de cierto tiempo se modificó el medio y el número de bacterias comenzó a disminuir.
Se supone que la cantidad de bacterias, al cabo de x minutos, está dada por la fórmula: 
y = -x^2 + 40X + 500
Se extingue la población de bacterias, cuándo """

opcion_1_3_cuadratica = """Sí, a los -10 minutos y a los 50 minutos"""
opcion_2_3_cuadratica = """No se extingue, dicha población solo crece"""
opcion_3_3_cuadratica = """Sí, a los 50 minutos."""

#------------------------------pregunta 1 raiz--------------------------------
pregunta_1_raiz = """1.	Hallar dominio y corte con eje x de la función.
aqui imagen"""
opcion_1_1_raiz = """Dominio: -1<x<0  or x>0, corte x: (-1,0)"""
opcion_2_1_raiz = """Dominio:  X>-1, corte x: (0,*-1)"""
opcion_3_1_raiz = """Dominio:  R-{0}, corte x: (0,*-1)"""

#------------------------------pregunta 2 raiz--------------------------------
pregunta_2_raiz = """2.	Hallar la inversa de la función:
aqui imagen"""
opcion_1_2_raiz = """No tiene inversa"""
opcion_2_2_raiz = """(1 + y) / (y-1)"""
opcion_3_2_raiz = """(1+y^2)/(y^2-1)"""

#------------------------------pregunta 3 raiz--------------------------------
pregunta_3_raiz = """3.	Encontrar el área de la cometa en función de x
aqui imagen"""
opcion_1_3_raiz = """No se puede"""
opcion_2_3_raiz = """x( (25-x^2)^(1/2) + (100-x^2)^(1/2))"""
opcion_3_3_raiz = """x((5-x^2)^(1/2) + (10-x^2)^(1/2))"""
#-----------------------------pregunta 1 exponencial--------------------------
pregunta_1_exponencial = """1.	Halle los cortes de la función 
aqui imagen"""
opcion_1_1_exponencial= """Corte y: (0, e^2), corte x: (-e^2/3,0)"""
opcion_2_1_exponencial= """No tiene cortes"""
opcion_3_1_exponencial = """Corte y: (-e^2/3,0), corte x: (0, e^2)"""

#-----------------------------pregunta 2 exponencial--------------------------
pregunta_2_exponencial = """2.	Hallar la inversa de tanh x: 
#aqui va imagen"""
opcion_1_2_exponencial= """No se puede calcular"""
opcion_2_2_exponencial= """(½)* (ln(1+x)/(1-x))"""
opcion_3_2_exponencial = """(ln(1+x)/(1-x))"""

#-----------------------------pregunta 3 exponencial--------------------------
pregunta_3_exponencial = """3. La población futura de un pueblo se puede 
aproximar mediante la fórmula y = 8000(1,4)^(0,2t), donde t es el número 
de años transcurridos.  
¿A los cuántos años la población será de 15680 habitantes??"""
opcion_1_3_exponencial= """Información insuficiente"""
opcion_2_3_exponencial= """A los 5 años"""
opcion_3_3_exponencial = """A los 10 años"""

#-----------------------------pregunta 1 logaritmica--------------------------
pregunta_1_logaritmica = """1.	Hallar el dominio, el rango y el corte en Y 
aqui imagen"""
opcion_1_1_logaritmica= """Dominio: R-{-2,2}, Rango: R corte y: (0, log4)"""
opcion_2_1_logaritimica= """Dominio: R-{4,-4}, Rango: R, corte y: (log4, 0)"""
opcion_3_1_logaritmica = """Dominio: R-, Rango: R, corte y:  (log4, 0) """

#-----------------------------pregunta 2 logaritmica--------------------------
pregunta_2_logaritmica = """2.	Hallar la inversa de la función 2logx: """
opcion_1_2_logaritmica= """No tiene por ser logarítmica"""
opcion_2_2_logaritmica= """10^x"""
opcion_3_2_logaritmica = """10^(x/2)"""

#-----------------------------pregunta 3 logaritmica-----------------------
pregunta_3_logaritmica = """3.	Una variedad de peces fue introducida en el 
océano pacífico. El siguiente modelo predice en un tiempo t de meses cuántos 
P peces hay:
AQUI IMAGEN"""
pregunta_3_logaritmica_p2 = """¿Cuántos peces habrá para 18 meses?"""
opcion_1_3_logaritmica= """6400""" 
opcion_2_3_logaritmica= """Información insuficiente"""
opcion_3_3_logaritmica = """10000"""

#-----------------------------pregunta 1 seno--------------------------
pregunta_1_seno = """1.	Dominio y rango de la función sin(x) """
opcion_1_1_seno= """Dominio: x > 0, rango: R"""
opcion_2_1_seno= """Dominio: R, rango: R"""
opcion_3_1_seno = """Dominio: R, rango: [-1, 1] """

#-----------------------------pregunta 2 seno--------------------------
pregunta_2_seno = """2.	Según la gráfica de la función sin x, 
dicha función que simetría tiene.  
#aqui va imagen"""
opcion_1_2_seno= """Es par debido a que tiene simetría en el 
eje Y"""
opcion_2_2_seno= """Es impar porque tiene simetría con el origen"""
opcion_3_2_seno = """Es impar porque tiene simetría con el eje Y"""

#-----------------------------pregunta 3 seno--------------------------
pregunta_3_seno = """Una Cometa se queda atascada en la rama más alta 
de un árbol si la cuerda de la Cometa mide 25 m y forma un ángulo de 
37° con el suelo, estime la altura del árbol encontrando la distancia 
que hay entre la cometa y el suelo
AQUI IMAGEN"""
opcion_1_3_seno= """Datos insuficientes, falta un lado para 
realizar el teorema de Pitágoras"""
opcion_2_3_seno= """10.5m"""
opcion_3_3_seno = """15m"""