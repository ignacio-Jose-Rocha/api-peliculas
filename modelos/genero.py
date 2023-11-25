import json


class Genero:
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre

    def obtenerId(self):
        return self._id

    def obtenerNombre(self):
        return self._nombre

    def __repr__(self):
        return json.dumps({
            "nombre": self.obtenerNombre()
        })

    def convertirAJSON(self):
        return {
            "nombre": self.obtenerNombre()
        }
