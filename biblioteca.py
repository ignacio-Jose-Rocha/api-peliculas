# librerias
import os
import json

# modelos
from modelos.artista import Artista
from modelos.actor import Actor
from modelos.director import Director
from modelos.genero import Genero
from modelos.pelicula import Pelicula


class Biblioteca:
    __archivoDeDatos = "biblioteca.json"
    __actores = []
    __directores = []
    __generos = []
    __peliculas = []

    def inicializar():
        datos = Biblioteca.__parsearArchivoDeDatos()
        Biblioteca.__convertirJsonAListas(datos)

    @classmethod
    def obtenerActores(cls, orden=None, reverso=False):
        actores = cls.__actores.copy()
        if isinstance(orden, str):
            if orden == 'nombre':
                actores.sort(key=lambda x: x.obtenerNombre(), reverse=reverso)
            elif orden == 'colegas':
                actores.sort(key=lambda x: len(x.obtenerColegas()), reverse=reverso)
            elif orden == 'peliculas':
                actores.sort(key=lambda x: len(x.obtenerPeliculas()), reverse=reverso)
        return actores

    @classmethod
    def obtenerDirectores(cls, orden=None, reverso=False):
        directores = cls.__directores.copy()
        if isinstance(orden, str):
            if orden == 'nombre':
                directores.sort(key=lambda x: x.obtenerNombre(), reverse=reverso)
            elif orden == 'peliculas':
                directores.sort(key=lambda x: len(x.obtenerPeliculas()), reverse=reverso)
        return directores

    @classmethod
    def obtenerPeliculas(cls, orden=None, reverso=False):
        peliculas = cls.__peliculas.copy()
        if isinstance(orden, str):
            if orden == 'nombre':
                peliculas.sort(key=lambda x: x.obtenerNombre(), reverse=reverso)
            elif orden == 'director':
                peliculas.sort(key=lambda x: x.obtenerDirector().obtenerNombre(), reverse=reverso)
            elif orden == 'actores':
                peliculas.sort(key=lambda x: len(x.obtenerActores()), reverse=reverso)
            elif orden == 'anio':
                peliculas.sort(key=lambda x: x.obtenerAnio(), reverse=reverso)
        return peliculas

    @classmethod
    def obtenerGeneros(cls, orden=None, reverso=False):
        generos = cls.__generos.copy()
        if isinstance(orden, str):
            if orden == 'nombre':
                generos.sort(key=lambda x: x.obtenerNombre(), reverse=reverso)
        return generos

    @classmethod
    def buscarActor(cls, id):
        for actor in cls.__actores:
            if actor.obtenerId() == id:
                return actor
        return None

    @classmethod
    def buscarDirector(cls, id):
        for director in cls.__directores:
            if director.obtenerId() == id:
                return director
        return None

    @classmethod
    def buscarGenero(cls, id):
        for genero in cls.__generos:
            if genero.obtenerId() == id:
                return genero
        return None

    @classmethod
    def buscarPelicula(cls, id):
        for pelicula in cls.__peliculas:
            if pelicula.obtenerId() == id:
                return pelicula
        return None

    @classmethod
    def __parsearArchivoDeDatos(cls):
        with open(cls.__archivoDeDatos, "r", encoding='utf-8') as archivo:
            return json.load(archivo)
    
    @classmethod
    def __convertirJsonAListas(cls, listas):
        cls.__actores = [Actor(**datos) for datos in listas.get('actores', [])]
        cls.__directores = [Director(**datos) for datos in listas.get('directores', [])]
        cls.__generos = [Genero(**datos) for datos in listas.get('generos', [])]
        cls.__peliculas = [Pelicula(**datos) for datos in listas.get('peliculas', [])]