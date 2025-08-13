# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:50:36 2019

@author: spinosaurus777
"""
import exoplanets as exo

def ejecutar_cargar_datos()->object:
    """Ejecuta la función cargar datos. Pregunta al usuario el nombre del
    archivo y lo utiliza en dicha función. Muestra en pantalla un mensaje si los
    dato se cargaron o no correctamente.
    Retorno:
        planetas(object): DataFrame con los dato de los planetas. 
    """
    archivo=input("Ingrese el nombre del archivo CSV con los datos de los exoplanetas: ")
    planetas=exo.cargar_datos(archivo)
    if planetas.shape==(0, 0):
        print("El archivo seleccionado no es válido. No se pudieron cargar los datos.")
    else:
        print("Se cargaron los datos correctamente.")
    return planetas

def ejecutar_distancia_planeta_estrella_KDE(df:object)->None:
    """Ejecuta la función distancia_planeta_estrella_KDE.
    """
    exo.distancia_planeta_estrella_KDE(df)
    
def ejecutar_descubrimiento_cantidad_hist(df:object)->None:
    """Ejecuta la función descubrimiento_cantidad_hist.
    """
    exo.descubrimiento_cantidad_hist(df)

def ejecutar_descubrimiento_estado_publicacion_box(df:object)->None:
    """Ejecuta la función descubrimiento_estado_publicacion_box.
    """
    exo.descubrimiento_estado_publicacion_box(df)
    
def ejecutar_deteccion_descubrimiento_box(df:object)->None:
    """Ejecuta la función deteccion_descubrimiento_box.
    """
    exo.deteccion_descubrimiento_box(df)
    
def ejecutar_deteccion_todos_años(df:object)->None:
    """Ejecuta la función detección_todos_años.
    """
    exo.deteccion_todos_años(df)
    
def ejecutar_deteccion_año(df:object)->None:
    """"Ejecuta la función detección año. Le pide al usuario el año que desea
    estudiar para tal fin.
    """
    año=int(input("Ingrese que año que desea analizar: "))
    exo.deteccion_año(df, año)
      
def ejecutar_masa_estrella_KDE_hist(df:object)->None:
    """Ejecuta la función masa_estrella_KDE_hist.
    """
    exo.masa_estrella_KDE_hist(df)
    
def ejecutar_imagen_cielo(df:object)->None:
    """Ejecuta la función imagen_cielo.
    """
    exo.imagen_cielo(df)

def mostrar_menu():
    """Imprime las opciones disponibles para el usuario.
    """
    print("\nOpciones")
    print("1. Cargar archivo de planetas")
    print("2. Gráfica KDE distancia planeta-estrella más cercana")
    print("3. Histograma de la cantidad de planetas descubiertos por año")
    print("4. Box-plot que relacione el año de descubrimiento y el tipo de publicación de los planetas")
    print("5. Box-plot que relacione el año de descubrimiento y el tipo de detección de los planetas")
    print("6. Gráfica pie para los tipos de detección en todos los años")
    print("7. Gráfica pie para los tipo de detección en un año")
    print("8. Comparar histograma y gráfica KDE de la masa de las estrellas más cercanas a los planetas")
    print("9. Crear imagen del cielo")    
    print("10. Salir")


def iniciar_aplicacion():
    """Ejecuta el programa para el usuario.
    """
    
    continuar=True
    while continuar==True:
        mostrar_menu()
        opcion_seleccionada=int(input("Por favor, seleccione una opción: "))
        if opcion_seleccionada==1:
            planetas=ejecutar_cargar_datos()
        elif opcion_seleccionada==2:
            ejecutar_distancia_planeta_estrella_KDE(planetas)
        elif opcion_seleccionada==3:
            ejecutar_descubrimiento_cantidad_hist(planetas)
        elif opcion_seleccionada==4:
            ejecutar_descubrimiento_estado_publicacion_box(planetas)
        elif opcion_seleccionada==5:
            ejecutar_deteccion_descubrimiento_box(planetas)
        elif opcion_seleccionada==6:
            ejecutar_deteccion_todos_años(planetas)
        elif opcion_seleccionada==7:
            ejecutar_deteccion_año(planetas)
        elif opcion_seleccionada==8:
            ejecutar_masa_estrella_KDE_hist(planetas)
        elif opcion_seleccionada==9:
            ejecutar_imagen_cielo(planetas)          
        elif opcion_seleccionada==10:
            continuar=False
        else:
            print("Por favor seleccione una opción válida.")
            
iniciar_aplicacion()
