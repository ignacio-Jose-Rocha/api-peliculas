import json
import biblioteca
from modelos.artista import Artista

class Director(Artista):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def obtenerPeliculas(self):
        return [p for p in biblioteca.Biblioteca.obtenerPeliculas() if self == p.obtenerDirector()]

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": len(self.obtenerGeneros()),
            "peliculas": len(self.obtenerPeliculas()),
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": self._mapearGeneros(),
            "peliculas": self._mapearPeliculas(),
        }