class Artista:
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre

    def establecerNombre(self, nombre):
        self._nombre = nombre

    def obtenerId(self):
        return self._id

    def obtenerNombre(self):
        return self._nombre

    def obtenerGeneros(self):
        generos = []
        for pelicula in self.obtenerPeliculas():
            generos.append(pelicula.obtenerGenero())
        generos = [generos[i] for i in range(len(generos)) if i == generos.index(generos[i])]  # remueve generos duplicados
        return generos
    
    def _mapearGeneros(self):
        generos = self.obtenerGeneros()
        generosMapa = map(lambda g: g.obtenerNombre(), generos)
        return list(generosMapa)

    def _mapearPeliculas(self):
        peliculas = self.obtenerPeliculas()
        peliculasMapa = [{"nombre": p.obtenerNombre(), "anio": p.obtenerAnio()} for p in peliculas]
        print(peliculasMapa)  # Agrega esta línea para imprimir el contenido
        return peliculasMapa