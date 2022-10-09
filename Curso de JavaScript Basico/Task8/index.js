/*Crea un archivo JS que contenga las siguientes líneas

- Una función sin parámetros que devuelva siempre "true"

- Una función asíncrona que utilice un setTimeout y pase por consola un "Hola soy una promesa" 5 segundos después de haberse ejecutado

- Una función generadora de índices pares automáticos */

const siempreTrue = () => true;

console.log(siempreTrue());

const funcionAsincrona = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Hola soy una promesa");
        }, 5000);
    });
}

funcionAsincrona().then((result) => {
    console.log(result);
});

function* generadorIndicesPares() {
    let number = 0;
    while (true) {
        yield number;
        number += 2;
    }
}

const indicesPares = generadorIndicesPares();

console.log(indicesPares.next().value);
console.log(indicesPares.next().value);
console.log(indicesPares.next().value);
console.log(indicesPares.next().value);
console.log(indicesPares.next().value);
