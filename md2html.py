#! /usr/bin/env python3

# -*- coding: utf-8 -*-


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
        return 0

def conviertehtml(md):
    ''' Recibe texto y sin hacer pruebas lo convierte de markdown a html5, (avisa nomas si el primer parrafo no es titulo) '''
    html = markdown.markdown(md)
    return html

    
for file in argumentos:
    post = existe(file)
    if post != 0:
        text = post.read()
        html = conviertehtml(text)
        print(html)




