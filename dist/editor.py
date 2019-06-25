# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:01:31 2019

@author: Juan Pablo Umbarila Granada
"""

from tkinter import filedialog as FileDialog
from io import open

ruta = "" # save file path

def nuevo():
    global ruta
    mensaje.set("Nuevo Fichero")
    ruta = ""
    texto.delete(1.0, 'end')
    root.title("Best Editor")

def abrir():
    global ruta
    mensaje.set("Abrir Fichero")
    ruta = FileDialog.askopenfilename(initialdir='.', 
                                      filetype=(("Fichero de Texto", "*.txt"),),
                                      title="Abrir Fichero de Texto")
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - " + "Best Editor")

def guardar():
    global ruta
    mensaje.set("Guardar Fichero")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero Guardado Correctamente")
    else:
        guardar_como()
    
def guardar_como():
    global ruta
    mensaje.set("Guardar Fichero como")
    fichero = FileDialog.asksaveasfile(title="Guardar Fichero", mode="w", 
                                       defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero Guardado Correctamente")
    else:
        mensaje.set("Guardado Cancelado")
        ruta = ""

root = Tk()
root.title("Best Editor")

# Top Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Gurdar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.destroy)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Box Editor
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Comic Sans MS", 12))

# Bottom Monitor
mensaje = StringVar()
mensaje.set("Bienvenido a tu Best Editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)
root.mainloop()