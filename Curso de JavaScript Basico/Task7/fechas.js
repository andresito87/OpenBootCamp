/*Crea un archivo llamado fechas.js que contenga las siguientes líneas

- La fecha de hoy

- La fecha de tu nacimiento

- Un variable que indique si hoy es más tarde (>) que la fecha de tu nacimiento

- Una variable que contenga el día de tu nacimiento

- Una variable que contenga el mes de tu nacimiento (recuerda que Enero es mes 0)

- Una variable que contenga el año de tu nacimiento (con 4 dígitos) */

const hoy = new Date();
const nacimiento = new Date(1987, 07, 05);
const esMasTarde = hoy > nacimiento;
const diaNacimiento = nacimiento.getDate();
const mesNacimiento = nacimiento.getMonth();
const anioNacimiento = nacimiento.getFullYear();

console.log(`Hoy es ${hoy}, naci el ${nacimiento}, es mas tarde ${esMasTarde}, dia de nacimiento ${diaNacimiento}, mes de nacimiento ${mesNacimiento}, anio de nacimiento ${anioNacimiento}`);