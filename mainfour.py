import numpy as np
import matplotlib.pyplot as plt
import random



def main(vidas):
    global enemigos, jumpping, timeintheair, p
    ranxi,ranxf = -10,11 #coordenadas plano
    xi, xf, yi, yf = 0, 1, 0, -1 #vértices cuadrado
    posx, posf = 8,9 #coordenadas triangulo
    enemigos = [[posx,posf]]
    timeintheair = 0
    p=0
    jumpping = False
    actualizar_posicion(xi,xf,yi,yf, ranxi, ranxf, posx, posf, vidas)
    plt.show()
 
def funcion_exponencial(x,t):
    return ((0.5 **(x-p+7)) + t)*-1

def dibujar_plano(ranxi, ranxf):
    #Se definen arreglos de valores que van desde -10 hasta 10 
    x_values = np.arange(ranxi, ranxf, 1)
    y_values = np.arange(-10, 11, 1)
    #Se ponen los números que van en el plano tanto en x  como en y
    plt.xticks(np.arange(ranxi, ranxf, 1))
    plt.yticks(np.arange(-10, 11, 1))
    #límite de lo que se va a mostrar visualmente
    plt.xlim(ranxi, ranxf)
    plt.ylim(-10, 10)
    #Se pone el título del juego y de los ejes
    plt.title("Descartico")
    plt.xlabel("x")
    plt.ylabel("y")     
    #Se activa cuadricula
    plt.grid(True)
    #Se dibujan la abscisa y la ordenada
    plt.plot(x_values, np.zeros(21), color="blue")
    plt.plot(np.zeros(21), y_values, color="blue")

def dibujar_personaje(xi, xf, yi, yf, color):
    x_values = [xi, xf, xf, xi, xi]
    y_values = [yi, yi, yf, yf, yi ]
    plt.plot(x_values, y_values, color=color)


def saltar(event):
    global jumpping
    if event.key == ' ':
        jumpping = True

def dibujarenemigos(amount, posx, posf, xi, xf):

    global enemigos
    if amount == 1:
        posx = xi + 7
        posf = xf + 7
        if posx - enemigos[-1][0] > 7:
            enemigos.append([posx,posf])
        
    else:
        posx = xi + 7
        posf = xf + 7
        if posx - enemigos[-1][0] > 7:

            enemigos.append([posx,posf])
            posx = xi + 8
            posf = xf + 8
            enemigos.append([posx,posf])
    
    for i in range(len (enemigos)):
        x_values = []
        x_values.append(enemigos[i][0])
        x_values.append(enemigos[i][1])
        x_values.append((enemigos[i][0]+enemigos[i][1])/2)
        x_values.append(enemigos[i][0])
        y_values = []
        y_values.append(0)
        y_values.append(0)
        y_values.append(-1)
        y_values.append(0)
        plt.plot(x_values, y_values, color="yellow")

def gameover():
    plt.pause(5)
    plt.clf()
    plt.text(0.2, 0.5, "GAME OVER", color="red", fontsize=30, fontweight="bold")
    plt.pause(5)
    plt.close() 


def actualizar_posicion(xi,xf, yi,yf, ranxi, ranxf, posx, posf, vidas):
    global jumpping, timeintheair, enemigos,p
    plt.ion()
    plt.gcf().canvas.mpl_connect("key_press_event", saltar)
    while True:
        plt.clf()  # Limpia la figura
        ranxi += 1
        ranxf += 1
        plt.text(ranxi+2, 8, 'Vidas: ' + str(vidas), color="black", fontsize=12    )
        dibujar_plano(ranxi, ranxf)
        if jumpping and yi == 0:          
            yi -= 2.2
            yf -= 2.2
            jumpping = False
        if yi < 0:
            timeintheair += 1
        if timeintheair > 3:
            yi += 2.2
            yf += 2.2 
            jumpping = False
            timeintheair = 0
        dibujar_personaje(xi, xf, yi, yf, 'red')  # Dibuja el cuadrado
        amount = random.randint(1,2)
        dibujarenemigos(amount,posx, posf, xi, xf)
        if enemigos[-1][0] == xi and enemigos[-1][1] == xf and yi == 0:
            vidas -= 1
        if enemigos[-1][0] == xi and enemigos[-1][1] == xf and yi == 0 and vidas == 0:
            plt.text(ranxi+2, 8, 'Vidas: ' + str(vidas), color="black", fontsize=12    )
            p += 8
            x_valuesfunction = np.linspace(ranxi, ranxf, 400)
            y_valuesfunction = funcion_exponencial(x_valuesfunction, -1)
            plt.plot(x_valuesfunction, y_valuesfunction, color="green",)    
            plt.text(ranxi + 10, -10, 'Puntaje: ' + str(p), color="brown", fontsize=12    )  
            plt.text(p-3, 4, f"-0.5^(x-{p})-3", color="brown", fontsize=12) 
            vidas -= 1
            gameover()
            break
        else:
            p += 1
            x_valuesfunction = np.linspace(ranxi, ranxf, 400)
            y_valuesfunction = funcion_exponencial(x_valuesfunction, 2)
            plt.plot(x_valuesfunction, y_valuesfunction, color="green",) 
            plt.text(ranxi + 10, -10, 'Puntaje: ' + str(p), color="brown", fontsize=12)  
            plt.text(p, 4, f"-0.5^(x-{p})+2", color="brown", fontsize=12)
        plt.draw()  # Actualiza la figura
        plt.pause(0.1)  # Pausa para crear la animación
        xi += 1  # Mueve el cuadrado hacia la derecha
        xf += 1  # Mueve el cuadrado hacia la derecha
    plt.ioff()  # Desactiva el modo interactivo
    plt.show()  # Muestra la figura final  








if __name__ == "__main__":
    vidas = 3
    main(vidas) 