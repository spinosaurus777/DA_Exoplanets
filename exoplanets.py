# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:55:40 2019

@author: spinosaurus777
"""
import pandas as pd
import matplotlib.pyplot as plt
import os
import math as m

def cargar_datos(nombre_archivo:str)->object:
    """Recibe el nombre de un archivo CSV y lo convierte en un DataFrame.
    Parámetros: 
        nombre_archivo(str): Nombre del archivo CSV que contiene los datos de los palentas.
    Retorno:
        DataFrame(object): DataFrame con los datos de los planetas.
    """
    planetas=pd.read_csv(nombre_archivo)
    return planetas

def distancia_planeta_estrella_KDE(df:object)->None:
    """Crea una gráfica KDE para la distancia entre los planetas y sus estrellas más
    cercanas. Primero, crea la figura para la gráfica. Del DataFrame que recibe como parámetro,
    extrae lo datos relevantes en una serie. Luego, genera la gráfica KDE en la figura
    con los límites en su eje x de 0 y 8500. Le asigna el título y los nombres
    de los ejes a la figura. Por último, lo imprime en pantalla.
    Parámetros:
        df(object): DataFrame con los datos de los planetas.
    """
    plt.figure()
    distancia=df.DISTANCIA_ESTRELLA
    distancia.plot(kind="KDE", figsize=(10, 5), xlim=(0, 8500))
    plt.suptitle("Densidad de probabilidad de distancias planeta-estrella más cercana")
    plt.xlabel("Distancia planeta-estrella más cercana")
    plt.ylabel("Densidad de probabilidad")
    plt.show()
    
    
def descubrimiento_cantidad_hist(df:object)->None:
    """Cra un histograma para la cantidad de planetas descubiertos cada años. Primero, 
    crea la figura para la gráfica. Del DataFrame que recibe como parámetro, extrae lo datos relevantes en
    una serie. Luego, genera en histograma en la figura agrupado en 30 grupos y con los límites 
    en su eje x de 1988 y 2018. Le asigna el título y los nombres
    de los ejes a la figura. Por último, lo imprime en pantalla.
    Parámetros:
        df(object): DataFrame con los datos de los planetas.
    """
    plt.figure()
    año_descubrimiento=df.DESCUBRIMIENTO
    año_descubrimiento.plot(kind="hist", bins=30, figsize=(10,5), xlim=(1988, 2018))
    plt.suptitle("Cantidad de planetas descubiertos entre 1988 y 2018")
    plt.xlabel("Años")
    plt.ylabel("Cantidad de planetas descubiertos")
    plt.show()
    
def descubrimiento_estado_publicacion_box(df:object)->None:
    """Crea un box-plot que relaciona el año de descubrimiento y el tipo de publicación que
    tuvieron los planetas. Primero, crea la figura para la gráfica. Del DataFrame que recibe como paramétro, 
    extrae lo datos relevantes en otro DataFrame. Luego, genera el box-plot en la figura 
    con sus etiquetas rotadas 90°. Le asigna el título y el nombre al eje y de la figura.
    Por último, lo imprime en pantalla.
    Parámetros:
        df(object): DataFrame con los datos de los planetas.
    """
    plt.figure()
    publicacion_año=df.iloc[:, [2, 4]]
    publicacion_año.boxplot(figsize=(8, 8), rot=90, by="ESTADO_PUBLICACION")
    plt.suptitle("Tipo de publicación vs. Año de descubrimiento")
    plt.ylabel("Año de descubrimiento")
    plt.show()
    
def deteccion_descubrimiento_box(df:object)->None:
    """Crea la figura para la gráfica. Del DataFrame que recibe, extrae lo datos relevantes en
    otro DataFrame. Luego, genera el box-plot en la figura con sus etiquetas rotadas 90°.
    Le asigna el título y el nombre al eje y de la figura.
    Por último, lo imprime en pantalla.
    Parámetros:
        df(object): DataFrame con los datos de los planetas.
    """
    plt.figure()
    deteccion_año=df.iloc[:, [2, 5]]
    deteccion_año.boxplot(figsize=(8, 8), rot=90, by="TIPO_DETECCION")
    plt.suptitle("Tipo de detección vs. Año de descubrimiento")
    plt.ylabel("Año de descubrimiento")
    plt.show()
    
def df_y_etiquetas_para_pie(serie:object)->tuple:
    """Crea una tupla con un DataFrame con los tipos de detección y las veces que estos fueron utilizados,
    y una lista con los strings de los nombres de los tipos para ser usados como etiquetas. 
    Recibe una serie con la información relevante para desarrollar las gráficas pie, en este caso,
    el tipo de detección, filtrada o no por un año. Crea un diccionario que tiene como llaves
    todos lo tipos de detección, todas con un valor de 0. Posteriormente, recorre el DataFrame que recibe contando
    las veces que aparece cada tipo de detección en este y asigando ese valor a su repectiva llave en el
    diccionario. Luego, crea un segundo diccionario vacío y una lista vacía. Recorre el primer diccionario, 
    preguntando si el valor de cada llave es mayor a 0, si cumple la condición incluye la llave con su 
    respectivo valor en el segundo diccionario y la llave la añade a la lista. Utilizando el segundo diccionario
    crea un DataFrame con los tipos de detección y la cantidad de veces que fueron utilizados. Por último, 
    crea la tupla con este DataFrame y la lista.
    Parámetros:
        df(object): DataFrame con los tipos de detección, filtrado o no por un año.
    Retorno:
        df_labels(tuple): Tupla con el DataFrame creado y la lista con los tipo de detección que aparecen.
    """
    deteccion={"Astrometry":0, "Imaging":0, "Microlensing":0, "Other":0, 
           "Primary Transit":0, "Primary Transit, TTV":0, "Pulsar":0,
           "Radial Velocity":0, "TTV":0}

    for cada_tipo in serie:
        if cada_tipo=="Astrometry":
            deteccion["Astrometry"]+=1
        elif cada_tipo=="Imaging":
            deteccion["Imaging"]+=1
        elif cada_tipo=="Microlensing":
            deteccion["Microlensing"]+=1
        elif cada_tipo=="Other":
            deteccion["Other"]+=1
        elif cada_tipo=="Primary Transit":
            deteccion["Primary Transit"]+=1
        elif cada_tipo=="Primary Transit, TTV":
            deteccion["Primary Transit, TTV"]+=1
        elif cada_tipo=="Pulsar":
            deteccion["Pulsar"]+=1
        elif cada_tipo=="Radial Velocity":
            deteccion["Radial Velocity"]+=1
        elif cada_tipo=="TTV":
            deteccion["TTV"]+=1
        
    labels=[]
    deteccion2={}
    for cada_llave in deteccion:
        if deteccion[cada_llave]>0:
            deteccion2[cada_llave]=deteccion[cada_llave]
            labels.append(cada_llave)
        
    df_deteccion=pd.DataFrame([[cada_llave, deteccion2[cada_llave]] for cada_llave in deteccion2.keys()],
                           columns=["Tipo deteccion", "Cantidad"])
    
    df_labels=(df_deteccion, labels)
    return df_labels

def deteccion_todos_años(df:object)->None:
    """Crea un gráfica pie que muestra el porcentaje de veces que fueron utilizados los tipo de detección
    en todos los años de los datos. Primero, del DataFrame que recibe como parámetro extrae la columna TIPO_DETECCION
    en una serie. Luego, con la serie utiliza la función df_y_etiquetas_para_pie con el fin 
    de crear una tupla. Crea la figura para la gráfica. Genera la gráfica tipo pie utilizando el primer valor
    de la tupla que es un DataFrame y le asigna las etiquetas a esta utlizando la lista que la tupla tiene como
    segundo valor. Por último, lo imprime en pantalla. 
    Parámetros:
        df(object): DataFrame con los datos de los planetas.
    """ 
    tipo_deteccion=df.TIPO_DETECCION
    df_etiquetas=df_y_etiquetas_para_pie(tipo_deteccion)
    plt.figure()
    df_etiquetas[0].plot(kind="pie", y="Cantidad", figsize=(8, 8), autopct="%1.1f%%",
                  labels=df_etiquetas[1])
    plt.show()
    
def deteccion_año(df:object, año:int)->None:
    """Crea un gráfica pie que muestra el porcentaje de veces que fueron utilizados los tipo de detección
    en el año seleccionado. Primero, filtra el DataFrame que recibe como parámetro a través del año
    recibido como parametro, y extre la columna TIPO_DETECCION en unsa serie. Luego, con la serie utiliza 
    la función df_y_etiquetas_para_pie con el fin de crear una tupla. Crea la figura para la gráfica. 
    Genera la gráfica tipo pie utilizando el primer valor de la tupla que es un DataFrame y le asigna 
    las etiquetas a esta utlizando la lista que la tupla tiene como segundo valor.
    Por último, lo imprime en pantalla.
    Parámetros:
        df(object): DataFrame con los datos de los planetas.
    """
    año_deteccion=df[df.DESCUBRIMIENTO==año]
    tipo_deteccion=año_deteccion.TIPO_DETECCION
    df_etiquetas=df_y_etiquetas_para_pie(tipo_deteccion)
    plt.figure()
    df_etiquetas[0].plot(kind="pie", y="Cantidad", figsize=(8, 8), autopct="%1.1f%%",
                  labels=df_etiquetas[1])
    plt.show()
    
def masa_estrella_KDE_hist(df:object)->None:
    """Crea una figura con el KDE y el histograma de la masa de las estrellas más cercanas a los planetas.
    Primero, crea la fugura para las gráficas. Extrae la columna MASA_ESTRELA del DataFrame que recibe 
    como parametro en una serie. Divide la figura creada anteriormente en dos para cada gráfica.
    Creal ambas gráficas. Les pone títulos y nombres a los ejes. Y lo imprime en pantalla.
    Parámetros:
        df(object): DataFrame con los datos de los planetas.
    """
    plt.figure()
    masa_estrella=df.MASA_ESTRELLA
    fig, axes=plt.subplots(nrows=1, ncols=2)
    masa_estrella.plot(kind="KDE", figsize=(11, 5), xlim=(0, 40), ax=axes[0])
    masa_estrella.plot(kind="hist", figsize=(11, 5), bins=40, xlim=(0, 40), ylim=(0, 100), ax=axes[1])
    axes[0].set_title("Densidad de probabilidad de la masa de las estrellas")
    axes[0].set_xlabel("Masa")
    axes[0].set_ylabel("Densidad de probabilidad")
    axes[1].set_title("Masa vs. Cantidad de estrellas")
    axes[1].set_xlabel("Masa")
    axes[1].set_ylabel("Cantidad de estrellas")
    plt.show()
    
def imagen_cielo(df:object)->None:
    """Crea la imagen del cielo de acuerdo a las coordenadas RA y DEC de los planetas. Primero,
    crea una lista vacía en la cual genera la matriz 100x200 con todos los coponente
    RGB en cero para que todos los píxeles sean negros. Luego, crea tres listas vacías
    (ra, dec, t_deteccio) en las cuales pone cada valor correpondiente de DataFrame que
    recibe como parámetro. Crea otras dos listas vacía, columnas y filas, en las cuales
    agrega los valores resultantes al operar los valore en las listas ra y dec. Recorre
    la lista t_deteccion preguntando que tipo de deteccion hay en cada posición y 
    y utilizando las listas filas y columnas se asigna su color correpondiente en
    su posición en la matriz inicial. Guarda la matriz como imagen en el archivo 
    result.png y lo imprime en pantalla.
    Paramétros: 
        df(object): DataFrame con los datos de los planetas.
    """
    matriz=[]
    for i in range(0,100):
        lista=[]
        for j in range(0, 200):
            a=[0, 0, 0]
            lista.append(a)
        matriz.append(lista)
        
    ra=[]
    for cada_ra in df.RA:
        ra.append(cada_ra)   
    dec=[]
    for cada_dec in df.DEC:
        dec.append(cada_dec)
    t_deteccion=[]
    for cada_tipo in df.TIPO_DETECCION:
        t_deteccion.append(cada_tipo)
        
    columnas=[] 
    filas=[]
    i=0
    while i<len(ra):
        fila=int(99-abs(m.sin(ra[i])*m.cos(dec[i])*100))
        filas.append(fila)
        columna=int(((m.cos(ra[i]))*(m.cos(dec[i]))*100)+100)
        columnas.append(columna)
        i+=1
        
    j=0    
    while j<len(filas):
        if t_deteccion[j]=="Microlensing":
            matriz[filas[j]][columnas[j]]=[0.94, 0.10, 0.10]
        elif t_deteccion[j]=="Radial Velocity":
            matriz[filas[j]][columnas[j]]=[0.1, 0.5, 0.94]
        elif t_deteccion[j]=="Imaging":
            matriz[filas[j]][columnas[j]]=[0.34, 0.94, 0.10]
        elif t_deteccion[j]=="Primary Transit":
            matriz[filas[j]][columnas[j]]=[0.10, 0.94, 0.85]
        elif t_deteccion[j]=="Other":
            matriz[filas[j]][columnas[j]]=[0.94, 0.10, 0.85]
        elif t_deteccion[j]=="Astrometry":
            matriz[filas[j]][columnas[j]]=[0.94, 0.65, 0.10]
        elif t_deteccion[j]=="TTV":
            matriz[filas[j]][columnas[j]]=[1.0, 1.0, 1.0]
        j+=1  

    strFile = "result.png"
    if os.path.isfile(strFile):
        os.remove(strFile)
    plt.imshow(matriz)
    plt.savefig("result.png")
    plt.show()

    

    
    




        
        
