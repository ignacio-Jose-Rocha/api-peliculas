import json
import biblioteca
from modelos.artista import Artista

class Actor(Artista):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def obtenerPeliculas(self):
        peliculas = biblioteca.Biblioteca.obtenerPeliculas()
        actor_peliculas = []
        try:
            actor_peliculas = [p for p in peliculas if self in p.obtenerActores()]
            print(f"Películas de {self.obtenerNombre()}: {[p.obtenerNombre() for p in actor_peliculas]}")
        except Exception as e:
            print(f"Error al imprimir películas: {e}")
        return actor_peliculas
    
    def obtenerColegas(self):
        colegas = set()
        for pelicula in self.obtenerPeliculas():
            colegas.update(a for a in pelicula.obtenerActores() if a.obtenerId() != self.obtenerId())
        print(f"Colegas de {self.obtenerNombre()}: {[a.obtenerNombre() for a in colegas]}")
        return list(colegas)
    
    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        return self.obtenerNombre() == other.obtenerNombre() and self.obtenerId() == other.obtenerId()

    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": self._mapearGeneros(),
            "peliculas": self._mapearPeliculas(),
            "colegas": self.__mapearColegas()
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "generos": self._mapearGeneros(),
            "peliculas": self._mapearPeliculas(),
            "colegas": self.__mapearColegas()
        }
    
    def __mapearColegas(self):
        colegas = set()
        for pelicula in self.obtenerPeliculas():
            colegas.update(a.obtenerNombre() for a in pelicula.obtenerActores() if a.obtenerId() != self.obtenerId())
        print(f"Colegas de {self.obtenerNombre()}: {[nombre_actor for nombre_actor in colegas]}")
        return list(colegas)