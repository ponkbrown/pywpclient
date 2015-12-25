#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#Un modulo para el pequeño cliente de consola para blogs, sobre todo wordpress
#contiene las funciones:
#    existe() el cual devuelve 0 si el argumento que le pasaste no es un archivo existente
#        y si existe regresa el objeto de el archivo avierto para lectura
#
#    conviertehtml(s) Esta funcion obtiene el texto (s) y regresa el texto convertido a html,
#        si el primer caracter de el texto que no sea blank no es "#" imprime un aviso
# 
# Tue Dec 22 12:03:41 MST 2015

import sys
import markdown

argumentos = sys.argv[1:]   #Agarramos los argumentos enviados al comando menos el mismo comando

def existe(file):
    ''' Regresa el objeto de el archivo abierto si es que existe, de lo contrario imprime
    un error y regresa 0 '''
    try:
        myfile = open(file, 'r+') 
        return myfile
    except IOError:
        print ('No se puede abrir el archivo!')
        return False

def conviertehtml(md):
    ''' Recibe texto y sin hacer pruebas lo convierte de markdown a html5, (avisa nomas si el primer parrafo no es titulo) '''
    html = markdown.markdown(md)
    return html

def sacaTitulo(texto):
    ''' Busca un titulo dentro de el archivo md. las lineas que empiezan con "#" tienen precedencia (despues "##" etc) y despues la que este al principio del archivo, y regresa una cadena que sera el titulo'''
    titulo = ''
    lineas = texto.splitlines()

    if texto.strip().splitlines()[0].strip()[0] != "#":
        print("Parece que la primer linea del archivo no es un titulo!!")

    for linea in lineas[::-1]:
        if linea.strip().startswith('#'):
            titulo = linea.lstrip('#').strip()
            borra = linea
            found = True
    if found:
        lineas.remove(borra)
    contenido = '\n'.join(lineas).strip()

    return (titulo, contenido)
    
if __name__ == "__main__":

    # cuando lo ejecutas desde linea de comandos verifica que cada argumento sea un archivo valido
    # y si es, lo convierte a html y lo imprime a pantalla
    for file in argumentos:
        post = existe(file)
        if post != 0:
            text = post.read()
            titulo, contenido = sacaTitulo(text)
            html = conviertehtml(contenido)

            print(html)
            post.close()
