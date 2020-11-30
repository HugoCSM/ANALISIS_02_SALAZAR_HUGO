# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:34:05 2020

@author: usuario
"""
import csv

lista_datos = []
with open("synergy_logistics_database.csv", "r") as archivo: #Se abre el archivo csv en modo lectura
    lector = csv.DictReader(archivo)      #Se utiliza el archivo como diccionario
    
    for registro in lector:
        lista_datos.append(registro)      #Se recorre el diccionario y se guarada en lista_datos


#OPCIÓN 1 --> Rutas más demandadas

def rutas_export_import(direccion):     #Se crea la función y se mandará como parámetro Exportación o Importación
    contador = 0                        #Se crea la variable contador para guardar el número de veces que aparece la ruta
    rutas_contadas = []
    rutas_conteo = []                   #Se crean listas vacías para utilizar más adelante
    
    for ruta in lista_datos:            #Se recorre la lista             
        if ruta["direction"] == direccion:
            ruta_actual = [ruta["origin"], ruta["destination"]]  #Se guardan las variables a comparar
            
            if ruta_actual not in rutas_contadas: #Realiza el conteo de número de veces que se encuentra la ruta.
                for ruta_bd in lista_datos:      
                    if ruta_actual == [ruta_bd["origin"], ruta_bd["destination"]] and ruta_bd["direction"] == direccion:
                        contador+=1
                
                rutas_contadas.append(ruta_actual)
                rutas_conteo.append([ruta["origin"], ruta["destination"], contador])  #Se agrega la información obtenida a la tabla final
                contador = 0
   
        
    rutas_conteo.sort(reverse = True, key = lambda x:x[2])  #Ordena de mayor a menor el número obtenido de las rutas
    rutas_conteo=rutas_conteo[0:10]   #Aparecen solo las 10 Rutas con más demanda
    return rutas_conteo


conteo_exportaciones = rutas_export_import("Exports")  #Se manda a llamar la función para exportaciones
conteo_importaciones = rutas_export_import("Imports")  #Se manda a llamar la función para importaciones

print("Las 10 rutas con más demanda de exportaciones son: ") #Creado para una mejor visualización de los datos
for rutas_exp in conteo_exportaciones:
    print (rutas_exp)

print("Las 10 rutas con más demanda de importaciones son: ")  #Creado para una mejor visualización de los datos
for rutas_imp in conteo_importaciones :
    print (rutas_imp)

#OPCIÓN 2  --> Valor de medios de transporte

def transporte_valor_exports_import(direccion):    #Se crea la función y se mandará como parámetro Exportación o Importación
    contador = 0                                   #Se crea la variable contador para guardar el número de veces que aparece el medio de transporte
    total=0                                        #Se crea la variable total para guardar la suma del valor por cada medio de transporte
    transporte_contadas = []
    transportes_conteo = []                        #Se crean listas vacías para utilizar más adelante
    
    for ruta in lista_datos:                        #Se recorre la lista
        if ruta["direction"] == direccion:        
            ruta_actual = [ruta["transport_mode"]] #Se guarda la variable a comparar
            
            if ruta_actual not in transporte_contadas: #Realiza el conteo de número de veces que se encuentra el medio de transporte y realiza la suma
                for ruta_bd in lista_datos:
                    if ruta_actual == [ruta_bd["transport_mode"]] and ruta_bd["direction"] == direccion:
                        contador +=1
                        total += int(ruta_bd["total_value"]) #Se convierte el dato a entero para realizar la suma
                
                transporte_contadas.append(ruta_actual)
                transportes_conteo.append([ruta["transport_mode"], contador,total]) #Se agrega la información obtenida a la tabla final
                contador = 0
                total=0
        
    transportes_conteo.sort(reverse = True, key = lambda x:x[2])  #Ordena de mayor a menor el valor total de cada medio de transporte
    transportes_conteo= transportes_conteo[0:3] #Aparecen solo los 3 medios de transporte considerando su valor
    return transportes_conteo
            


transporte_exportaciones = transporte_valor_exports_import("Exports") #Se manda a llamar la función para exportaciones
transporte_importaciones = transporte_valor_exports_import("Imports") #Se manda a llamar la función para importaciones

print("Los 3 medios de transporte más importantes en exportaciones son: ") #Creado para una mejor visualización de los datos
for trans_exp in transporte_exportaciones:
    print (trans_exp)
    
print("Los 3 medios de transporte más importantes en importaciones son: ") #Creado para una mejor visualización de los datos
for trans_imp in transporte_importaciones:
    print (trans_imp)
    
#OPCIÓN 3  -->  Países que le generan el 80% de valor

def paises_exports_imports(direccion):   #Se crea la función y se mandará como parámetro Exportación o Importación
    contador_operaciones=0               #Se guardará cuantas veces aparece el país
    valor_total=0                        #Se guardará el valor total generado por país
    paises_contados=[]
    valor_paises=[]                      #Se crean listas vacías para utilizar más adelante
    
    
    for pais in lista_datos:             #Se recorren listas
        if pais["direction"] == direccion:
            pais_actual= [pais["origin"]] #Se guarda la variable a comparar
            
            if pais_actual not in paises_contados: #Realiza el conteo de número de veces que se encuentra el país y realiza la suma
                for pais_bd in lista_datos:
                    if pais_actual== [pais_bd["origin"]] and pais_bd["direction"]== direccion:
                        contador_operaciones +=1
                        valor_total += int (pais_bd["total_value"]) #Se convierte el dato a entero para realizar la suma
                        
                paises_contados.append(pais_actual)
                valor_paises.append([pais["origin"],valor_total,contador_operaciones]) #Se agrega la información obtenida a la tabla final
                contador_operaciones=0
                valor_total=0
                
    valor_paises.sort(reverse=True, key = lambda x:x[1]) #Ordena de mayor a menor el valor total de cada país
    return valor_paises



def porcentaje_paises_exports_imports (lista_paises, porcentaje = 0.8):    #Se crea la función y se mandará como parámetro Exportación o Importación y el porcentaje para conocer los países que forman parte de dicho porcentaje
    valor=0             #Valor total de las exportaciones o importaciones
    valor_actual=0      #Valor total por país
    paises=[]
    porcentajes_calculados=[]   #Se crean listas vacías para utilizar más adelante
    
    for pais in lista_paises:  #Se recorre la lista
        valor += pais[1]       #Se suma su valor de operación
        
    for pais in lista_paises:   #Se recorre la lista
        valor_actual += pais[1] #Se suma su valor de operación
        porcentaje_actual = round(valor_actual / valor, 3) #Se divide el valor del país de operación entre el valor total para obtener su porcentaje correspondiente
        
        paises.append(pais)
        porcentajes_calculados.append(porcentaje_actual) #Se agrega la información obtenida a la tabla final
        
        if porcentaje_actual <= porcentaje: #Condición para cumplir con el porcentaje deseado
            continue
        else:
            if porcentaje_actual - porcentaje <= porcentajes_calculados[-2] - porcentaje:
                break
            else:
                paises.pop(-1) #Si se rebasa el porcentaje que se desea, se borrará el último elemento sumado
                porcentajes_calculados.pop(-1)
                break
    
    return paises

paises_80_exportaciones = porcentaje_paises_exports_imports(paises_exports_imports("Exports")) #Se manda a llamar la función para exportaciones
paises_80_importaciones = porcentaje_paises_exports_imports(paises_exports_imports("Imports")) #Se manda a llamar la función para importaciones
        
print("Los países que generan el 80% en exportaciones son: ")  #Creado para una mejor visualización de los datos
for pais_exp in paises_80_exportaciones:
    print(pais_exp)

print("Los países que generan el 80% en importaciones son: ")  #Creado para una mejor visualización de los datos
for pais_imp in paises_80_importaciones:
    print(pais_imp)
            
        
    
    


