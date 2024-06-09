from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
import variables

#----------------------------------ventanas---------------------------------------
#VENTANA PRINCIPAL
root = ctk.CTk()
root.geometry("1000x600")
root.resizable(0,0)
root.title("Descartico")
root._set_appearance_mode("light")
root.iconbitmap("descartico.ico")


#----------------------------------variables-------------------------------------
font_1 = ctk.CTkFont(family="Inherit", size=26, weight="bold")
font_2 = ctk.CTkFont(family="Cooper Black", size = 35, weight="bold")

info_window = None
jugar_window = None
ajustes_window = None
aprender_window = None
#----------------------------------funciones-------------------------------------
#-----------------------------VENTANA INFORMACION-------------------------------------

def mostrar_info():
    global info_window
    global definicion_funcion
    if info_window is None:
        info_window = ctk.CTkToplevel(root)
        info_window.geometry("1000x600")
        info_window.resizable(0, 0)
        info_window.title("Información")
        
        info_frame = ctk.CTkFrame(master=info_window, width=1000, height=600, corner_radius=10, fg_color="#D6EAF8", border_color="white", border_width=2)
        info_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        close_button = ctk.CTkButton(master=info_frame, text="Cerrar", font=(font_1,16), text_color="black", width=100, height=40, corner_radius=32, fg_color="white", hover_color="light blue", command=cerrar_info)
        close_button.place(relx=0.07, rely=0.04, anchor="center")

        frame_lectura = ctk.CTkScrollableFrame(master = info_frame,
                        width = 950,
                        height = 430,
                        fg_color = "light blue",
                        corner_radius = 30,
                        scrollbar_button_color = "beige",
                        orientation = "vertical"
                        )
        frame_lectura.place(relx = 0.5, rely = 0.5, anchor = "center")

        label_funcion_1 = ctk.CTkLabel(master = frame_lectura,
                                    text = variables.definicion_funcion,
                                    width = 910,
                                    height = 240,
                                    font = (font_1, 22),
                                    text_color = "black",
                                    fg_color="transparent",
                                    )
        label_funcion_1.pack(padx=5, pady=2, expand=True, anchor="n") 
        
        imagen_categoria_funciones = ctk.CTkLabel(master = frame_lectura, 
                                image = variables.imagen_tipos_funciones,
                                width = 800,
                                height = 800,
                                text = ""
                                )
        imagen_categoria_funciones.pack(padx=5, pady=2, expand=True, anchor="center")

        texto_funcion_inyectiva = ctk.CTkLabel(master = frame_lectura,
                                    text = variables.inyectiva,
                                    width = 910,
                                    height = 240,
                                    font = (font_1, 21),
                                    text_color = "black",
                                    fg_color="transparent",
                                    )
        texto_funcion_inyectiva.pack(padx=5, pady=2, expand=True, anchor="center")

        imagen_funcion_inyectiva = ctk.CTkLabel(master = frame_lectura, 
                                image = variables.funcion_inyectiva,
                                width = 800,
                                height = 800,
                                text=""
                                )
        imagen_funcion_inyectiva.pack(padx=5, pady=2, expand=True, anchor="center")

        texto_funcion_sobreyectiva = ctk.CTkLabel(master = frame_lectura, 
                                    text = variables.sobreyectiva,
                                    width = 910,
                                    height = 240,
                                    font = (font_1, 21),
                                    text_color = "black",
                                    fg_color="transparent",
                                    )
        texto_funcion_sobreyectiva.pack(padx=5, pady=2, expand=True, anchor="center")

        imagen_funcion_sobreyectiva = ctk.CTkLabel(master = frame_lectura, 
                                image = variables.funcion_sobreyectiva,
                                width = 800,
                                height = 800,
                                text=""
                                )
        imagen_funcion_sobreyectiva.pack(padx=5, pady=2, expand=True, anchor="center")

        texto_funcion_biyectiva = ctk.CTkLabel(master = frame_lectura, 
                                    text = variables.biyectiva,
                                    width = 910,
                                    height = 240,
                                    font = (font_1, 21),
                                    text_color = "black",
                                    fg_color="transparent",
                                    )
        texto_funcion_biyectiva.pack(padx=5, pady=2, expand=True, anchor="center")

        imagen_funcion_biyectiva = ctk.CTkLabel(master = frame_lectura, 
                                image = variables.funcion_biyectiva,
                                width = 800,
                                height = 800,
                                text=""
                                )  
        imagen_funcion_biyectiva.pack(padx=5, pady=2, expand=True, anchor="center")

        
    root.withdraw()



def cerrar_info():
    global info_window
    if info_window is not None:
        info_window.destroy()
        info_window = None
    root.deiconify()

def cerrar_aprender():
    global info_window
    if info_window is not None:
        info_window.destroy()
        info_window = None
    jugar()



#---------------------------------VENTANA JUGAR-----------------------------------------
def jugar():
    global jugar_window
    if jugar_window is None:
        jugar_window = ctk.CTkToplevel(root)
        jugar_window.geometry("1000x600")
        jugar_window.resizable(0, 0)
        jugar_window.title("Jugar")
        
        jugar_frame = ctk.CTkFrame(master=jugar_window,
                            width=1000, 
                            height=600, 
                            corner_radius=10, 
                            fg_color="#D6EAF8", 
                            border_color="white", 
                            border_width=2
                            )
        jugar_frame.place(relx=0.5, rely=0.5, anchor="center")

        nivel_1 = ctk.CTkFrame(master=jugar_frame,  
                            width=250, 
                            height=200, 
                            corner_radius=32, 
                            fg_color="white", 
                            border_width=3,
                            border_color="#8CE5FF"
                            )
        nivel_1.place(relx=0.2, rely=0.3, anchor="center")

        nivel_2 = ctk.CTkFrame(master=jugar_frame,
                            width=250, 
                            height=200, 
                            corner_radius=32, 
                            fg_color="white",
                            border_width=3,
                            border_color="#8CE5FF"
                            )
        nivel_2.place(relx=0.5, rely=0.3, anchor="center")

        nivel_3 = ctk.CTkFrame(master=jugar_frame,
                            width=250, 
                            height=200, 
                            corner_radius=32, 
                            fg_color="white",
                            border_width=3,
                            border_color="#8CE5FF"
                            )
        nivel_3.place(relx=0.8, rely=0.3, anchor="center")

        nivel_4 = ctk.CTkFrame(master=jugar_frame,
                            width=250, 
                            height=200, 
                            corner_radius=32, 
                            fg_color="white",
                            border_width=3,
                            border_color="#8CE5FF"
                            )
        nivel_4.place(relx=0.2, rely=0.7, anchor="center")
        
        nivel_5 = ctk.CTkFrame(master=jugar_frame,
                            width=250, 
                            height=200, 
                            corner_radius=32, 
                            fg_color="white",
                            border_width=3,
                            border_color="#8CE5FF"
                            )
        nivel_5.place(relx=0.5, rely=0.7, anchor="center")
        
        nivel_6 = ctk.CTkFrame(master=jugar_frame,
                            width=250, 
                            height=200, 
                            corner_radius=32, 
                            fg_color="white",
                            border_width=3,
                            border_color="#8CE5FF"
                            )
        nivel_6.place(relx=0.8, rely=0.7, anchor="center")

        close_button = ctk.CTkButton(master=jugar_frame,
                            text="Cerrar", 
                            font=(font_1, 16), 
                            text_color="black", 
                            width=95, height=40, 
                            corner_radius=32, 
                            fg_color="white", 
                            hover_color="light blue", 
                            command=cerrar_jugar)
        close_button.place(relx=0.06, rely=0.05, anchor="center")

        nivel_1_label = ctk.CTkLabel(master=nivel_1, 
                            text="""Nivel 1
Función Lineal""", 
                            font=(font_1, 18), 
                            text_color="black")
        nivel_1_label.place(relx=0.5, rely=0.1, anchor="n")

        nivel_2_label = ctk.CTkLabel(master=nivel_2, 
                            text="""Nivel 2
Funcion Cuadrática""", 
                            font=(font_1, 18), 
                            text_color="black",
                            )
        nivel_2_label.place(relx=0.5, rely=0.1, anchor="n")
        
        nivel_3_label = ctk.CTkLabel(master=nivel_3, 
                            text="""Nivel 3
Función Raíz Cuadrada""",
                            font=(font_1, 18), 
                            text_color="black",
                            )
        nivel_3_label.place(relx=0.5, rely=0.1, anchor="n")

        nivel_4_label = ctk.CTkLabel(master=nivel_4, 
                            text="""Nivel 4
Función Exponencial""", 
                            font=(font_1, 18), 
                            text_color="black",
                            )
        nivel_4_label.place(relx=0.5, rely=0.1, anchor="n")

        nivel_5_label = ctk.CTkLabel(master=nivel_5, 
                            text="""Nivel 5 
Función Logaritmica""", 
                            font=(font_1, 18), 
                            text_color="black",
                            )
        nivel_5_label.place(relx=0.5, rely=0.1, anchor="n")

        nivel_6_label = ctk.CTkLabel(master=nivel_6, 
                            text="""Nivel 6 
Función Seno""",      
                            font=(font_1, 18), 
                            text_color="black",
                            )
        nivel_6_label.place(relx=0.5, rely=0.1, anchor="n")

        boton_jugar_nivel_1 = ctk.CTkButton(master=nivel_1,
                            text="Jugar", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED",
                            )
        boton_jugar_nivel_1.place(relx=0.5, rely=0.5, anchor="center")

        boton_aprender_nivel_1 = ctk.CTkButton(master=nivel_1, 
                            text="Aprender", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED",
                            command=lambda: asignar_parametros(1)
                            )
        boton_aprender_nivel_1.place(relx=0.5, rely=0.7, anchor="center")

        boton_jugar_nivel_2 = ctk.CTkButton(master=nivel_2, 
                            text="Jugar", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED", 
                            )
        boton_jugar_nivel_2.place(relx=0.5, rely=0.5, anchor="center")

        boton_aprender_nivel_2 = ctk.CTkButton(master=nivel_2, 
                            text="Aprender", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED",
                            command=lambda: asignar_parametros(2) 
                            )
        boton_aprender_nivel_2.place(relx=0.5, rely=0.7, anchor="center")

        boton_jugar_nivel_3 = ctk.CTkButton(master=nivel_3, 
                            text="Jugar", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED", 
                            )
        boton_jugar_nivel_3.place(relx=0.5, rely=0.5, anchor="center")

        boton_aprender_nivel_3 = ctk.CTkButton(master=nivel_3, 
                            text="Aprender", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED",
                            command=lambda: asignar_parametros(3) 
                            )
        boton_aprender_nivel_3.place(relx=0.5, rely=0.7, anchor="center")

        boton_jugar_nivel_4 = ctk.CTkButton(master=nivel_4, 
                            text="Jugar", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED", 
                            )
        boton_jugar_nivel_4.place(relx=0.5, rely=0.5, anchor="center")

        boton_aprender_nivel_4 = ctk.CTkButton(master=nivel_4, 
                            text="Aprender", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED", 
                            command=lambda: asignar_parametros(4)
                            )
        boton_aprender_nivel_4.place(relx=0.5, rely=0.7, anchor="center")

        boton_jugar_nivel_5 = ctk.CTkButton(master=nivel_5, 
                            text="Jugar", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED", 
                            )
        boton_jugar_nivel_5.place(relx=0.5, rely=0.5, anchor="center")

        boton_aprender_nivel_5 = ctk.CTkButton(master=nivel_5, 
                            text="Aprender", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED", 
                            command=lambda: asignar_parametros(5)
                            )
        boton_aprender_nivel_5.place(relx=0.5, rely=0.7, anchor="center")

        boton_jugar_nivel_6 = ctk.CTkButton(master=nivel_6, 
                            text="Jugar", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED", 
                            )
        boton_jugar_nivel_6.place(relx=0.5, rely=0.5, anchor="center")

        boton_aprender_nivel_6 = ctk.CTkButton(master=nivel_6, 
                            text="Aprender", 
                            font=(font_1, 18), 
                            text_color="black", 
                            width=200, 
                            height=30, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED",
                            command=lambda: asignar_parametros(6) 
                            )
        boton_aprender_nivel_6.place(relx=0.5, rely=0.7, anchor="center")

    root.withdraw()

def cerrar_jugar():
    global jugar_window
    if jugar_window is not None:
        jugar_window.destroy()
        jugar_window = None
    root.deiconify()

def aprender(valor):
    global aprender_window
    if aprender_window is None:
        aprender_window = ctk.CTkToplevel(root)
        aprender_window.geometry("1000x600")
        aprender_window.resizable(0, 0)
        aprender_window.title("Aprender")

        aprender = ctk.CTkFrame(master=aprender_window, 
                                    width=1000, 
                                    height=600, 
                                    corner_radius=10, 
                                    fg_color="#D6EAF8", 
                                    border_color="white", 
                                    border_width=2)
        aprender.place(relx=0.5, rely=0.5, anchor="center")

        frame_aprender = ctk.CTkScrollableFrame(master = aprender,
                        width = 950,
                        height = 430,
                        corner_radius = 30,
                        fg_color = "light blue",
                        scrollbar_button_color = "beige",
                        orientation = "vertical"
                        )
        frame_aprender.place(relx = 0.5, rely = 0.5, anchor = "center")

        close_button_aprender = ctk.CTkButton(master=aprender, text="Cerrar", font=(font_1,16), text_color="black", width=100, height=40, corner_radius=32, fg_color="white", hover_color="light blue", command=cerrar_aprender)
        close_button_aprender.place(relx=0.07, rely=0.04, anchor="center")

        if valor == 1:
            label_funcion_lineal = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.lineal,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_lineal.pack(padx=5, pady=2, expand=True, anchor="n")

        elif valor == 2:
            label_funcion_cuadratica_1 = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.cuadratica_1,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_cuadratica_1.pack(padx=2, pady=1, expand=True, anchor="n")

            imagen_metodo_resolucion_cuadratica = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.metodo_resolucion_cuadratica,
                                width = 400,
                                height = 200,
                                text = ""
                                )
            imagen_metodo_resolucion_cuadratica.pack(padx=2, pady=1, expand=True, anchor="center")

            label_funcion_cuadratica_2 = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.cuadratica_2,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_cuadratica_2.pack(padx=2, pady=1, expand=True, anchor="n")

            imagen_cuadratica_2 = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.imagen_2_cuadratica,
                                width = 400,
                                height = 200,
                                text = ""
                                )
            imagen_cuadratica_2.pack(padx=2, pady=1, expand=True, anchor="center")

            label_funcion_cuadratica_3 = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.cuadratica_3,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_cuadratica_3.pack(padx=2, pady=1, expand=True, anchor="n")

            imagen_cuadratica_3 = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.imagen_3_cuadratica,
                                width = 290,
                                height = 70,
                                text = ""
                                )
            imagen_cuadratica_3.pack(padx=2, pady=1, expand=True, anchor="center")

            imagen_cuadratica_4 = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.imagen_4_cuadratica,
                                width = 500,
                                height = 300,
                                text = ""
                                )
            imagen_cuadratica_4.pack(padx=2, pady=1, expand=True, anchor="center")

        elif valor == 3:
            label_funcion_raiz = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.raiz_cuadrada_1,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_raiz.pack(padx=5, pady=2, expand=True, anchor="n")
            imagen_raiz_1 = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.imagen_1_raiz,
                                width = 400,
                                height = 200,
                                text = ""
                                )
            imagen_raiz_1.pack(padx=2, pady=1, expand=True, anchor="center")

            label_funcion_raiz_2 = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.raiz_cuadrada_2,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_raiz_2.pack(padx=5, pady=2, expand=True, anchor="n")

            imagen_raiz_2 = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.imagen_2_raiz,
                                width = 400,
                                height = 200,
                                text = ""
                                )
            imagen_raiz_2.pack(padx=2, pady=1, expand=True, anchor="center")

            label_funcion_raiz_3 = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.raiz_cuadrada_3,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_raiz_3.pack(padx=5, pady=2, expand=True, anchor="n")
            imagen_raiz_3 = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.imagen_3_raiz,
                                width = 400,
                                height = 200,
                                text = ""
                                )
            imagen_raiz_3.pack(padx=2, pady=1, expand=True, anchor="center")
        
        elif valor == 4:
            label_funcion_exponencial = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.exponencial_1,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_exponencial.pack(padx=5, pady=2, expand=True, anchor="n")

            imagen_exponencial_1 = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.imagen_1_exponencial,
                                width = 400,
                                height = 200,
                                text = ""
                                )
            imagen_exponencial_1.pack(padx=2, pady=1, expand=True, anchor="center")

            label_funcion_exponencial_2 = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.exponencial_2,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_exponencial_2.pack(padx=5, pady=2, expand=True, anchor="n")
        
        elif valor == 5:
            label_funcion_logaritmica = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.logaritmica_1,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_logaritmica.pack(padx=5, pady=2, expand=True, anchor="n")

            imagen_logaritmica_1 = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.imagen_1_logaritmica,
                                width = 400,
                                height = 200,
                                text = ""
                                )
            imagen_logaritmica_1.pack(padx=2, pady=1, expand=True, anchor="center")

            label_funcion_logaritmica_2 = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.logaritmica_2,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_logaritmica_2.pack(padx=5, pady=2, expand=True, anchor="n")
        
        elif valor == 6:
            label_funcion_seno = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.seno_1,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_seno.pack(padx=5, pady=2, expand=True, anchor="n")
            imagen_seno_1 = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.imagen_1_seno,
                                width = 400,
                                height = 200,
                                text = ""
                                )
            imagen_seno_1.pack(padx=2, pady=1, expand=True, anchor="center")

            label_funcion_seno_2 = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.seno_2,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_seno_2.pack(padx=5, pady=2, expand=True, anchor="n")

            imagen_seno_2 = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.imagen_2_seno,
                                width = 400,
                                height = 200,
                                text = ""
                                )
            imagen_seno_2.pack(padx=2, pady=1, expand=True, anchor="center")

            label_funcion_seno_3 = ctk.CTkLabel(master = frame_aprender,
                                        text = variables.seno_3,
                                        width = 910,
                                        height = 240,
                                        font = (font_1, 22),
                                        text_color = "black",
                                        fg_color="transparent",
                                        )
            label_funcion_seno_3.pack(padx=5, pady=2, expand=True, anchor="n")
            imagen_seno_3 = ctk.CTkLabel(master = frame_aprender, 
                                image = variables.imagen_3_seno,
                                width = 400,
                                height = 200,
                                text = ""
                                )
            imagen_seno_3.pack(padx=2, pady=1, expand=True, anchor="center")

    jugar_window.withdraw()


def asignar_parametros(numero):
    aprender(numero)
    
def cerrar_aprender():
    global aprender_window
    if aprender_window is not None:
        aprender_window.destroy()
        aprender_window = None
    if jugar_window is None:
        jugar()
    else:
        jugar_window.deiconify()
#--------------------------------------------frames------------------------------------------
frame_principal = ctk.CTkFrame(master = root, 
                                        width = 1000, 
                                        height = 600, 
                                        corner_radius = 10, 
                                        fg_color = "#D6EAF8", 
                                        border_color = "white", 
                                        border_width = 2
                                        )
frame_imagen = ctk.CTkFrame(master = frame_principal,
                                    width = 400,
                                    height = 400,
                                    corner_radius = 10,
                                    fg_color = "white",
                                    border_color = "black",
                                    border_width = 2
                                    )


#----------------------------------------------botones------------------------------------------
boton_info = ctk.CTkButton(master = frame_principal, 
                                    text="INFO", 
                                    font=font_1, 
                                    text_color="black",
                                    width=200, 
                                    height=90, 
                                    corner_radius=32, 
                                    fg_color="white",
                                    hover_color= "#A4FC6C",
                                    command = mostrar_info
                                    )

boton_jugar = ctk.CTkButton(master = frame_principal,
                                    text="JUGAR",
                                    font=font_1,
                                    text_color="black",
                                    width=200,
                                    height=90,
                                    corner_radius=32,
                                    fg_color="white",
                                    hover_color= "#FBF4B8",
                                    command= jugar
                                    )

#----------------------------------------------labels--------------------------------------------
titulo = ctk.CTkLabel(master = frame_imagen, 
                                text = "DESCARTICO", 
                                font = font_2, 
                                text_color = "red",
                                width = 200,
                                height = 90
                                )
imagen_ = ctk.CTkLabel(master = frame_imagen, 
                                image = variables.imagen,
                                width = 200,
                                height = 200
                                )

#----------------------------Posicionamiento--------------------------------
frame_principal.place(relx = 0.5, rely = 0.5, anchor="center")
frame_imagen.place(relx = 0.5, rely = 0.03, anchor = "n")
titulo.place(relx = 0.5, rely = 0.115, anchor = "center")
imagen_.place(relx = 0.5, rely = 0.55,  anchor = "center")
boton_info.place(relx = 0.05, rely = 0.83, anchor = "w")
boton_jugar.place(relx = 0.599, rely = 0.83, anchor = "e")



root.mainloop()