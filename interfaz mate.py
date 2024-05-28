from tkinter import *
import customtkinter 
from PIL import Image, ImageTk
root = customtkinter.CTk()
root.geometry("1000x600")
root.resizable(0,0)
root.title("Descartico")
root._set_appearance_mode("light")
root.iconbitmap("descartico.ico")

#----------------------------------variables-------------------------------------
font_1 = customtkinter.CTkFont(family="Inherit", size=26, weight="bold")
font_2 = customtkinter.CTkFont(family="Cooper Black", size = 35, weight="bold")
imagen = customtkinter.CTkImage(light_image=Image.open("descartes.png"), 
                                dark_image=Image.open("descartes.png"),
                                size = (300,300)
                                )
#--------------------------------------------frames------------------------------------------
frame_principal = customtkinter.CTkFrame(master = root, 
                                        width = 1000, 
                                        height = 600, 
                                        corner_radius = 10, 
                                        fg_color = "#D6EAF8", 
                                        border_color = "white", 
                                        border_width = 2
                                        )
#----------------------------------------------botones------------------------------------------
boton_info = customtkinter.CTkButton(master = frame_principal, 
                                    text="INFO", 
                                    font=font_1, 
                                    text_color="black",
                                    width=200, 
                                    height=90, 
                                    corner_radius=32, 
                                    fg_color="white",
                                    hover_color= "light blue"
                                    )

boton_jugar = customtkinter.CTkButton(master = frame_principal,
                                    text="JUGAR",
                                    font=font_1,
                                    text_color="black",
                                    width=200,
                                    height=90,
                                    corner_radius=32,
                                    fg_color="white",
                                    hover_color= "light blue"
                                    )

boton_ajustes = customtkinter.CTkButton(master = frame_principal,
                                    text="AJUSTES",
                                    font=font_1,
                                    text_color="black",
                                    width=200,
                                    height=90,
                                    corner_radius=32,
                                    fg_color="white",
                                    hover_color= "light blue"
                                    )

#----------------------------------------------labels--------------------------------------------
titulo = customtkinter.CTkLabel(master = frame_principal, 
                                text = "DESCARTICO", 
                                font = font_2, 
                                text_color = "red",
                                width = 200,
                                height = 90
                                )
imagen_ = customtkinter.CTkLabel(master = frame_principal, 
                                image = imagen,
                                width = 200,
                                height = 200)

#----------------------------Posicionamiento--------------------------------
frame_principal.place(relx = 0.5, rely = 0.5, anchor="center")
boton_info.place(relx = 0.05, rely = 0.79, anchor = "w")
titulo.place(relx = 0.5, rely = 0.1, anchor = "center")
imagen_.place(relx = 0.5, rely = 0.4,  anchor = "center")
boton_jugar.place(relx = 0.599, rely = 0.79, anchor = "e")
boton_ajustes.place(relx = 0.85, rely = 0.79, anchor = "center")


root.mainloop()