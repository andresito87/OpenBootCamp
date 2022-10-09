/* Crea un nuevo proyecto de Node

- Instala la dependencia Winston

- En el archivo index.js crea una función que devuelva un error con un mensaje personalizado

- Registra el error en un archivo a través de un try...catch*/

const winston = require("winston");

const logger = winston.createLogger({
    transports: [
        new winston.transports.File({
            filename: "error.log",
            level: "error"
        })
    ]
});

const error = (message) => {
    throw new Error(message);
}

try {
    error("ERROR: Este es un error personalizado");
}
catch (e) {
    logger.error(e.message);
}
