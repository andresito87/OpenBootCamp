/*Crea un nuevo fichero JS que contenga las siguientes líneas

- Una clase llamada "Estudiante" que tenga:

- Una variable llamada nombre

- Otra variable lista llamada asignaturas con 3 asignaturas: Javascript, HTML, CSS

- Un método "obtenDatos" que devuelva un objeto con las propiedades nombre y asignaturas

- Crea una nueva instancia de "Estudiante"

- Haz la llamada al método obtenDatos */

class Estudiante {
    _nombre
    _asignaturas
    constructor(nombre) {
        this.nombre = nombre;
        this.asignaturas = ["Base de datos", "Programacion", "Lenguajes de marcas"];
    }
    obtenDatos() {
        return {
            nombre: this.nombre,
            asignaturas: this.asignaturas,
        };
    }
}

const estudiante = new Estudiante("Andres");
console.log(estudiante.obtenDatos());