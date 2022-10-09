/*  Crea un archivo JS que contenga las siguientes líneas

- Una variable que contenga la lista de la compra (mínimo 5 elementos)

- Modifica la lista de la compra y añádele "Aceite de Girasol"

- Vuelve a modificar la lista de la compra eliminando "Aceite de Girasol"

- Una lista de tus 3 películas favoritas (objetos con propiedades: titulo, director, fecha)

- Una nueva lista que contenga las películas posteriores al 1 de enero de 2010 (utilizando filter)

- Una nueva lista que contenga los directores de la lista de películas original (utilizando map)

- Una nueva lista que contenga los títulos de la lista de películas original (utilizando map)

- Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando concat)

- Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando el factor de propagación) */


let listaCompra = ["Leche", "Huevos", "Pan", "Queso", "Patatas"];
listaCompra.push("Aceite de Girasol");
listaCompra.pop();

let peliculas = [
    {
        titulo: "Troya",
        director: "Wolfgang Petersen",
        fecha: 2004
    },
    {
        titulo: "Gladiator",
        director: "Ridley Scott",
        fecha: 2000
    },
    {
        titulo: "El señor de los anillos: El retorno del rey",
        director: "Peter Jackson",
        fecha: 2003
    }
];

let peliculasPost2010 = peliculas.filter(pelicula => pelicula.fecha > 2010);
let directores = peliculas.map(pelicula => pelicula.director);
let titulos = peliculas.map(pelicula => pelicula.titulo);
let directoresYTitulos = directores.concat(titulos);
let directoresYTitulosSpread = [...directores, ...titulos];

console.log(listaCompra, peliculas, peliculasPost2010, directores, titulos, directoresYTitulos, directoresYTitulosSpread);