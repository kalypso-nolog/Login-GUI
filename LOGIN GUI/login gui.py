# https://github.com/kalypso-nolog Made by kalypso-nolog as a training code

import customtkinter as ctk # type: ignore
from customtkinter import * # type: ignore
from tkinter import Frame
from PIL import Image # type: ignore 
import ctypes

myappid = u'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# theme principaux / principal theme
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")

theme_image= ctk.CTkImage(Image.open("D:\Projets Divers\LOGIN GUI\sunn (1).ico"), size=(50, 50))

# Themes Toggle On/off
is_dark = True  # quel mode ?

def toggle_appearance_mode():
    global is_dark
    if is_dark:
        ctk.set_appearance_mode("light")
        is_dark = False
        new_image = ctk.CTkImage(Image.open("D:\Projets Divers\LOGIN GUI\moon.ico"), size=(50, 50))
        color_mode_button.configure(image=new_image, fg_color="white", hover_color="white")
    else:
        ctk.set_appearance_mode("dark")
        is_dark = True
        new_image = ctk.CTkImage(Image.open("D:\Projets Divers\LOGIN GUI\sunn (1).ico"), size=(50, 50))
        color_mode_button.configure(image=new_image, fg_color="black", hover_color="black")


login = ctk.CTk() # Crée la page / Create the gui
login.title('Login') # Donnez un titre
login.iconbitmap("D:\Projets Divers\LOGIN GUI\icon.ico") # Changer l'icone en haut à gauche # Change the upside corner icone
login.geometry("500x350") # Taille du gui # height of gui

# frame pour geometry / Frame for geometry
my_frame = ctk.CTkFrame(login, fg_color="transparent")
my_frame.pack(pady=40)


# Ajoutez tous les widgets / Add all the widgets
login_label = ctk.CTkLabel(my_frame, text="Login", font=("Arial", 28, "bold"))
username_label = ctk.CTkLabel(login, text="Username")
username_entry = ctk.CTkEntry(login, placeholder_text="Enter your Username")
password_label = ctk.CTkLabel(login, text="Password")
password_entry = ctk.CTkEntry(login, placeholder_text="Enter your Password")
error_label = ctk.CTkLabel(login, text="")

# Tout enlevé pour le reset de la page et prendre le user
def login_success():
    username = username_entry.get()
    password = password_entry.get()
    if not username:
        error_label.configure(text="Username's missing")
        return
    if not password:
        error_label.configure(text="Password's missing")
        return
    error_label.configure(text="")
    username_label.pack_forget()
    username_entry.pack_forget()
    password_label.pack_forget()
    password_entry.pack_forget()
    login_button.pack_forget()
    color_mode_button.place_forget()

    # Mettre a jour la page quand il s'est login
    login_label.configure(text=f"Successfully login, Welcome {username}", font=("Arial", 28, "bold"))

login_button = ctk.CTkButton(login, text="Login", text_color="black", command=login_success) # couleur du texte "login"
color_mode_button = ctk.CTkButton(login, text="", image=theme_image, width=50, height=50, corner_radius=25, command=toggle_appearance_mode)

# Mettre les couleurs pour le bouton / Make the correct color for the button
if is_dark:
    color_mode_button.configure(fg_color="black", hover_color="black")
else:
    color_mode_button.configure(fg_color="white", hover_color="white")

# Mettre les widgets dans la page GUI # Put all the widgets in

login_label.grid(row=0, column=0, columnspan=10)
username_label.pack(pady=0)
username_entry.pack(pady=10)
password_label.pack(pady=0)
password_entry.pack(pady=0)
error_label.pack(pady=5)
color_mode_button.place(relx=0.95, rely=0.05, anchor="ne")  # mettre en haut à droite (corner)
login_button.pack(pady=0)

login.mainloop() # Pour lancer / To launch
