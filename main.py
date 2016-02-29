#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import md2html
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, EditPost
from wordpress_xmlrpc import WordPressPost


# Obtiene los parametros al comando los archivos a procesar
get_files = sys.argv[1:]

# creamos el objeto wordpress
poodle = Client('http://ponkbrown.com/POODLE/xmlrpc.php', 'poodle', '099eo3')
posts = poodle.call(GetPosts())

for file in get_files:
    post = md2html.existe(file)
    if post:
        entrada = WordPressPost()
        texto = post.read()
        titulo, contenido = md2html.sacaTitulo(texto)
        html = md2html.conviertehtml(contenido)
        entrada.title = titulo
        entrada.content = html
        entrada.id = poodle.call(NewPost(entrada))
        
        print (''' {0}
        {1}'''.format(titulo,contenido))
        publicar = input("¿Quieres Publicarlo? 'Y/N':")
        
        if publicar == ('Y' or 'y'):
            entrada.post_status = 'publish'
            poodle.call(EditPost(entrada.id, entrada)) 
