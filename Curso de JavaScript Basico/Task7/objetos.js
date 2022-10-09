/* Crea un archivo llamado objetos.js que contenga las siguientes líneas

- Un objeto con tus datos personales (nombre, apellido, edad, altura, eresDesarrollador)

- Una variable que obtenga tu edad a partir del objeto anterior

- Una lista que contenga el objeto con tus datos personales y un nuevo objeto con los datos personales de tus dos mejores amig@s

- Una nueva lista con los objetos de la lista anterior ordenados por edad, de mayor a menor */

const misDatos = {
    nombre: "Andres",
    apellido: "Podadera",
    edad: 35,
    altura: 1.70,
    eresDesarrollador: true
}

const { edad } = misDatos;

const lista = [
    misDatos,
    {
        nombre: "Francisco",
        apellido: "Matamoros",
        edad: 52,
        altura: 1.60,
        eresDesarrollador: true
    },
    {
        nombre: "Xavi",
        apellido: "Gutierrez",
        edad: 36,
        altura: 1.70,
        eresDesarrollador: true
    }
]

const listaOrdenada = lista.sort((a, b) => b.edad - a.edad);

console.log(listaOrdenada);