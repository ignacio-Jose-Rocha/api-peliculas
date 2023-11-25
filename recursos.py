from flask_restful import Resource
from flask import request

import json

import biblioteca

from modelos.actor import Actor
from modelos.director import Director
from modelos.pelicula import Pelicula


class RecursoActor(Resource):

    def get(self, id):
        actor = biblioteca.Biblioteca.buscarActor(id)
        if isinstance(actor, Actor):
            return json.loads(json.dumps(actor.convertirAJSONFull())), 200
        else:
            return {"error": "Actor no encontrado"}, 404


class RecursoActores(Resource):

    def get(self):
        orden = request.args.get('orden')
        if (orden):
            reverso = request.args.get('reverso')
            actores = biblioteca.Biblioteca.obtenerActores(
                orden=orden, reverso=reverso == 'si')
        else:
            actores = biblioteca.Biblioteca.obtenerActores()
        return json.loads(json.dumps(actores, default=lambda o: o.convertirAJSON())), 200


class RecursoDirector(Resource):

    def get(self, id):
        director = biblioteca.Biblioteca.buscarDirector(id)
        if isinstance(director, Director):
            return json.loads(json.dumps(director.convertirAJSONFull())), 200
        else:
            return {"error": "Director no encontrado"}, 404


class RecursoDirectores(Resource):

    def get(self):
        orden = request.args.get('orden')
        if (orden):
            reverso = request.args.get('reverso')
            directores = biblioteca.Biblioteca.obtenerDirectores(
                orden=orden, reverso=reverso == 'si')
        else:
            directores = biblioteca.Biblioteca.obtenerDirectores()
        return json.loads(json.dumps(directores, default=lambda o: o.convertirAJSONFull())), 200


class RecursoPelicula(Resource):

    def get(self, id):
        pelicula = biblioteca.Biblioteca.buscarPelicula(id)
        if isinstance(pelicula, Pelicula):
            return json.loads(json.dumps(pelicula.convertirAJSONFull())), 200
        else:
            return {"error": "Pelicula no encontrada"}, 404


class RecursoPeliculas(Resource):

    def get(self):
        orden = request.args.get('orden')
        if (orden):
            reverso = request.args.get('reverso')
            peliculas = biblioteca.Biblioteca.obtenerPeliculas(
                orden=orden, reverso=reverso == 'si')
        else:
            peliculas = biblioteca.Biblioteca.obtenerPeliculas()
        return json.loads(json.dumps(peliculas, default=lambda o: o.convertirAJSON())), 200
