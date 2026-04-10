import tkinter as tk 
from tkinter import messagebox #permite crear mensajes emergentes para mostrar información al usuario
import json #libreria para leer y escribir archivos con progreso del juego
import os #permite interactuar con el os
import random #para que el hollow eloija personajes y acciones de forma aleatoria
from PIL import Image, ImageTk #libreria para manejar imagenes en tkinter   
def cargar_personajes ():
    personajes = [] #lista vacia para almacenar los personajes
    archivo = open("personajes.txt", "r") #abre el archivo con los personajes, la r es para leer el archivo, el resultado se guarda en la variable archivo
    for linea in archivo: #recorre cada linea del archivo, cada linea representa un personaje, el resultado se guarda en la variable linea
       partes = linea.strip().split(",") #.strip() elimina los espacios en blanco al inicio y al final de la linea, split(",") divide la linea en partes usando la coma , el resultado se guarda en la variable partes
       personaje = { #{} crea un diccionario para almacenar los datos del personaje, el resultado se guarda en la variable personaje
              "nombre": partes[0],
              "vida": int(partes[1]), #int() convierte a numero entero, el resultado se guarda en la clave vida del diccionario personaje
              "ataque": int(partes[2]),
              "defensa": int(partes[3]),
              "imagen": partes[4]
              }
       personajes.append(personaje) #append() agrega el personaje a la lista de personajes, cada fora del ciclo for se agrega un personaje a la lista, el resultado se guarda en la variable personajes
    archivo.close() #cierra el archivo para liberar memoria
    return personajes #devuelve la lista de 15 personajes cargados desde el archivo, el resultado se guarda en la variable personajes
