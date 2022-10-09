//- factorial-while.js -> Este archivo debe calcular el factorial de 10 utilizando un bucle while

let factorial = 1;
let i = 1;
while (i <= 10) {
    factorial *= i;
    i++;
}

console.log(factorial);