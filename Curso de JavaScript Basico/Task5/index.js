/* Crea un archivo JS que contenga las siguientes líneas

- Una variable que contenga tu altura en centímetros (entero)

- Una variable que contenga tu altura en metros (número de coma flotante)

- Una variable que contenga tu peso en kilogramos (número de coma flotante)

- Una variable que contenga tu altura en metros redondeada hacia arriba

- Una variable que contenga tu peso en kilogramos redondeado hacia abajo

- Una variable que contenga si "el máximo valor que se puede obtener en Javascript + 1" es igual al máximo valor que se puede obtener en Javascript*/

let alturaCentimetros = 170;
let alturaMetros = 1.70;
let pesoKilogramos = 73.5;
let alturaMetrosRedondeada = Math.ceil(alturaMetros);
let pesoKilogramosRedondeado = Math.floor(pesoKilogramos);
let maximoValor = Number.MAX_VALUE;
let maximoValorMasUno = maximoValor + 1;
let maximoValorIgualMaximoValorMasUno = maximoValor === maximoValorMasUno;

console.log(alturaCentimetros, alturaMetros, pesoKilogramos, alturaMetrosRedondeada, pesoKilogramosRedondeado, maximoValor, maximoValorMasUno, maximoValorIgualMaximoValorMasUno);