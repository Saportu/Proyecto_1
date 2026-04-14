import tkinter as tk 
from tkinter import messagebox #permite crear mensajes emergentes para mostrar información al usuario
import json #libreria para leer y escribir archivos con progreso del juego
import os #permite interactuar con el os
import random #para que el hollow elija personajes y acciones de forma aleatoria
from PIL import Image, ImageTk #libreria para manejar imagenes en tkinter   

def cargar_personajes (): # esta funcion carga los personajes desde un archivo de texto, cada linea del archivo representa un personaje con sus atributos separados por comas, el resultado se guarda en la variable personajes
    personajes = [] #lista vacia para almacenar los personajes
    archivo = open("personajes.txt", "r") #abre el archivo con los personajes, la r es para leer el archivo, el resultado se guarda en la variable archivo
    for linea in archivo: #recorre cada linea del archivo, cada linea representa un personaje, el resultado se guarda en la variable linea
       partes = linea.strip().split(",") #.strip() elimina los espacios en blanco al inicio y al final de la linea, split(",") divide la linea en partes usando la coma , el resultado se guarda en la variable partes
       personaje = { #{} crea un diccionario para almacenar los datos del personaje, el resultado se guarda en la variable personaje
              "nombre": partes[0],
              "vida": int(partes[1]), #int() convierte a numero entero, el resultado se guarda en la clave vida del diccionario personaje
              "vida_max": int(partes[1]), #guarda la vida max del personaje, que es igual a la vida inicial, el resultado se guarda en la clave vida_max del diccionario personaje
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
    if not os.path.exists("progreso.json"): # da un diccionario vacio si no hay progreso # json es un archivo de texto que se usa para guardar datos en formato de diccionario, el resultado se guarda en la variable progreso.json
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
    tk.Label (popup, text= "Profesor: Ellioth Ramirez").pack() #un label es un elemento de texto que se muestra
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
    nombre_usuario = entrada_usuario.get().strip() #obtiene el texto que ingresa el usuario, .get() obtiene el texto del campo de entrada, .strip() elimina los espacios en blanco al inicio y al final del texto, el resultado se guarda en la variable nombre_usuario
    if nombre_usuario == "":
        messagebox.showwarning("Atencion","Por favor ingrese un nombre de usuario") #muestra un mensaje de advertencia si el usuario no ingresa un nombre, el resultado se muestra en una ventana emergente
        return #para la funcion cuando no hay nombre de usuario
    progreso = cargar_progreso() #carga el progreso del juego desde el archivo, el resultado se guarda en la variable progreso
    if nombre_usuario in progreso: #verifica si el nombre de usuario ya existe en el progreso
        datos_usuario = progreso [nombre_usuario] #si el usuario existe, carga sus datos del progreso, el resultado se guarda en la variable datos_usuario
        pantalla_mapa (nombre_usuario, datos_usuario) #muestra la pantalla del mapa con los datos del usuario cargados
    else:
        pantalla_seleccion(nombre_usuario,[]) #si el usuario no existe, muestra la pantalla de seleccion de personaje para crear un nuevo progreso para ese usuario
       #se llama con un segundo argumeto de lista vacia ya que el usuario no tiene personajes desbloqueados aun 

def pantalla_seleccion(nombre_usuario, personajes_disponibles): #escoger 3 personajes para el usuario
    limpiar_ventana() #limpia la ventana para mostrar la pantalla de seleccion de personajes, el resultado se muestra en la ventana principal
    todos_personajes = cargar_personajes() #carga todos los personajes disponibles desde el archivo, el resultado se guarda en la variable todos_personajes
    if len(personajes_disponibles) == 0: #si el usuario no tiene personajes desbloqueados, se cargan todos los personajes disponibles para la seleccion
        # len() devuelve la cantidad de elementos en la lista de personajes_disponibles, si es igual a 0 significa que el usuario no tiene personajes desbloqueados
        personajes_a_mostrar = todos_personajes
    else: 
        personajes_a_mostrar = [p for p in todos_personajes if p["nombre"] in personajes_disponibles]#filtra solo los personajes que el jugador tiene disponibls
        #p for p recorre cada personaje el la lista de todos_personajes, if p["nombre"] in personajes_disponibles verifica si el nombre del personaje esta en la lista de personajes disponibles para el usuario, el resultado se guarda en la variable personajes_a_mostrar
    tk.Label(ventana, text="Escoge 3 personajes para la aventura", font=("Arial",18,"bold")).pack(pady=15)
    tk.Label(ventana, text= "Solo selecciona 3:", font= ("Arial", 12)).pack()

    variables = [] #lista donde se guardan las variables de cada checkbox
    frame_personajes = tk.Frame(ventana) #Frame es un contenedor que agrupa elementos
    frame_personajes.pack(pady=5) #lo usamos para mostrar los personajes en la ventana
    frame_personajes.imagenes = [] #creamos un atributo del frame para guardar las imagenes, esto es necesario para que las imagenes no desaparezcan al mostrarlas en la ventana, el resultado se guarda en el atributo imagenes del frame_personajes

    for i, p in enumerate(personajes_a_mostrar): #enumerate recorre lista de personajes, en cada vuelta da num de posicion y el elemento
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
                seleccionados.append(personajes_a_mostrar[i]) #agrega el personaje si esta marcado a la lista de seleccionados
        if len(seleccionados) != 3: #si el usuario no selecciona exactamente 3 personajes muestra un mensaje de error, len() devuelve la cantidad de elementos en la lista de seleccionados, el resultado se compara con 3 para verificar si el usuario selecciono exactamente 3 personajes
            messagebox.showerror("Atencion","Debes seleccionar exactamente 3 personajes") #muestra un mensaje de error si el usuario no selecciona exactamente 3 personajes, el resultado se muestra en una ventana emergente
            return #para la funcion si no se seleccionan 3 personajes
        
        progreso = cargar_progreso()
        if nombre_usuario not in progreso: #si el usuario no existe en el progreso, se crea un nuevo progreso para ese usuario con los personajes seleccionados y el hollow actual en 0, el resultado se guarda en la variable progreso
            progreso[nombre_usuario]= { #se van a guardar los nombres de los perosnajes seleccionados en el progreso del usuario, el resultado se guarda en la variable progreso
            "personajes":[p["nombre"] for p in seleccionados], #guarda solo el nombre de los personajes seleccionados en el progreso del usuario
            #Es una lista de comprensio; recorre cada personaje seleccionado y extrae su nombre para guardarlo en la lista de personajes del progreso del usuario
            "hollow_actual": 0, #guarda el indice del hollow actual en el progreso del usuario, el resultado se guarda en la clave hollow_actual del progreso del usuario
            "personajes_desbloqueados": [p["nombre"] for p in seleccionados] #guarda una lista de personajes desbloqueados en el progreso del usuario, inicialmente vacia, el resultado se guarda en la clave personajes_desbloqueados del progreso del usuario  
        }
        else: #actualiza solo los personajes activos, deja el progreso
            progreso [nombre_usuario]["personajes"] = [p["nombre"] for p in seleccionados] #si el usuario ya existe, actualiza la lista de personajes seleccionados en su progreso, el resultado se guarda en la clave personajes del progreso del usuario
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
   todos = cargar_personajes() #carga todos los personajes disponibles desde el archivo, el resultado se guarda en la variable todos
   nombres_jugador = datos_usuario["personajes"] #obtiene los nombres de los personajes seleccionados por el usuario, el resultado se guarda en la variable nombres_jugador
   disponibles = [p for p in todos if p ["nombre"] not in nombres_jugador] #filtra los personajes que no fueron seleccionados por el usuario para usarlos como enemigos en el hollow, el resultado se guarda en la variable disponibles
   personajes_hollow = random.sample(disponibles, 3) #elige 3 personajes aleatorios de la lista de disponibles para el hollow, el resultado se guarda en la variable personajes_hollow
   personajes_usuario = [p for p in todos if p["nombre"] in nombres_jugador] # p for p recorre cada personaje en la lista de todos, if p["nombre"] in nombres_jugador verifica si el nombre del personaje esta en la lista de nombres del jugador, el resultado se guarda en la variable personajes_usuario
   for p in personajes_usuario: # restaura vida de los personajes
       p["vida"] = p["vida_max"]
   for p in personajes_hollow:
       p["vida"] = p["vida_max"]
       
   pantalla_batalla(nombre_usuario, datos_usuario, personajes_usuario, personajes_hollow, indice_hollow) #muestra la pantalla de batalla con los personajes del usuario y los personajes del hollow, el resultado se muestra en la ventana principal

def pantalla_batalla(nombre_usuario, datos_usuario, equipo_jugador, equipo_hollow, indice_hollow): 
    limpiar_ventana()
    estado = { #se crea un diccionario para guardar el estado de la batalla, el resultado se guarda en la variable estado
        "personaje_jugador" : equipo_jugador[0], # de equipo_jugador toma el primer personaje para ser el personaje activo del jugador, el resultado se guarda en la clave personaje_jugador del estado
        "personaje_hollow" : equipo_hollow[0], # de equipo_hollow toma el primer personaje para ser el personaje activo del hollow, el resultado se guarda en la clave personaje
        "puntaje_jugador" : 0,
        "puntaje_hollow" : 0,
        "turno" : "jugador", #indica de quien es el turno, inicialmente es del jugador, el resultado se guarda en la clave turno del estado
        "batalla_activa": True #indica si la batalla sigue activa o ya termino, inicialmente es True, el resultado se guarda en la clave batalla_activa del estado
    }
    fondo_imagen = cargar_imagen(Hollows[indice_hollow]["imagen"], ancho=800, alto=600) #carga la imagen de fondo del hollow seleccionado, el resultado se guarda en la variable fondo_imagen
    if fondo_imagen: #si la imagen se cargo correctamente la muestra como fondo
        lbl_fondo = tk.Label(ventana, image=fondo_imagen) #crea una etiqueta para mostrar la imagen de fondo, el resultado se guarda en la variable lbl_fondo
        lbl_fondo.place(x=0, y=0) #coloca la imagen de fondo en la ventana
        lbl_fondo.image = fondo_imagen #guarda la imagen en un atributo de la etiqueta para que no desaparezca, el resultado se guarda en el atributo image del lbl_fondo

    lbl_puntaje = tk.Label(ventana, text=f"Tu puntaje: {estado['puntaje_jugador']} | Hollow: {estado['puntaje_hollow']}", font=("Arial", 12), bg="black", fg="white") #crea una etiqueta para mostrar el puntaje del jugador y del hollow, el resultado se guarda en la variable lbl_puntaje, bg significa background y fg significa foreground, se usan para que el texto sea legible sobre la imagen de fondo
    lbl_puntaje.place(x=250, y=10) #coloca la etiqueta de puntaje en la ventana
    frame_equipo = tk.Frame(ventana, bg="black") #crea un frame para mostrar los personajes del jugador, el resultado se guarda en la variable frame_equipo
    frame_equipo.place(x=10, y=10) #coloca el frame del equipo en la ventana, x=10 y=10 lo coloca en la esquina superior izquierda
    frame_equipo.imagenes = [] #crea un atributo del frame para guardar las imagenes de los personajes del jugador, esto es necesario para que las imagenes no desaparezcan al mostrarlas en la ventana, el resultado se guarda en la lista de imagenes del frame_equipo

    def actualizar_equipo():
        for widget in frame_equipo.winfo_children(): #winfo_children() devuelve una lista de todos los widgets hijos del frame_equipo, el resultado se guarda en la variable widget
            widget.destroy() #elimina los widgets actuales del frame del equipo para actualizar la informacion, el resultado se muestra en la ventana
        frame_equipo.imagenes.clear() #limpia la lista de imagenes para actualizar las imagenes del equipo
        for p in equipo_jugador:
            img = cargar_imagen(p["imagen"], ancho=40, alto=40) #carga la imagen del personaje del jugador, el resultado se guarda en la variable img para personaje del jugador #p viene de equipo_jugador, que es la lista de personajes del jugador
            frame_equipo.imagenes.append(img) #guarda la imagen en la lista de imagenes del frame para que no desaparezca, el resultado se guarda en la lista de imagenes del frame_equipo
            color_fondo = "green" if p["vida"] > 0 else "red" #si la vida del personaje es mayor a 0 el fondo es verde, si no es rojo, el resultado se guarda en la variable color_fondo
            borde = "yellow" if p == estado ["personaje_jugador"] else color_fondo #si el personaje es el personaje activo del jugador, el borde es amarillo, si no es el personaje activo el borde es del mismo color que el fondo, el resultado se guarda en la variable borde
            btn = tk.Button(frame_equipo, image = img, bg=borde, command=lambda p=p: cambiar_personaje(p)) #crea un boton para mostrar la imagen del personaje del jugador, el resultado se guarda en la variable btn, el fondo del boton es el color definido por color_fondo, al hacer click en el boton se llama a la funcion seleccionar_personaje con el personaje correspondiente
            #lambda p=p es necesario para que cada boton guarde el personaje correcto, sin lambda todos los botones se asociarian al mismo personaje por como funciona el ciclo for # cambiar_personaje es la funcion que se llama al hacer click en el boton del personaje del jugador, recibe el personaje correspondiente como argumento (ahora se va a crear)
            btn.pack(side="left", padx=3) #coloca el boton del personaje en el frame del equipo, side="left" los alinea a la izquierda, padx=5 agrega espacio entre los botones

    frame_jugador = tk.Frame(ventana, bg="black", bd=2, relief="solid") #crea un frame para mostrar el personaje activo del jugador, el resultado se guarda en la variable frame_jugador, bd es el grosor del borde, relief define el estilo del borde
    frame_jugador.place(x=30, y=200) #coloca el frame del jugador en la ventana
    frame_jugador.imagenes = [] #crea un atributo del frame para guardar la imagen del personaje activo del jugador, esto es necesario para que la imagen no desaparezca al mostrarla en la ventana, el resultado se guarda en la lista de imagenes del frame_jugador
    lbl_nombre_jugador = tk.Label(frame_jugador,text="", font=("Arial", 11, "bold"), bg="black", fg="white") #crea una etiqueta para mostrar el nombre del personaje activo del jugador, el resultado se guarda en la variable lbl_nombre_jugador
    lbl_nombre_jugador.pack(pady=5) #coloca la etiqueta del nombre del personaje activo del jugador en el frame del jugador
    lbl_img_jugador = tk.Label (frame_jugador, bg="black") #crea una etiqueta para mostrar la imagen del personaje activo del jugador, el resultado se guarda en la variable lbl_img_jugador
    lbl_img_jugador.pack(pady=5) #coloca la etiqueta de la imagen
    lbl_vida_jugador = tk.Label(frame_jugador, text="", font = ("Arial", 12), bg="black", fg="lime") #crea una etiqueta para mostrar la vida del personaje activo del jugador, el resultado se guarda en la variable lbl_vida_jugador
    lbl_vida_jugador.pack() #coloca la etiqueta de la vida del personaje activo

    frame_hollow = tk.Frame(ventana, bg="black", bd=2, relief="solid") #crea un frame para mostrar el personaje activo del hollow, el resultado se guarda en la variable frame_hollow
    frame_hollow.place(x=580, y=200) #coloca el frame del hollow en la ventana
    frame_hollow.imagenes = [] #crea un atributo del frame para guardar la imagen del personaje activo del hollow, esto es necesario para que la imagen no desaparezca
    lbl_nombre_hollow = tk.Label(frame_hollow,text="", font=("Arial", 11, "bold"), bg="black", fg="white") #crea una etiqueta para mostrar el nombre del personaje activo del hollow, el resultado se guarda en la variable lbl_nombre_hollow
    lbl_nombre_hollow.pack() #coloca la etiqueta del nombre del hollow en el frame del hollow
    lbl_img_hollow = tk.Label (frame_hollow, bg="black") #crea una etiqueta para mostrar la imagen del personaje activo del hollow, el resultado se guarda en la variable lbl_img_hollow
    lbl_img_hollow.pack() #coloca la etiqueta de la imagen del personaje activo del hollow
    lbl_vida_hollow = tk.Label(frame_hollow, text="", font = ("Arial", 12), bg="black", fg="lime") #crea una etiqueta para mostrar la vida del personaje activo del hollow, el resultado se guarda en la variable lbl_vida_hollow
    lbl_vida_hollow.pack() #coloca la etiqueta de la vida del hollow en el frame del hollow

    lbl_log = tk.Label(ventana, text="", font=("Arial", 11), bg="black", fg="white", wraplength=400) #crea una etiqueta para mostrar el log de la batalla, el resultado se guarda en la variable lbl_log
# wraplength hace que el texto en el log se ajuste a un ancho maximo de 400 pixeles, evitando que se salga de la ventana, el resultado se guarda en la variable lbl_log
    lbl_log.place (x=200, y=500) #coloca la etiqueta del log en la ventana
    btn_atacar = tk.Button(ventana, text="Atacar", font=("Arial", 13, "bold"), bg="red", fg="black", width=12) #crea un boton para atacar, el resultado se guarda en la variable btn_atacar
    btn_atacar.place(x=300, y=450) #coloca el boton de atacar en la ventana

    def actualizar_pantalla(): # actualiza las imagenes y vida en pantalla
        pj = estado["personaje_jugador"] #toma estado del personaje activo del jugador, el resultado se guarda en la variable pj
        ph = estado["personaje_hollow"] #toma estado del personaje activo del hollow, el resultado se guarda en la variable ph

        lbl_nombre_jugador.config(text=pj["nombre"]) #actualiza el texto del nombre del personaje activo del jugador, pj viene de estado, que es el diccionario que guarda el estado de la batalla
        img_j = cargar_imagen(pj["imagen"], ancho=120, alto=120) #carga la imagen del personaje activo del jugador, el resultado se guarda en la variable img_j
        frame_jugador.imagenes = [img_j] #guarda la imagen en la lista de imagenes del frame del jugador para que no desaparezca, el resultado se guarda en la lista de imagenes del frame_jugador
        lbl_img_jugador.config(image=img_j) #actualiza la imagen del personaje activo del jugador, img_j viene de cargar_imagen
        lbl_vida_jugador.config(text=f"Vida: {pj['vida']} / {pj['vida_max']}") #actualiza el texto de la vida del personaje activo del jugador, pj viene de estado, que es el diccionario que guarda el estado de la batalla

        lbl_nombre_hollow.config(text=ph["nombre"]) #actualiza el texto del nombre del personaje activo del hollow, ph viene de estado, que es el diccionario que guarda el estado de la batalla
        img_h = cargar_imagen(ph["imagen"], ancho=120, alto=120) #carga la imagen del personaje activo del hollow, el resultado se guarda en la variable img_h
        frame_hollow.imagenes = [img_h] #guarda la imagen en la lista de imagenes del frame del hollow para que no desaparezca, el resultado se guarda en la lista de imagenes del frame_hollow
        lbl_img_hollow.config(image=img_h) #actualiza la imagen del personaje activo del hollow, img_h viene de cargar_imagen
        lbl_vida_hollow.config(text=f"Vida: {ph['vida']} / {ph['vida_max']}") #actualiza el texto de la vida del personaje activo del hollow, ph viene de estado, que es el diccionario que guarda el estado de la batalla
        lbl_puntaje.config(text=f"Tu puntaje: {estado['puntaje_jugador']} | Hollow: {estado['puntaje_hollow']}") #actualiza el texto del puntaje del jugador y del hollow, estado viene de la variable que guarda el estado de la batalla

        actualizar_equipo() #actualiza el frame del equipo del jugador para reflejar cualquier cambio en la vida de los personajes o el personaje activo, el resultado se muestra en la ventana

    def calcular_perdida(atacante, defensor): #calcula la perdida de vida en un ataque, recibe el atacante y defensor como diccionarios
        perdida = atacante["ataque"] - defensor["defensa"] #la perdida se calcula restando la defensa al ataque, el resultado se guarda en la variable perdida
        if perdida < 1: #si la perdida es menor a 1, se ajusta a 1 para evitar que se gane vida al atacar, el resultado se compara con 1 para verificar si es negativa
            perdida = 1
        return perdida #devuelve la cantidad de vida que se pierde en el ataque, el resultado se guarda en la variable perdida

    def ver_ko(personaje_ko, equipo_perdedor, equipo_ganador, usuario_gana):
        if personaje_ko["vida"] <= 0:
            personaje_ko ["vida"] = 0 #ajusta la vida a 0 si es negativa para evitar mostrar valores negativos, el resultado se guarda en la clave vida del personaje_ko
            personaje_ko["vida"] = personaje_ko ["vida_max"] #recupera vida de el perosnaje
            equipo_ganador.append(personaje_ko) #agrega el personaje que fue ko al equipo ganador, el resultado se guarda en la lista del equipo_ganador
            equipo_perdedor.remove(personaje_ko) #elimina el personaje que fue ko del equipo perdedor, el resultado se guarda en la lista del equipo_perdedor
            if usuario_gana:
                estado ["puntaje_jugador"] += 1 #si el usuario gana el punto, se incrementa el puntaje del jugador en 1, el resultado se guarda en la clave puntaje_jugador del estado
                lbl_log.config(text=f"¡Has derrotado a {personaje_ko['nombre']}!") #muestra un mensaje en el log indicando que el jugador ha derrotado al personaje ko, el resultado se muestra en la etiqueta del log
            else:
                estado ["puntaje_hollow"] += 1 #si el hollow gana el punto, se incrementa el puntaje del hollow en 1, el resultado se guarda en la clave puntaje_hollow del estado
                lbl_log.config(text=f"¡{personaje_ko['nombre']} te ha derrotado!") #muestra un mensaje en el log indicando que el hollow ha derrotado al personaje ko, el resultado se muestra en la etiqueta del log
            return True #devuelve True si hubo un ko, el resultado se guarda en la variable que llama a la funcion ver_ko
        return False #devuelve False si no hubo un ko, el resultado se guarda en la variable que llama a la funcion ver_ko
    def Turno(): 
        if len (equipo_jugador) == 0: 
            estado["batalla_activa"] = False #si el equipo del jugador se queda sin personajes, la batalla termina, el resultado se guarda en la clave batalla_activa del estado
            btn_atacar.config(state=tk.DISABLED) #desactiva el boton de atacar al finalizar la batalla, el resultado se muestra en la ventana
            messagebox.showinfo("Derrota", "Recuperate! e Intenta de nuevo.") #muestra un mensaje de derrota si el jugador pierde la batalla, el resultado se muestra en una ventana emergente
            todos = cargar_personajes() #carga todos los personajes disponibles desde el archivo, el resultado se guarda en la variable todos
            for p in todos: #restaura la vida de todos los personajes para que el jugador los tenga disponibles en su proximo intento, p viene de todos, que es la lista de todos los personajes
                p["vida"] = p["vida_max"]
            pantalla_mapa(nombre_usuario, datos_usuario) #regresa al mapa para que el jugador pueda intentar otro hollow, el resultado se muestra en la ventana principal
            return #termina la funcion Turno cuando el jugador pierde
        if len(equipo_hollow) == 0: #si el equipo del hollow se queda sin personajes, la batalla termina, el resultado se guarda en la clave batalla_activa del estado
            estado["batalla_activa"] = False #si el hollow pierde la batalla, se desbloquea el siguiente hollow en el progreso del usuario, el resultado se guarda en la clave batalla_activa del estado
            btn_atacar.config(state=tk.DISABLED) #desactiva el boton de atacar al finalizar la batalla, el resultado se muestra en la ventana
            progreso = cargar_progreso() #carga el progreso del usuario desde el archivo, el resultado se guarda en la variable progreso
            nombres_ganados = [p["nombre"] for p in equipo_jugador] #crea una lista con los nombres de los personajes del jugador que ganaron la batalla, p viene de equipo_jugador, que es la lista de personajes del jugador
            desbloqueados_antes = progreso[nombre_usuario].get("personajes_desbloqueados", []) #obtiene la lista de personajes desbloqueados antes de la batalla, si no existe se devuelve una lista vacia, el resultado se guarda en la variable desbloqueados_antes
            nuevos_desbloqueados = [p["nombre"] for p in equipo_jugador if p["nombre"] not in desbloqueados_antes] #crea una lista con los nombres de los personajes del jugador que ganaron la batalla y que no estaban desbloqueados antes, el resultado se guarda en la variable nuevos_desbloqueados
            progreso[nombre_usuario]["personajes_desbloqueados"] = desbloqueados_antes + nuevos_desbloqueados #actualiza la lista de personajes desbloqueados en el progreso del usuario sumando los nuevos desbloqueados a los que ya estaban desbloqueados
            progreso [nombre_usuario]["hollow_actual"] = indice_hollow + 1 #desbloquea el siguente hollow
            guardar_progreso(progreso) #guarda el progreso actualizado del usuario en el archivo, el resultado se guarda en la variable progreso
            messagebox.showinfo ("Ganaste!", f"Ganaste! Se suman a tu equipo {len(nuevos_desbloqueados)} nuevos personajes.") #muestra un mensaje de victoria si el jugador gana la batalla, indicando cuantos personajes nuevos se suman a su equipo

            personajes_disponibles = progreso[nombre_usuario].get("personajes_desbloqueados", []) #obtiene la lista de personajes desbloqueados del usuario para mostrarla en la pantalla de seleccion de personajes, si no existe se devuelve una lista vacia, el resultado se guarda en la variable personajes_disponibles
            pantalla_seleccion(nombre_usuario, personajes_disponibles) #regresa a la pantalla de seleccion de personajes para que el jugador pueda elegir su equipo para el siguiente hollow, el resultado se muestra en la ventana principal
            return #termina la funcion Turno cuando el jugador gana
        
        if estado["turno"] == "jugador": #si es el turno del jugador, se realiza el ataque del jugador al hollow, el resultado se compara con "jugador" para verificar de quien es el turno
            btn_atacar.config(state=tk.NORMAL) #activa el boton de atacar para que el jugador pueda realizar su ataque, el resultado se muestra en la ventana
            lbl_log.config(text="Es tu turno. Ataca!") #muestra un mensaje en el log indicando que es el turno del jugador, el resultado se muestra en la etiqueta del log
        else: #si es el turno del hollow, se realiza el ataque del hollow al jugador
            btn_atacar.config(state=tk.DISABLED) #desactiva el boton de atacar para que el jugador no pueda realizar acciones durante el turno del hollow, el resultado se muestra en la ventana
            accion_hollow = random.choice(["atacar", "atacar", "cambiar"]) #el hollow elige aleatoriamente entre atacar o cambiar de personaje, el resultado se guarda en la variable accion_hollow
            if accion_hollow == "cambiar" and len(equipo_hollow) > 1: #si el hollow elige cambiar y tiene mas de un personaje en su equipo, cambia a otro personaje aleatorio del equipo del hollow, el resultado se compara con "cambiar" para verificar la accion del hollow
                disponibles_hollow = [p for p in equipo_hollow if p != estado["personaje_hollow"] and p["vida"] > 0] #crea una lista de personajes disponibles para el hollow que no sean el personaje activo actual y que tengan vida mayor a 0, el resultado se guarda en la variable disponibles_hollow
                if disponibles_hollow: #si hay personajes disponibles para cambiar, el hollow cambia a uno de ellos aleatoriamente, el resultado se compara con la lista de disponibles_hollow para verificar si hay personajes disponibles para cambiar
                    estado ["personaje_hollow"] = random.choice(disponibles_hollow) #cambia el personaje activo del hollow a uno de los personajes disponibles, el resultado se guarda en la clave personaje_hollow del estado
                    lbl_log.config(text=f"{estado['personaje_hollow']['nombre']} ha entrado en la batalla!") #muestra un mensaje en el log indicando que el hollow ha cambiado de personaje,
            else: # hollow ataca
                perdida = calcular_perdida(estado["personaje_hollow"], estado["personaje_jugador"]) #calcula el daño que el hollow le hace al jugador usando la funcion calcular_perdida, el resultado se guarda en la variable perdida
                estado["personaje_jugador"]["vida"] -= perdida #resta la perdida de vida al personaje activo del jugador, el resultado se guarda en la clave vida del personaje activo del jugador en el estado
                lbl_log.config(text=f"{estado['personaje_hollow']['nombre']} atacó a {estado['personaje_jugador']['nombre']} y le hizo {perdida} de daño.") #muestra un mensaje en el log indicando que el hollow ha atacado al

                if  ver_ko(estado["personaje_jugador"], equipo_jugador, equipo_hollow, False): #verifica si el personaje del jugador esta en KO
                    actualizar_pantalla() #turno del jugador de nuevo
                    vivos = [p for p in equipo_jugador if p["vida"] > 0] #crea una lista de personajes del jugador que siguen vivos después del ataque, el resultado se guarda en la variable vivos
                    if vivos:
                        estado ["personaje_jugador"] = vivos[0] #si hay personajes vivos, cambia el personaje activo del jugador al siguiente personaje vivo en la lista, el resultado se guarda en la clave personaje_jugador del estado
                        lbl_log.config(text=f"{estado['personaje_jugador']['nombre']} fue derrotado! {vivos[0]['nombre']} ha entrado en la batalla!")
            actualizar_pantalla() # turno del jugador de nuevo
            estado ["turno"] = "jugador" 
            ventana.after(500, Turno) # espera 500ms para que se vea el log antes de continuar #llamada recursiva para continuar la batalla 
            
    def al_atacar(): #cuando el jugador presiona atacar
        if not estado ["batalla_activa"]:  
            return
        if estado ["turno"] != "jugador":
            return 
        perdida = calcular_perdida(estado ["personaje_jugador"], estado ["personaje_hollow"]) #jugador ataca al personaje del hollow
        estado["personaje_hollow"]["vida"] -= perdida
        lbl_log.config(text=f"{estado['personaje_jugador']['nombre']} Atacó e hizo {perdida} de vida!")

        if ver_ko(estado["personaje_hollow"], equipo_hollow, equipo_jugador, True): #ve si el personaje del hollow quedo en KO
            actualizar_pantalla()
            #busca al proximo personaje del hollow
            vivos_hollow = [p for p in equipo_hollow if p["vida"] > 0]
            if vivos_hollow:
                estado["personaje_hollow"]= vivos_hollow[0]
                
        actualizar_pantalla()

        estado ["turno"] = "hollow" #cambia el turno al hollow
        btn_atacar.config(state=tk.DISABLED)

        ventana.after (800, Turno) #llamada recursiva para continuar con el turno del hollow

    def cambiar_personaje(personaje_nuevo): #permite al jugador cambiar de personaje
        if not estado ["batalla_activa"]:
            return
        if personaje_nuevo == estado ["personaje_jugador"]:
            lbl_log.config(text="Ya esta en la Batalla!")
            return
        if personaje_nuevo["vida"] <= 0:
            lbl_log.config(text="El personaje ya fue derrotado!")
            return
        estado["personaje_jugador"] = personaje_nuevo
        lbl_log.config(text=f"Entró {personaje_nuevo['nombre']}!")
        actualizar_pantalla()

            #se quiere que el personaje gaste el turno
        estado["turno"] = "hollow"
        btn_atacar.config(state = tk.DISABLED)
        ventana.after(800, Turno) #llamada recursiva para que siga el hollow

    btn_atacar.config(command=al_atacar) #conecta al boton de atacar con la funcion al_atacar
    actualizar_pantalla() #crea la pantalla por primera vez
    Turno() #inicia la batalla llamando a turno por primera vez
        
            
            
                    


ventana = tk.Tk() #Se crea la ventana principal del juego
ventana.title("Cartoon's Epic Adventure") #titulo que aparce en la barra superior de la ventana
ventana.geometry("800x600") #tamaño de la ventana
ventana.resizable(False, False) #evita que la ventana se pueda cambiar de tamaño

menu_principal() #se llama a la primera pantalla para que aparezca
ventana.mainloop() #mantiene la ventana abierta y escucha eventos como clicks o entradas de teclado, el resultado se muestra en la ventana principal 
