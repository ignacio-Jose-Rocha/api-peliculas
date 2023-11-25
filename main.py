# Flask
from flask import Flask
from flask_restful import Api

from biblioteca import Biblioteca

# API
from recursos import *

if __name__ == "__main__":
    Biblioteca.inicializar()

    app = Flask(__name__)

    api = Api(app)
    api.add_resource(RecursoActor, '/api/actores/<id>')
    api.add_resource(RecursoActores, '/api/actores')
    api.add_resource(RecursoDirector, '/api/directores/<id>')
    api.add_resource(RecursoDirectores, '/api/directores')
    api.add_resource(RecursoPelicula, '/api/peliculas/<id>')
    api.add_resource(RecursoPeliculas, '/api/peliculas')

    app.run()
