import json
import biblioteca

class Pelicula:
    def __init__(self, id, nombre, genero, director, actores, anio):
        self._id = id
        self._nombre = nombre
        self._genero = genero
        self._director = director
        self._actores = actores
        self._anio = anio

    def establecerNombre(self, nombre):
        self._nombre = nombre
           
    def establecerGenero(self, genero):
        self._genero = genero
    
    def establecerDirector(self, director):
        self._director = director
        
    def establecerActores(self, actores):
        self._actores = actores
    
    def establecerAnio(self, anio):
        self._anio = anio

    def obtenerId(self):
        return self._id

    def obtenerNombre(self):
        return self._nombre    

    def obtenerGenero(self):
        genero = biblioteca.Biblioteca.buscarGenero(self._genero)
        if genero is None:
            raise ValueError(f"No se encontró el género con ID: {self._genero}")
        return genero

    def obtenerDirector(self):
        director = biblioteca.Biblioteca.buscarDirector(self._director)
        if director is None:
            raise ValueError(f"No se encontró el director con ID: {self._director}")
        return director

    def obtenerActores(self):
        actores = [biblioteca.Biblioteca.buscarActor(actor["id"]) for actor in self._actores]
        actores_validos = [actor for actor in actores if actor is not None]
        print(f"Actores en {self.obtenerNombre()}: {[actor.obtenerNombre() for actor in actores_validos]}")
        return actores_validos

    def obtenerAnio(self):
        return self._anio

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "director": self.obtenerDirector().obtenerNombre(),
            "actores": len(self.obtenerActores()),
            "anio": self._anio
        }

    def convertirAJSONFull(self):
        return {
            "nombre": self.obtenerNombre(),
            "genero": self.obtenerGenero().obtenerNombre(),
            "director": self.obtenerDirector().obtenerNombre(),
            "actores": self.__mapearActores(),
            "anio": self._anio
        }
    
    def __mapearActores(self):
        actores = self.obtenerActores()
        actoresMapa = map(lambda a: a.obtenerNombre(), actores)
        return list(actoresMapa)

    def __eq__(self, other):
            if not isinstance(other, Pelicula):
                return False
            return self.obtenerId() == other.obtenerId()
