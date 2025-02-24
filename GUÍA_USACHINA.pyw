# FUNDAMENTOS DE PROGRAMACIÓN
# SECCIÓN DEL CURSO: L-22
# PROFESOR DE TEORÍA: CARLOS VERA
# PROFESOR DE LABORATORIO: ALFREDO GONZÁLEZ
# GRUPO: 5

# INTEGRANTES
# 1. AARON DELGADO/RUT: 21996208-8
# 2. ANDRÉS NAVARRETE/RUT: 21838492-7
# 3. THOMAS PONCE/ RUT: 21671459-8
# 4. IGNACIO QUINTANA/ RUT: 21621922-8

# DESCRIPCIÓN DE PROGRAMA: 
"""SOFTWARE DE INTERFAZ GRÁFICA DINÁMICA CON FINES EDUCATIVOS. OFRECE INFORMACIÓN LIGADA A LOCACIONES Y DATOS 
DE LA UNIVERSIDAD DE SANTIAGO (USACH) Y SUS CARRERAS EN LA FACULTAD DE INGENIERÍA. 
ESTA INFORMACIÓN ENFOCA SU RECEPCIÓN EN ESTUDIANTES DE INGENIERÍA EN LA USACH QUE SE ENCUENTREN EN SU PRIMER O SEGUNDO SEMESTRE."""

###### IMPORTACIÓN DE MÓDULOS Y FUNCIONES
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

####### VENTANA PRINCIPAL
ventana = tk.Tk() 
ventana.title("Guía Usachina")
ventana.geometry("800x750+320+50")
ventana.minsize(1000,750)
ventana.resizable(True,True)
ventana.iconbitmap("GUIA-USACH-Port.ico")
ventana.configure(bg="cornflower blue")

######## TÍTULOS
cuadrado = LabelFrame(ventana,bg="sandy brown",height=200,width=400)
título = Label(cuadrado,text="Guía Usachina",font=("Arial Black","20","bold") 
               ,bg="sandy brown",fg="khaki1")

subtítulo = Label(cuadrado,text="Mini motor de búsqueda para estudiantes novatos de Ingeniería USACH"
                  ,font=("Arial","19","bold"),bg="sandy brown",fg="khaki1")
cuadrado.pack(pady=50)
título.pack(pady=10)
subtítulo.pack(pady=10)
####### ÍCONO DE LA PORTADA
imagen_usach = Image.open("GUIA_USACH_Port.png")   
first_imagen = imagen_usach.resize((350, 280))  
imagen_final = ImageTk.PhotoImage(first_imagen)
label_imagen = tk.Label(ventana, image=imagen_final, fg = "khaki1") #Se carga la imagen importada
label_imagen.pack(pady=40)


####### CUADRO DE PREGUNTAS
primus_label = LabelFrame(ventana, text = "Selecciona tu pregunta: ",
                          bg = "sandy brown", fg = "khaki1",
                          font=("Arial",22,"bold"), width=1000, height = 700)
primus_label.pack_propagate(0) ## El cuadro se mantiene con sus dimensiones fijas

def ingresar():
    cuadrado.pack_forget() #pack.forget() permite desaperecer la variable, sin eliminar sus datos
    label_imagen.pack_forget()
    boton_entrada.pack_forget()
    boton_salir.pack_forget()
    primus_label.pack(pady=20)

#Se crean y cargan los botones de entrada y salida
boton_entrada = tk.Button(ventana, text="Ingresar",command=ingresar, bg = "sandy brown", fg = "black", font=("Arial",16,"bold"), height = 1, width =7)
boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy, bg = "sandy brown", fg = "black", font=("Arial",16,"bold"), height = 1, width =4)
boton_entrada.pack(pady=18)
boton_salir.pack(pady=17)


###### PREGUNTAS PRELIMINARES
prime_questions = ["¿Dónde hay servicios de comida alrededor de la USACH?" #subopciones
                   ,"¿Dónde se encuentra la Facultad de Ingeniería?",
                   "¿Qué trámites puedo realizar en los departamentos de la Facultad?",
                   "¿Dónde se ubica el Departamento de Administración y Finanzas?",
                   "¿Dónde se ubica el Departamento de Beneficios Estudiantiles?",
                   "¿Dónde encuentro el Departamento de mi carrera?",#subopciones
                   "¿Dónde puedo encontrar sitios de baño alrededor de la USACH?",#subopciones
                   "¿Qué significan las siglas para sala de mi sistema de horario LOA?"]
respuesta1 = tk.IntVar() #variable de respuesta que reciba entradas de tipo Int
respuesta1.set(0) #Lee 0 por defecto

x = 0
while x < len(prime_questions): #Bucle que lee cada pregunta y le agrega un botón propio
    Radiobutton(primus_label, text = prime_questions[x], bg = "sandy brown", fg = "khaki1"
                , font =("Arial",19,"bold"), variable = respuesta1, value = x+1, height=2).pack()
    x += 1

##### NUEVAS VENTANAS
labelframe = LabelFrame(ventana, text = "Locales de Almuerzos y Comida en la USACH",
                        bg = "sandy brown",fg = "khaki1",
                        font=("Arial",18,"bold"), width=450, height = 300)
####### LISTA COMBOBOX PARA COMIDA
combobox1 = ttk.Combobox(labelframe,width=70, font=("Arial",18),foreground="black"
                        ,background="white")
lugares_menu = [ "Casino Central","Casino Heisenberg",
                    "Casino EAO","Cafetería ED","Cafeterías EAO",
                  "Local El Faraón", "Local Pizzas XL"]
combobox1["values"]= lugares_menu

###### LISTA COMBOBOX PARA INGENIERÍA 
lugares_departamentos = ["Departamento de Ing. Informática", "Departamento de Ing. Industrial", "Departamento de Ing. Mecánica"
                         , "Departamento de Ing. Eléctrica", "Departamento de Ing. Química y Bioprocesos", "Departamento de Ing. Geospacial y Ambiental", 
                        "Departamento de Ing. Biomédica ", "Departamento de Ing. en Obras Civíles",
                          "Departamento de Ing. de Minas", "Departamento de Ing. Metalúrgica"]
label_ingenieria = LabelFrame(ventana, text = "Departamentos de Ingeniería de la FIING",
                        bg = "sandy brown",fg = "khaki1",
                        font=("Arial",18,"bold"), width=450, height = 300)
combobox2 = ttk.Combobox(label_ingenieria,width=70, font=("Arial",18),foreground="black"
                        ,background="white")
combobox2["values"]= lugares_departamentos


####### LISTA COMBOBOX PARA BAÑOS
lugares_banos = ["Baños ED", "Baños Casino Central", "Baños PAIEP", "Baños Departamentos de Ingenierías"]
label_banos = LabelFrame(ventana, text= "Baños Principales USACH", 
                         bg = "sandy brown",fg = "khaki1",
                        font=("Arial",18,"bold"), width=450, height=300)
combobox3 = ttk.Combobox(label_banos,width=70, font=("Arial",18),foreground="black"
                        ,background="white")
combobox3["values"]= lugares_banos

##### IMAGENES UNICA RESPUESTA

imagen_fiing = Image.open("FACULTAD_INGENERIA.png")
imagen_fiing1 = imagen_fiing.resize((500, 450))
imagen_fiing_final = ImageTk.PhotoImage(imagen_fiing1)

###### IMAGEN FINANZAS
imagen_finanzas = Image.open("VICERRECTORIA_FINANZAS.png")
imagen_finanzas1 = imagen_finanzas.resize((500, 450))
imagen_finanzas_final = ImageTk.PhotoImage(imagen_finanzas1)


###### IMAGEN BENEFICIOS ESTUDIANTILES
imagen_beneficios = Image.open("BENEFICIOS_ESTUDIANTILES.png")
imagen_beneficios1 = imagen_beneficios.resize((500, 450))
imagen_beneficios_final = ImageTk.PhotoImage(imagen_beneficios1)


frameII = Frame(ventana,bg = "sandy brown",
                width=450,height = 300)
CanvasI = Canvas(frameII,width=500,height = 450)



###### ETIQUETA PARA OPCIONES ÚNICAS
label_unico = LabelFrame(ventana, text="Respuesta", font=("Arial",20,"bold"),height=630,width=1080,
                         bg = "sandy brown",fg = "khaki1")
label_unico.pack_propagate(0)
facultad_descripcion = "La Facultad de Ingeniería de la Universidad de Santiago se encuentra en la calle \nLas Sophoras 165, 8320000 de Santiago, Estación Central. Es una edificación \nperteneciente a los alrededores de la Casa Central de la USACH, siendo aledaña \na la Vicerrectoría de Posgrado y a la Sala Christian Yáñez. La Facultad de \nIngeniería es una infraestructura destinada a gestionar las divisiones y \nactividades académicas pertenecientes a las carreras de Ingeniería de la USACH."
facultad_ing = Label(label_unico,text=facultad_descripcion,
                     font=("Arial",18,"bold"),height=500,width=650,bg = "sandy brown",fg = "khaki1" )

###### TRAMITES

tramites_descripcion = "Los departamentos pertenecientes a cada carrera de la Facultad de Ingeniería \ntienen el propósito de representar al equipo académico y estudiantil de \ncada carrera de Ingeniería. En estos departamentos se efectúan clases enfocadas \nen la respectiva especialidad, permitiendo la convivencia entre profesores y estudiantes; \ntanto en el ambiente de pregrado como de posgrado. \n\nDe este modo, cada departamento cuenta con sus propias salas de clases, salas de estudio \ny laboratorios al servicio del estudiantado y del equipo docente. \nHabiendo un total 10 departamentos de Ingeniería \nen la Universidad de Santiago."

tramites = Label(label_unico,text=tramites_descripcion,
                     font=("Arial",18,"bold"), bg = "sandy brown",fg = "khaki1" )

######### FINANZAS

finanzas_descripcion = "El Departamento de Administración y Finanzas de la USACH, \nestá ubicada en la calle Enrique Kirberg 10, Estación Central, Santiago. \nEsta unidad se encarga de trámites como la gestión de pagos, \nconvenios para aranceles de matrículas, \nsolicitudes de documentos financieros, \nregularización de cambios académicos y otros trámites universitarios."

finanzas = Label(label_unico,text=finanzas_descripcion,
                     font=("Arial",18,"bold"), bg = "sandy brown",fg = "khaki1" )
        

######### BENEFICIOS

beneficios_descripcion = "El Departamento de Beneficios Estudiantiles de la USACH, \nestá ubicado en la Escuela de Artes y Oficios, \ncon dirección en Av. Víctor Jara 9170124, Estación Central, Santiago. \nEsta unidad brinda apoyo a los estudiantes \nproporcionando soluciones socioeconómicas \npara el financiamiento de sus estudios."

beneficios = Label(label_unico,text=beneficios_descripcion,
                     font=("Arial",18,"bold"), bg = "sandy brown",fg = "khaki1" )

#### LOA

loa_descripcion = "ED: Edificio de Innovación Docente.\nEAO: Escuela de Artes y Oficios.\nFIS: Laboratorios de Departamentos de Física.\nEPF: Edificio Pabellón Forma.\nELE: Departamento de Ingeniería Eléctrica.\nIND: Departamento de Ingeniería Industrial.\nFACIMED: Facultad de Ciencias Médicas."
loa = Label(label_unico,text=loa_descripcion,
            font=("Arial",18,"bold"),bg= "sandy brown",fg = "khaki1")

####### FUNCIÓN QUE GUÍA LOS CAMBIOS AL ESCOGER LAS PREGUNTAS TIPO RADIOBUTTON
def entrar_ventana(*args):
    answer = respuesta1.get()
    if answer == 1:
        primus_label.pack_forget()
        labelframe.pack(padx = 5, pady = 20)
        combobox1.pack()
        

    if answer == 2:
        frameII.pack()
        CanvasI.pack(pady=30)  
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_fiing_final)
        primus_label.pack_forget()
        label_unico.pack(padx = 5, pady = 20)
        facultad_ing.place(relx=0.5, rely=0.8, anchor= "center")
        facultad_ing.pack(padx = 4, pady = 15)
        

    if answer == 3:
        primus_label.pack_forget()
        label_unico.pack(padx = 5, pady = 20)
        tramites.place(relx=0.5, rely=0.8, anchor= "center")
        tramites.pack(padx = 4, pady = 15)

    if answer == 4:
        frameII.pack()
        CanvasI.pack(pady=30)  
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_finanzas_final)
        primus_label.pack_forget()
        label_unico.pack(padx = 5, pady = 20)
        finanzas.place(relx=0.5, rely=0.8, anchor= "center")
        finanzas.pack(padx=4,pady=15)
        
        
    if answer == 5:
        frameII.pack()
        CanvasI.pack(pady=30)  
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_beneficios_final)
        primus_label.pack_forget()
        label_unico.pack(padx = 5, pady = 20)
        beneficios.place(relx=0.5, rely=0.8, anchor= "center")
        beneficios.pack(padx=4,pady=15)
        
        
    if answer == 6:
        primus_label.pack_forget()
        label_ingenieria.pack(padx = 5, pady = 20)
        combobox2.pack()
        
        
    if answer == 7:
        primus_label.pack_forget()
        label_banos.pack(padx = 5, pady = 20)
        combobox3.pack()
        
        
    if answer == 8:
        primus_label.pack_forget()
        label_unico.pack(padx = 5, pady = 20)   
        loa.place(relx=0.5, rely=0.8, anchor= "center")
        loa.pack(padx=4,pady=15)
        
        
mark0 = respuesta1.trace("w",entrar_ventana)

###### IMAGEN DE COMIDAS
imagen_casino = Image.open("CASINO_CENTRAL.png")
imagen_casino1 = imagen_casino.resize((500, 450))
imagen_casino_final = ImageTk.PhotoImage(imagen_casino1)

imagen_heisen = Image.open("CASINO_HEISENBERG.png")
imagen_heisen1 = imagen_heisen.resize((500, 450))
imagen_heisen_final = ImageTk.PhotoImage(imagen_heisen1)


imagen_casino_eao = Image.open("CASINO_EAO.png")
imagen_casino_eao1 = imagen_casino_eao.resize((500, 450)).rotate(270)
imagen_casino_eao_final = ImageTk.PhotoImage(imagen_casino_eao1)

imagen_cafeteria_ed = Image.open("CAFETERIA_ED.png")
imagen_cafeteria_ed1 = imagen_cafeteria_ed.resize((500, 450))
imagen_cafeteria_ed_final = ImageTk.PhotoImage(imagen_cafeteria_ed1)

imagen_cafeteria_eao = Image.open("CAFETERIA_EAO.png")
imagen_cafeteria_eao1 = imagen_cafeteria_eao.resize((500, 450))
imagen_cafeteria_eao_final = ImageTk.PhotoImage(imagen_cafeteria_eao1)

imagen_faraon = Image.open("FARAON.png")
imagen_faraon1 = imagen_faraon.resize((500, 450))
imagen_faraon_final = ImageTk.PhotoImage(imagen_faraon1)

imagen_pizzas = Image.open("PIZZAS_XL.png")
imagen_pizzas1 = imagen_pizzas.resize((500, 450))
imagen_pizzas_final = ImageTk.PhotoImage(imagen_pizzas1)

##### IMAGEN DE DEPARTAMENTOS

imagen_diinf = Image.open("DEPARTAMENTO_ING_INFORMATICA.png")
imagen_diinf1 = imagen_diinf.resize((500, 450))
imagen_diinf_final = ImageTk.PhotoImage(imagen_diinf1)

imagen_industrial = Image.open("DEPARTAMENTO_INDUSTRIAL.png")
imagen_industrial1 = imagen_industrial.resize((500, 450))
imagen_industrial_final = ImageTk.PhotoImage(imagen_industrial1)

imagen_mecanica = Image.open("DEPARTAMENTO_MECANICA.png")
imagen_mecanica1 = imagen_mecanica.resize((500, 450))
imagen_mecanica_final = ImageTk.PhotoImage(imagen_mecanica1)

imagen_electrica = Image.open("DEPARTAMENTO_ING_ELECTRICA.png")
imagen_electrica1 = imagen_electrica.resize((500, 450))
imagen_electrica_final = ImageTk.PhotoImage(imagen_electrica1)

imagen_quimica = Image.open("DEPARTAMENTO_ING_QUIMICA.png")
imagen_quimica1 = imagen_quimica.resize((500, 450))
imagen_quimica_final = ImageTk.PhotoImage(imagen_quimica1)

imagen_geomatica = Image.open("DEPARTAMENTO_GEOESPACIAL_AMBIENTAL.png")
imagen_geomatica1 = imagen_geomatica.resize((500, 450))
imagen_geomatica_final = ImageTk.PhotoImage(imagen_geomatica1)


imagen_biomedica = Image.open("DEPARTAMENTO_BIOMEDICA.png")
imagen_biomedica1 = imagen_biomedica.resize((500, 450))
imagen_biomedica_final = ImageTk.PhotoImage(imagen_biomedica1)

imagen_obras = Image.open("DEPARTAMENTO_ING_OBRAS.png")
imagen_obras1 = imagen_obras.resize((500, 450))
imagen_obras_final = ImageTk.PhotoImage(imagen_obras1)

imagen_minas = Image.open("DEPARTAMENTO_ING_MINAS.png")
imagen_minas1 = imagen_minas.resize((500, 450))
imagen_minas_final = ImageTk.PhotoImage(imagen_minas1)

imagen_metalurgia = Image.open("DEPARTAMENTO_METALURGIA.png")
imagen_metalurgia1 = imagen_metalurgia.resize((500, 500))
imagen_metalurgia_final = ImageTk.PhotoImage(imagen_metalurgia1)


######### IMAGEN DE BAÑOS

imagen_banos_ed = Image.open("BANO_ED.png")
imagen_banos_ed1 = imagen_banos_ed.resize((500, 450))
imagen_banos_ed_final = ImageTk.PhotoImage(imagen_banos_ed1)

imagen_banos_cc = Image.open("BANO_EAO.png")
imagen_banos_cc1 = imagen_banos_cc.resize((500, 450))
imagen_banos_cc1 = imagen_banos_cc1.rotate(270)
imagen_banos_cc_final = ImageTk.PhotoImage(imagen_banos_cc1)

imagen_banos_paiep = Image.open("BANO_AZUL.png")
imagen_banos_paiep1 = imagen_banos_paiep.resize((500, 450))
imagen_banos_paiep_final = ImageTk.PhotoImage(imagen_banos_paiep1)

imagen_banos_depas = Image.open("BANO_GEOESPACIAL.png")
imagen_banos_depas1 = imagen_banos_depas.resize((500, 450))
imagen_banos_depas_final = ImageTk.PhotoImage(imagen_banos_depas1)


frameII = Frame(ventana,bg = "sandy brown",
                width=450,height = 300)
CanvasI = Canvas(frameII,width=500,height = 450)


texto_label = None  #Esta variable almacenará la última etiqueta creada
#FUNCIÓN QUE GUÍA LOS CAMBIOS EN COMBOBOX DE COMIDAS
def crear_ventana(*args):
    global texto_label  #Declaramos la variable como global para poder modificarla
    
    #Destruir la etiqueta anterior si existe
    if texto_label:
        texto_label.destroy()

    seleccion = combobox1.get()
    if seleccion == lugares_menu[0]:
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_casino_final)
        texto_label = tk.Label(ventana, text="Casino Central:\nEs un Casino posicionado al centro de la EAO. Dispone de minutas semanales,\nalmuerzos tradicionales y flexitarianos.", 
                                bg="sandy brown", font=("Arial", 14,"bold"), fg="white") 
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")

    if seleccion == lugares_menu[1]:
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_heisen_final)
        texto_label = tk.Label(ventana, text="Casino Heisenberg:\nEs un Casino posicionado cerca de la Facultad de Ingeniería Química\n y Bioprocesos, en Casa Central. Dispone de minutas semanales y cómida rápida."
                               , bg="sandy brown", font=("Arial",14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")

    if seleccion == lugares_menu[2]:
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_casino_eao_final)
        texto_label = tk.Label(ventana, text="Casino EAO:\nEs un Casino aledaño al Casino Central, en el centro de la EAO. Dispone de minutas semanales,\n almuerzos tradicionales, vegetarianos y venta de snacks.", 
                               bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")


    if seleccion == lugares_menu[3]:
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_cafeteria_ed_final)
        texto_label = tk.Label(ventana, text="Cafetería ED:\nEs una cafetería dispuesta al interior del Edificio de Desarrollo e Innovación Docente (ED).\nEste negocio ofrece sus servicios al estudiantado y docentes de la FIING que tienen clases en el edificio. \nVende bebidas, snacks y sandwiches.", 
                               bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")

    if seleccion == lugares_menu[4]:
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_cafeteria_eao_final)
        texto_label = tk.Label(ventana, text="Cafetería EAO:\nEs una cafetería del centro de la EAO. Su venta principal son las bebidas, snacks y sandwiches.", 
                               bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")

    if seleccion == lugares_menu[5]:
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_faraon_final)
        texto_label = tk.Label(ventana, text="Local El Faraón:\nEs un local de comida rápida dispuesto frente a la Biblioteca Central, en Enrique Kirberg con Victor Jara.\nSu venta son la cómida rápida (Papas Fritas y Completos, en su mayoría)."
                               , bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")

    if seleccion == lugares_menu[6]:
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_pizzas_final)
        texto_label = tk.Label(ventana, text="Local Pizzas XL:\nEs un local de comida rápida dispuesto al lado del Edificio de Desarrollo e Innovación Docente (ED),\nen Av. Victor Jara. Su venta principal son las Pizzas, Papas Fritas y Nuggets.", 
                               bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")


combobox1.bind("<<ComboboxSelected>>", crear_ventana)#Función para reconocer el input insertado a combobox


#FUNCIÓN QUE GUÍA LOS CAMBIOS DEL COMBOBOX PARA INGENIERÍAS
def ventanas_ingenieria(*args):
    global texto_label  #Declaramos la variable como global para poder modificarla
    
    #Destruir la etiqueta anterior si existe
    if texto_label:
        texto_label.destroy()
    answer = combobox2.get()
    if answer == lugares_departamentos[0]:#Informática
        descripcion= """Departamento de Ingeniería Informática:
        El Departamento de Ingeniería Informática (DIINF) de la USACH es la edificación académica en donde se imparten 
        los ramos destinados a las carreras de Ingeniería Civil en Informática e Ingeniería de Ejecución en Computación 
        e Informática. El DIINF se localiza en la zona de Campus externa a la Calle El Belloto, anexa al Aula Magna."""
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_diinf_final)
        texto_label = tk.Label(ventana, text=descripcion, bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")  
    if answer == lugares_departamentos[1]:#Industrial
        descripcion="""Departamento de Ingeniería Industrial:
        El Departamento de Ingeniería Industrial (IND) de la USACH es la edificación académica 
        en donde se imparten los ramos destinados a las carreras de Ingeniería Civil Industrial 
        e Ingeniería de Ejecución Industrial. El IND está ubicado en Avenida Víctor Jara 3769, 
        en la comuna de Estación Central."""
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_industrial_final)
        texto_label = tk.Label(ventana, text=descripcion, bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center") 
    if answer == lugares_departamentos[2]:#Mecánica
        descripcion="""Departamento de Ingeniería Mecánica:
        El Departamento de Ingeniería Mecánica (MEC) de la USACH es la edificación académica en donde se imparten 
        distintos ramos relacionados a las carreras de Ingeniería Civil Mecánica, Ingeniería de Ejecución Mecánica 
        e Ingeniería de Ejecución en Climatización. El MEC se localiza en la zona norte del campus Casa Central de la 
        USACH, externa a la calle Las Sophoras 175."""
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_mecanica_final)
        texto_label = tk.Label(ventana, text=descripcion, bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center") 
    if answer == lugares_departamentos[3]:#Eléctrica
        descripcion ="""Departamento de Ingeniería Eléctrica:
        El Departamento de Ingeniería Eléctrica (DIE) de la USACH es la
        edificación académica en donde se imparten los ramos destinados a las carreras de Ingeniería Civil en Electricidad, 
        Ingeniería en Ejecución en Electricidad e Ingeniería Civil en Telemática. 
        El DIE se localiza en la calle Av. Victor Jara N° 3519."""
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_electrica_final)
        texto_label = tk.Label(ventana, text=descripcion, bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center") 
    if answer == lugares_departamentos[4]:#Química
        descripcion ="""Departamento de Ingeniería Química y Bioprocesos:
        El Departamento de Química y Bioprocesos (DIQB) de la USACH es la
        edificación académica en donde se imparten los ramos destinados a las carreras de Ingeniería Civil Química,
        Ingeniería de Ejecución Química e Ingeniería Civil en Biotecnología."""
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_quimica_final)
        texto_label = tk.Label(ventana, text=descripcion, bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center") 
    if answer == lugares_departamentos[5]:#Geoespacial
        descripcion ="""Departamento de Ingeniería Geoespacial y Ambiental:
        El DIGEA de la USACH es la edificación académica en donde se imparten los ramos destinados a las carreras 
        de Ingeniería Civil en Geomensura y Geomática, Ingeniería Civil en Ambiente e Ingeniería Civil en
        Territorio y Medio Ambiente."""
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_geomatica_final)
        texto_label = tk.Label(ventana, text=descripcion, bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center") 
    if answer == lugares_departamentos[6]:#Biomédica
        descripcion ="""Departamento de Ingeniería Biomédica:
        El Departamento de Ingeniería Biomédica de la USACH es la edificación académica 
        en donde se imparten los ramos destinados a la carrera de Ingeniería Civil Biomédica.
        Se localiza en el Patio de los Perros, aledaña al centro de la EAO."""
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_biomedica_final)
        texto_label = tk.Label(ventana, text=descripcion, bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center") 
    if answer == lugares_departamentos[7]:#Obras Civiles
        descripcion ="""Departamento de Ingeniería en Obras Civiles:
        El Departamento de Ingeniería en Obras Civiles de la USACH es la edificación académica
        en donde se imparten los ramos destinados a la carrera de Ingeniería Civil en Obras Civiles.
        Se localiza en el Patio de los Perros, aledaña al centro de la EAO."""
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_obras_final)
        texto_label = tk.Label(ventana, text=descripcion, bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center") 
    if answer == lugares_departamentos[8]:#Minas
        descripcion ="""Departamento de Ingeniería en Minas:
        El Departamento de Ingeniería en Minas (DIM) de la USACH es la edificación académica
        en donde se imparten los ramos destinados a las carreras de Ingeniería Civil en Minas
        e Ingeniería de Ejecución en Minas. Se localiza en Casa Central, aledaña al Departamento de
        Matemáticas y Ciencias de la Computación, en la calle Las Sophoras 165, 8320000 de Estación Central."""
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_minas_final)
        texto_label = tk.Label(ventana, text=descripcion, bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center") 
    if answer == lugares_departamentos[9]:#Metalurgia
        descripcion ="""Departamento de Ingeniería en Metalurgia:
        El Departamento de Ingeniería en Metalurgia de la USACH es la
        edificación académica en donde se imparten los ramos destinados a las carreras de Ingeniería Civil en
        Metalurgia e Ingeniería de Ejecución en Metalurgia. Se localiza en el centro de la EAO, 
        al frente del Aula Magna y el Departamento de Ingeniería Informática."""
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_metalurgia_final)
        texto_label = tk.Label(ventana, text=descripcion, bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")

combobox2.bind("<<ComboboxSelected>>", ventanas_ingenieria)

#FUNCIÓN QUE CONTROLA LOS CAMBIOS EN EL COMBOBOX PARA BAÑOS
def ventana_banos(*args):
    global texto_label #Declaramos la variable como global para poder modificarla
    
    # Destruir la etiqueta anterior si existe
    if texto_label:
        texto_label.destroy()

    seleccion = combobox3.get()
    if seleccion == lugares_banos[0]:
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_banos_ed_final)
        texto_label = tk.Label(ventana, text="Baños ED: \nAl lado este, desde el nivel 1 hasta el 8, se ubican los baños del Edificio De Innovación Docente.", 
                                bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")

    if seleccion == lugares_banos[1]:
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_banos_cc_final)
        texto_label = tk.Label(ventana, text="Baños Casino Central (EAO): \nEstán ubicados al lado este del Casino Central.", 
                               bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")

    if seleccion == lugares_banos[2]:
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_banos_paiep_final)
        texto_label = tk.Label(ventana, text="Baños PAIEP: \nEstán ubicados afuera del edificio PAIEP, al lado este. \nSe puede identificar con un techo rojo sostenido por barras azules.", 
                               bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")
    if seleccion == lugares_banos[3]:
        frameII.pack()
        CanvasI.pack(pady=30)
        CanvasI.create_image(0, 0, anchor=tk.NW, image=imagen_banos_depas_final)
        texto_label = tk.Label(ventana, text="Baños Departamentos: \nCada departamento contiene sus propios baños para estudiantes.", 
                               bg="sandy brown", font=("Arial", 14,"bold"), fg="white")
        texto_label.place(relx=0.5, rely=0.8, anchor= "center")
 
combobox3.bind("<<ComboboxSelected>>", ventana_banos)

ventana.mainloop()  

     

