import tkinter as tk 
from tkinter import messagebox #permite crear mensajes emergentes para mostrar información al usuario
import json #libreria para leer y escribir archivos con progreso del juego
import os #permite interactuar con el os
import random #para que el hollow elija personajes y acciones de forma aleatoria
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

Hollows = [  
    {"nombre":  "El Parque", "imagen": "imagenes/ElParque.jpg"},
    {"nombre":  "El D3", "imagen": "imagenes/D3.png"},
    {"nombre":  "Casa Griffin", "imagen": "imagenes/Griffin.jpg"},
    {"nombre":  "South Park Elementary", "imagen": "imagenes/Elementary.jpg"},
    {"nombre":  "Casa Bonita", "imagen": "imagenes/CasaBonita.jpg"},
] #lista de hollows con su nombre y la ruta de su imagen, cada hollow es un diccionario con las claves nombre e imagen, el resultado se guarda en la variable Hollows

def cargar_imagen (ruta, ancho=80, alto=80): #la ruta es donde esta el archivo
    if not os.path.exists(ruta): #verifica si la ruta del archivo existe, si no existe muestra un mensaje de error y devuelve None
        return None
    imagen_original = Image.open(ruta) #abre la imagen
    imagen_redimensionada = imagen_original.resize((ancho, alto)) #redimensiona la imagen al tamaño especificado, el resultado se guarda en la variable imagen_redimensionada
    imagen_tkinter = ImageTk.PhotoImage(imagen_redimensionada) #convierte la imagen redimensionada a un formato compatible con tkinter, el resultado se guarda en la variable imagen_tkinter
    return imagen_tkinter #devuelve la imagen en formato tkinter, listo para usar la imagen en la interfaz grafica, el resultado se guarda en la variable imagen_tkinter

def cargar_progreso (): #verifica si hay un archivo de progreso existente, si existe lo carga, si no existe crea un nuevo archivo con el progreso actual del juego
    if not os.path.exists("progreso.json"): # da un diccionario vacio si no hay progreso
        return {}
    archivo = open("progreso.json", "r") # abre el archivo en modo lectura, el resultado se guarda en la variable archivo
    datos = json.load(archivo) #convierte el contenido del archivo de formato json a un diccionario de python, el resultado se guarda en la variable datos
    archivo.close() #cierra el archivo para liberar memoria
    return datos #devuelve los datos del progreso de los usuarios cargados desde el archivo
    
def guardar_progreso (datos): #guarda el progreso del juego en un archivo json, recibe un diccionario con los datos del progreso de los usuarios y lo guarda en un archivo llamado progreso.json
    archivo = open("progreso.json", "w") #abre el archivo en modo escritura, el resultado se guarda en la variable archivo
    json.dump(datos, archivo) #convierte el diccionario de datos a formato json y lo escribe en el archivo, el resultado se guarda en la variable datos
    archivo.close() #cierra el archivo para liberar memoria

def limpiar_ventana (): #elimina elementos visuales de la ventana
    for widget in ventana.winfo_children(): #winfo_children() devuelve una lista de todos los widgets hijos de la ventana, el resultado se guarda en la variable widget
        widget.destroy() #destroy() elimina el widget de la ventana, cada widget en la lista de widgets hijos es eliminado, el resultado se guarda en la variable widget

def about(): # crea ventana en la que se enseña info del proyecto
    popup = tk.Toplevel(ventana) #crea una nueva ventana emergente, el resultado se guarda en la variable popup
    popup.title("About") #establece el titulo de la ventana emergente
    popup.geometry("300x220") #establece el tamaño de la ventana emergente
    popup.resizable(False, False) #evita que la ventana emergente se pueda cambiar de tamaño
    tk.Label (popup, text= "Proyecto 1 Introduccion a la programacion", font=("Arial", 14)).pack(pady=20) #pady agrga un espacio entre los elementos
    tk.Label (popup, text= "Cartoon's Epic Adventure").pack()  #popup es el nombre que se le dio a la vetnana emergente
    tk.Label (popup, text= "Santiago Portuguez Hernandez").pack() #pack le dice tkinter que muestre el elemento en la ventana
    tk.Label (popup, text= "Profesor: Ellioth Ramirez").pack()
    tk.Label (popup, text= "I semestre 2026").pack()
    tk.Button (popup, text= "Cerrar", command=popup.destroy).pack(pady=10) #crea un boton para cerrar la ventana emergente, el resultado se muestra en la ventana emergente

def menu_principal():
    global entrada_usuario #declara la variable entrada_usuario como global para que pueda ser accedida desde otras funciones 
    limpiar_ventana() #limpia la ventana principal para mostrar el menu principal, el resultado se muestra en la ventana principal
    boton_about = tk.Button(ventana, text="About", command= about)
    boton_about.place (x = 720, y = 10) #crea un boton para mostrar la ventana de about, el resultado se muestra en la ventana principal
    tk.Label(ventana, text="Cartoon's Epic Adventure", font=("Arial", 28, "bold")).pack(pady=80) #crea una etiqueta con el titulo del juego, el resultado se muestra en la ventana principal
    tk.Label(ventana,text="Introduzca nombre de Usuario:", font=("Arial", 14)).pack() #crea una etiqueta para pedir el nombre de usuario, el resultado se muestra en la ventana principal
    entrada_usuario = tk.Entry(ventana, font =("Arial", 14), width=25) #crea un campo de entrada para que el usuario escriba su nombre, el resultado se guarda en la variable entrada_usuario
    entrada_usuario.pack(pady=10) #muestra el campo de entrada en la ventana principal
    tk.Button (ventana , text="Iniciar", font = ("Arial", 14), width=15, command=Inicio).pack(pady=20) #crea un boton para iniciar el juego, el resultado se muestra en la ventana principal, al hacer click en el boton se llama a la funcion Inicio para comenzar el juego
    

def Inicio():
    nombre_usuario = entrada_usuario.get().strip()
    if nombre_usuario == "":
        messagebox.showwarning("Atencion","Por favor ingrese un nombre de usuario") #muestra un mensaje de advertencia si el usuario no ingresa un nombre, el resultado se muestra en una ventana emergente
        return #para la funcion cuando no hay nombre de usuario
    progreso = cargar_progreso() #carga el progreso del juego desde el archivo, el resultado se guarda en la variable progreso
    if nombre_usuario in progreso: #verifica si el nombre de usuario ya existe en el progreso
        datos_usuario = progreso [nombre_usuario] #si el usuario existe, carga sus datos del progreso, el resultado se guarda en la variable datos_usuario
        pantalla_mapa (nombre_usuario, datos_usuario) #muestra la pantalla del mapa con los datos del usuario cargados
    else:
        pantalla_seleccion(nombre_usuario) #si el usuario no existe, muestra la pantalla de seleccion de personaje para crear un nuevo progreso para ese usuario
        

def pantalla_seleccion(nombre_usuario): #escoger 3 personajes para el usuario
    limpiar_ventana() #limpia la ventana para mostrar la pantalla de seleccion de personajes, el resultado se muestra en la ventana principal
    personajes = cargar_personajes() #carga los personajes desde el archivo, el resultado se guarda en la variable personajes
    tk.Label(ventana, text="Escoge 3 personajes para la aventura", font=("Arial",18,"bold")).pack(pady=15)
    tk.Label(ventana, text= "Solo selecciona 3:", font= ("Arial", 12)).pack()
    variables = [] #lista donde se guardan las variables de cada checkbox

    frame_personajes = tk.Frame(ventana) #Frame es un contenedor que agrupa elementos
    frame_personajes.pack(pady=5) #lo usamos para mostrar los personajes en la ventana
    frame_personajes.imagenes = [] #creamos un atributo del frame para guardar las imagenes, esto es necesario para que las imagenes no desaparezcan al mostrarlas en la ventana, el resultado se guarda en el atributo imagenes del frame_personajes

    for i, p in enumerate(personajes): #enumerate recorre lista de personajes, en cada vuelta da num de posicion y el elemento
        #i es el numero de posicion, p es el personaje
        var = tk.IntVar() #tk.InVar() es una clase de tkinter que crea una variable entera que puede ser usada para controlar el estado de un checkbox, el resultado se guarda en la variable var
        variables.append(var) # append() va anotando los personajes que se van seleccionando en el checkbox
        imagen = cargar_imagen(p["imagen"], ancho=45, alto=45) #carga la imagen del personaje, el resultado se guarda en la variable imagen
        frame_personajes.imagenes.append(imagen) #guarda la imagen en el atributo del frame para que no desaparezca, el resultado se guarda en la lista de imagenes del frame_personajes

        fila_num = i // 2 # calcula la fila
        col_num =  i % 2 # calcula la columna

        #Ocupe ayuda de AI para el razonamiento debido a que los personajes me quedaban en una sola linea y no podia verlos todos
        
        fila = tk.Frame(frame_personajes) #crea un nuevo frame para cada personaje, el resultado se guarda en la variable fila
        fila.grid(row=fila_num, column=col_num, pady=2, padx =10, sticky="w") #.grid() permite organizar los personajes es una cuadricula, cada personaje se coloca en una fila diferente
        #row= i pone cada personaje en una fila
        #column=0 los pone en la misma columna
        #sticky="w" los alinea a la izquierda, w viene de west
        if imagen: #si la imagen se cargo correctamente la muestra
            tk.Label(fila, image=imagen).pack(side="left", padx=5) #crea una etiqueta para mostrar la imagen del personaje, el resultado se muestra en la ventana
            # side="left" coloca la imagen a la izquierdadel frame y padx=5 agrega espacio entre imagen y checkbox
        texto = f"{p['nombre']} (Vida: {p['vida']}, Ataque: {p['ataque']}, Defensa: {p['defensa']})" #crea un texto con elnombre y stats del personaje, p viene de personajes, el resultado se guarda en la variable texto
        tk.Checkbutton(fila, text=texto, variable=var, font=("Arial", 10)).pack(side="left") #checkbutton crea un checkbox para seleccionar el personaje, el resultado se muestra en la ventana
        #variable=var conecta el checkbox con su variable
        #cuando el usuario selecciona el checkbox, la variable var se actualiza a 1, si lo deselecciona se actualiza a 0

    def confirmar ():
        seleccionados = [] #lista para guardar los personajes seleccionados por el usuario
        for i, var in enumerate(variables): #recorre todas las variables de los checkbox
            if var.get() == 1: #si esta marcada
                seleccionados.append(personajes[i]) #agrega el personaje si esta marcado a la lista de seleccionados
        if len(seleccionados) != 3: #si el usuario no selecciona exactamente 3 personajes muestra un mensaje de error
            messagebox.showerror("Atencion","Debes seleccionar exactamente 3 personajes") #muestra un mensaje de error si el usuario no selecciona exactamente 3 personajes, el resultado se muestra en una ventana emergente
            return #para la funcion si no se seleccionan 3 personajes
        progreso = cargar_progreso()
        progreso[nombre_usuario]= { #se van a guardar los nombres de los perosnajes seleccionados en el progreso del usuario, el resultado se guarda en la variable progreso
            "personajes":[p["nombre"] for p in seleccionados], #guarda solo el nombre de los personajes seleccionados en el progreso del usuario
            #Es una lista de comprensio; recorre cada personaje seleccionado y extrae su nombre para guardarlo en la lista de personajes del progreso del usuario
            "hollow_actual": 0, #guarda el indice del hollow actual en el progreso del usuario, el resultado se guarda en la clave hollow_actual del progreso del usuario
            "personajes_desbloqueados": [] #guarda una lista de personajes desbloqueados en el progreso del usuario, inicialmente vacia, el resultado se guarda en la clave personajes_desbloqueados del progreso del usuario  
        }
        guardar_progreso(progreso) #guarda el progreso del usuario en el archivo, el resultado se guarda en la variable progreso
        pantalla_mapa(nombre_usuario, progreso[nombre_usuario]) #muestra la pantalla del mapa con el progreso del usuario actualizado

    tk.Button(ventana, text = "Confirmar", font=("Arial",13), command=confirmar).pack(pady=10) #crea un boton para confirmar la seleccion de personajes

def pantalla_mapa(nombre_usuario, datos_usuario):
    limpiar_ventana() #limpia la ventana para mostrar el mapa, el resultado se muestra en la ventana principal
    imagenes_guardadas = [] #lista para guardar las imagenes de los hollows
    hollow_actual = datos_usuario["hollow_actual"] #se ve en que hollow va el usuario, datos_usuario es el diccionario del usuario, hollow_actual es la clave que guarda el indice del hollow actual, el resultado se guarda en la variable hollow_actual
    tk.Label(ventana, text= "Mapa Cartoon", font = ("Arial",22,"bold")).pack(pady=20) #Titulo del mapa
    tk.Label(ventana, text= f"Usuario: {nombre_usuario}", font = ("Arial", 14)).pack() #muestra el nombre del usuario en el mapa
    frame_mapa = tk.Frame(ventana) #frame que contiene los botones del mapa
    frame_mapa.pack(pady=15) #muestra el frame del mapa en la ventana
    frame_mapa.imagenes = [] #crea un atributo del frame para guardar las imagenes de los hollows, esto es necesario para que las imagenes no desaparezcan al mostrarlas en la ventana, el resultado se guarda en la lista de imagenes del frame_mapa
    for i, hollow in enumerate (Hollows): #recorre lista de hollows del inicio, enumerate da indice y hollow
        imagen = cargar_imagen(hollow["imagen"], ancho = 60, alto=60) #carga imagen del hollow
        frame_mapa.imagenes.append(imagen) #guarda la imagen en la lista de imagenes para que no desaparezca
        if i < hollow_actual: #si el hollow ya fue ganado
            estado = tk.DISABLED #desactiva el boton del hollow
            texto = f"{hollow['nombre']} (Completado)" #muestra el nombre del hollow con la etiqueta de completado
            color = "green" #color verde para los hollows completados
        elif i == hollow_actual: # hollow disponible
            estado = tk.NORMAL #activa el boton del hollow
            texto = f"{hollow['nombre']} (Disponible)" #muestra el nombre del hollow con la etiqueta de disponible
            color = "darkblue" #color azul para el hollow disponible
        else:
            estado = tk.DISABLED #desactiva el boton del hollow
            texto = f"{hollow['nombre']} (Bloqueado)" #muestra el nombre del hollow con la etiqueta de bloqueado
            color = "red" #color rojo para los hollows bloqueados
        fila = tk.Frame(frame_mapa) #frame para poner la imagen y el boton juntos en una fila
        fila.grid(row=i, column=0, pady=5) #organiza los botones del mapa en una cuadricula, cada hollow en una fila diferente
        if imagen: #si la imagen se cargo correctamente la muestra
            tk.Label(fila, image=imagen).pack(side="left", padx=8)

        tk.Button(fila, text=texto, width=28, font=("Arial", 12),fg=color, state=estado, command=lambda i=i: ir_a_hollow(nombre_usuario, datos_usuario, i)).pack(side="left")
            #state=estado define si el boton esta activo o no 
            #lambda es una funcion que se usa cuando se ocupa pasar un valor a algo en un momento, sin crear una funcion con def
            #aca en el mapa hay un for que hace 5 botones (uno para cada hollow)
            #lambda i=i le dice a cada boton que guarde el numero del hollow en este momento
            # sin lamda todos los botones se van al mismo hollow por que en el for al final i siempre va a valer 4 

def ir_a_hollow(nombre_usuario, datos_usuario, indice_hollow): #cuando un usuario selecciona una ubi del mapa
    #ademas prepara a los personajes de cada hollow(diferentes a los del jugador)
    personajes = cargar_personajes() #carga los personajes disponibles
    nombres_jugador = datos_usuario["personajes"] #guarda los nombres de los personajes del jugador en una lista, el resultado se guarda en la variable nombres_jugador
    disponibles =[] #lista para guardar los personajes disponibles para el hollow
    for p in personajes: #p es cada personaje en la lista de personajes
        if p["nombre"] not in nombres_jugador: #si el nombre del personaje no esta en la lista de personajes del jugador, lo agrega a la lista de personajes disponibles para el hollow
            disponibles.append(p) #append agrega el personaje a la lista de disponibles
    personajes_hollow = random.sample(disponibles, 3) #elige 3 personajes aleatorios de la lista de disponibles para el hollow, el resultado se guarda en la variable personajes_hollow
    #random.sample(lista, cantidad) escoge elementos al azar sin repetir, en este caso escoge 3 personajes de la lista de disponibles para el hollow
    messagebox.showinfo("Hollow encontrado", f"El Hollow tiene: {', '.join([p['nombre'] for p in personajes_hollow])}") #muestra un mensaje con los personajes del hollow, el resultado se muestra en una ventana emergente
    #messagebox.showinfo muestra un mensaje informativo
    #', '.join(lista) une los elementos de la lista en un string separado por comas, en este caso une los nombres de los personajes del hollow para mostrarlos en el mensaje
    #(p['nombre'] for p in personajes_hollow) es una lista de comprension que recorre cada personaje del hollow y extrae su nombre para unirlo en el mensaje

ventana = tk.Tk() #Se crea la ventana principal del juego
ventana.title("Cartoon's Epic Adventure") #titulo que aparce en la barra superior de la ventana
ventana.geometry("800x600") #tamaño de la ventana
ventana.resizable(False, False) #evita que la ventana se pueda cambiar de tamaño

menu_principal() #se llama a la primera pantalla para que aparezca
ventana.mainloop() #mantiene la ventana abierta y escucha eventos como clicks o entradas de teclado, el resultado se muestra en la ventana principal 