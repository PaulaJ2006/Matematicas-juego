import numpy as np
import matplotlib.pyplot as plt
import random


def main(vidas):
    global enemigos, jumpping, timeintheair, p
    ranyi,ranyf = -10,11 #coordenadas plano
    xi, xf, yi, yf = 0, 1, 0, 1 #vértices cuadrado
    posy, posyf = 8,9 #coordenadas triangulo
    enemigos = [[posy,posyf]]
    timeintheair = 0
    p = 0
    jumpping = False
    actualizar_posicion(xi,xf,yi,yf, ranyi, ranyf, posy, posyf, vidas)
    plt.show()


def funcion_cuadratica(x, a, b, c):
    return (a*(x**2) + b*x + c-5)

def dibujar_plano(ranyi, ranyf):
    #Se definen arreglos de valores que van desde -10 hasta 10 
    y_values = np.arange(ranyi, ranyf, 1)
    x_values = np.arange(-10, 11, 1)
    #Se ponen los números que van en el plano tanto en x  como en y
    plt.yticks(np.arange(ranyi, ranyf, 1))
    plt.xticks(np.arange(-10, 11, 1))
    #límite de lo que se va a mostrar visualmente
    plt.ylim(ranyi, ranyf)
    plt.xlim(-10, 10)
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

def dibujarenemigos(amount, posy, posyf, yi, yf):
    global enemigos
    if amount == 1:
        posy = yi + 10
        posyf = yf + 10
        if posy - enemigos[-1][0] > 10:
            enemigos.append([posy,posyf])
        
    else:
        posy = yi + 10
        posyf = yf + 10
        if posy - enemigos[-1][0] > 10:

            enemigos.append([posy,posyf])
            posy = yi + 11
            posyf = yf + 11
            enemigos.append([posy,posyf])
    
    for i in range(len (enemigos)):
        y_values = []
        y_values.append(enemigos[i][0])
        y_values.append(enemigos[i][1])
        y_values.append((enemigos[i][0]+enemigos[i][1])/2)
        y_values.append(enemigos[i][0])
        x_values = []
        x_values.append(0)
        x_values.append(0)
        x_values.append(1)
        x_values.append(0)
        plt.plot(x_values, y_values, color="yellow")

def gameover():
    plt.pause(5)
    plt.clf()
    plt.text(0.2, 0.5, "GAME OVER", color="red", fontsize=30, fontweight="bold")
    plt.pause(5)
    plt.close() 


def actualizar_posicion(xi,xf, yi,yf, ranyi, ranyf, posy, posyf, vidas):
    global jumpping, timeintheair, enemigos, p
    plt.ion()
    plt.gcf().canvas.mpl_connect("key_press_event", saltar)
    while True:
        plt.clf()  # Limpia la figura
        ranyi += 1
        ranyf += 1
        plt.text(4, p+5, 'Vidas: ' + str(vidas), color="black", fontsize=12    )
        dibujar_plano(ranyi, ranyf)
        if jumpping and xi == 0:          
            xi += 2.2
            xf += 2.2
            jumpping = False
        if xi > 0:
            timeintheair += 1
        if timeintheair > 3:
            xi -= 2.2
            xf -= 2.2 
            jumpping = False
            timeintheair = 0
        dibujar_personaje(xi, xf, yi, yf, 'red')  # Dibuja el cuadrado
        amount = random.randint(1,2)
        dibujarenemigos(amount,posy, posyf, yi, yf)
        if enemigos[-1][0] == yi and enemigos[-1][1] == yf and xi == 0:
            vidas -= 1
        if enemigos[-1][0] == yi and enemigos[-1][1] == yf and xi == 0 and vidas == 0:
            plt.text(4, p+5, 'Vidas: ' + str(vidas), color="black", fontsize=12    )
            p += 5
            x_valuesfunction = np.linspace(-10, 10, 400)
            y_valuesfunction = funcion_cuadratica(x_valuesfunction, 2, -1, p)
            plt.plot(x_valuesfunction, y_valuesfunction, color="green",)    
            plt.text(3, p-8, 'Puntaje: ' + str(p), color="brown", fontsize=12)  
            plt.text(-7, p+3, f"2x^2-x+{p}", color="brown", fontsize=12) 
            h = -1/(2*2)
            k = funcion_cuadratica(h, 2, -1, p+5)
            plt.text(-9, p+5, f'h={h}, k={k} ', color="purple", fontsize=12)
            gameover()
            break
        else:
            p += 1
            x_valuesfunction = np.linspace(-10, 10,400)
            y_valuesfunction = funcion_cuadratica(x_valuesfunction, 2, -1, p)
            plt.plot(x_valuesfunction, y_valuesfunction, color="green",)    
            plt.text(3, p-8, 'Puntaje: ' + str(p), color="brown", fontsize=12)  
            plt.text(-7, p+3, f"2x^2-x+{p}", color="brown", fontsize=12) 
            h = -1/(2*2)
            k = funcion_cuadratica(h, 2, -1, p+5)
            plt.text(-9, p+5, f'h={h}, k={k} ', color="purple", fontsize=12)
        plt.draw()  # Actualiza la figura
        plt.pause(0.1)  # Pausa para crear la animación
        yi += 1  # Mueve el cuadrado hacia la derecha
        yf += 1  # Mueve el cuadrado hacia la derecha
    plt.ioff()  # Desactiva el modo interactivo
    plt.show()  # Muestra la figura final  





if __name__ == "__main__":
    vidas = 3
    main(vidas)