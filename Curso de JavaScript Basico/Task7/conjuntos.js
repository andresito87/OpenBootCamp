/*Crea un archivo llamado conjuntos.js que contenga las siguientes líneas

- Un nuevo Set con los nombres de tu familia

- Modifica el Set original añadiendo tu nombre (duplicado) (debería darte lo mismo)

- Modifica el Set original añadiendo el nombre "Javascript" (ya que empieza a formar parte de tu vida ;)*/



const family = new Set(["Andres", "Maria", "Jose", "Luis", "Ana", "Luisa", "Luis"]);
family.add("Andres");
family.add("Javascript");


console.log(family);