from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk

#----------------------------------ventanas---------------------------------------
#VENTANA PRINCIPAL
root = ctk.CTk()
root.geometry("1000x600")
root.resizable(0,0)
root.title("Descartico")
root._set_appearance_mode("light")
root.iconbitmap("descartico.ico")

#VENTANA INFO
info_window = None
jugar_window = None
ajustes_window = None
#----------------------------------funciones-------------------------------------
#VENTANA INFORMACION
def mostrar_info():
    global info_window
    if info_window is None:
        info_window = ctk.CTkToplevel(root)
        info_window.geometry("1000x600")
        info_window.resizable(0, 0)
        info_window.title("Información")
        
        info_frame = ctk.CTkFrame(master=info_window, width=1000, height=600, corner_radius=10, fg_color="#D6EAF8", border_color="white", border_width=2)
        info_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        info_label = ctk.CTkLabel(master=info_frame, text="Aquí va la información", font=font_1, text_color="black")
        info_label.place(relx=0.5, rely=0.5, anchor="center")
        
        close_button = ctk.CTkButton(master=info_frame, text="Cerrar", font=font_1, text_color="black", width=100, height=40, corner_radius=32, fg_color="white", hover_color="light blue", command=cerrar_info)
        close_button.place(relx=0.5, rely=0.9, anchor="center")
        
    root.withdraw()

def cerrar_info():
    global info_window
    if info_window is not None:
        info_window.destroy()
        info_window = None
    root.deiconify()

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
                            width=350, 
                            height=500, 
                            corner_radius=32, 
                            fg_color="white", 
                            border_width=3,
                            border_color="#8CE5FF"
                            )
        nivel_1.place(relx=0.3, rely=0.5, anchor="center")

        nivel_2 = ctk.CTkFrame(master=jugar_frame,
                            width=350, 
                            height=500, 
                            corner_radius=32, 
                            fg_color="white",
                            border_width=3,
                            border_color="#8CE5FF"
                            )
        nivel_2.place(relx=0.7, rely=0.5, anchor="center")
        
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
                            font=font_1, 
                            text_color="black")
        nivel_1_label.place(relx=0.5, rely=0.1, anchor="n")

        nivel_2_label = ctk.CTkLabel(master=nivel_2, 
                            text="""Nivel 2
Funcion Cuadrática""", 
                            font=font_1, 
                            text_color="black",
                            )

        nivel_2_label.place(relx=0.5, rely=0.1, anchor="n")

        boton_jugar_nivel_1 = ctk.CTkButton(master=nivel_1,
                            text="Jugar", 
                            font=(font_1, 24), 
                            text_color="black", 
                            width=200, 
                            height=50, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED",
                            )
        boton_jugar_nivel_1.place(relx=0.5, rely=0.4, anchor="center")

        boton_jugar_nivel_2 = ctk.CTkButton(master=nivel_2, 
                            text="Jugar", 
                            font=(font_1, 24), 
                            text_color="black", 
                            width=200, 
                            height=50, 
                            corner_radius=36, 
                            fg_color="#A6FFCD", 
                            hover_color="#A6FFED", 
                            )
        boton_jugar_nivel_2.place(relx=0.5, rely=0.4, anchor="center")    
    root.withdraw()

def cerrar_jugar():
    global jugar_window
    if jugar_window is not None:
        jugar_window.destroy()
        jugar_window = None
    root.deiconify()

#VENTANA AJUSTES

def ajustes():
    global ajustes_window
    if ajustes_window is None:
        ajustes_window = ctk.CTkToplevel(root)
        ajustes_window.geometry("1000x600")
        ajustes_window.resizable(0, 0)
        ajustes_window.title("Ajustes")
        
        ajustes_frame = ctk.CTkFrame(master=ajustes_window, width=1000, height=600, corner_radius=10, fg_color="#D6EAF8", border_color="white", border_width=2)
        ajustes_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        ajustes_label = ctk.CTkLabel(master=ajustes_frame, text="Aquí van los ajustes", font=font_1, text_color="black")
        ajustes_label.place(relx=0.5, rely=0.5, anchor="center")
        
        close_button = ctk.CTkButton(master=ajustes_frame, text="Cerrar", font=(font_1, 10), text_color="black", width=100, height=40, corner_radius=32, fg_color="white", hover_color="light blue", command=cerrar_ajustes)
        close_button.place(relx=0.5, rely=0.9, anchor="center")
        
    root.withdraw()

def cerrar_ajustes():
    global ajustes_window
    if ajustes_window is not None:
        ajustes_window.destroy()
        ajustes_window = None
    root.deiconify()

#----------------------------------variables-------------------------------------
font_1 = ctk.CTkFont(family="Inherit", size=26, weight="bold")
font_2 = ctk.CTkFont(family="Cooper Black", size = 35, weight="bold")
imagen = ctk.CTkImage(light_image=Image.open("descartes.png"), 
                                dark_image=Image.open("descartes.png"),
                                size = (300,300)
                                )
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

boton_ajustes = ctk.CTkButton(master = frame_principal,
                                    text="AJUSTES",
                                    font=font_1,
                                    text_color="black",
                                    width=200,
                                    height=90,
                                    corner_radius=32,
                                    fg_color="white",
                                    hover_color= "#76FEEF",
                                    command= ajustes
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
                                image = imagen,
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
boton_ajustes.place(relx = 0.85, rely = 0.83, anchor = "center")

root.mainloop()