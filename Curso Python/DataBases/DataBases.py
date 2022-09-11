# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.


import sqlite3

# Conectamos con la base de datos
conexion = sqlite3.connect("Alumnos.db")

# Creamos el cursor
cursor = conexion.cursor()

# Creamos la tabla
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Alumnos (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT)")

# Insertamos datos
cursor.execute("INSERT INTO Alumnos VALUES (1, 'Juan', 'Perez')")
cursor.execute("INSERT INTO Alumnos VALUES (2, 'Maria', 'Gomez')")
cursor.execute("INSERT INTO Alumnos VALUES (3, 'Pedro', 'Garcia')")
cursor.execute("INSERT INTO Alumnos VALUES (4, 'Luis', 'Gonzalez')")
cursor.execute("INSERT INTO Alumnos VALUES (5, 'Ana', 'Rodriguez')")
cursor.execute("INSERT INTO Alumnos VALUES (6, 'Jose', 'Fernandez')")
cursor.execute("INSERT INTO Alumnos VALUES (7, 'Laura', 'Lopez')")
cursor.execute("INSERT INTO Alumnos VALUES (8, 'Marta', 'Martinez')")
cursor.execute("INSERT INTO Alumnos VALUES (9, 'Sara', 'Sanchez')")
cursor.execute("INSERT INTO Alumnos VALUES (10, 'Pablo', 'Diaz')")
cursor.execute("INSERT INTO Alumnos VALUES (11, 'Sergio', 'Moreno')")
cursor.execute("INSERT INTO Alumnos VALUES (12, 'Raul', 'Alvarez')")
cursor.execute("INSERT INTO Alumnos VALUES (13, 'Miguel', 'Romero')")
cursor.execute("INSERT INTO Alumnos VALUES (14, 'Sandra', 'Alonso')")
cursor.execute("INSERT INTO Alumnos VALUES (15, 'Nuria', 'Gutierrez')")
cursor.execute("INSERT INTO Alumnos VALUES (16, 'Carmen', 'Navarro')")
cursor.execute("INSERT INTO Alumnos VALUES (17, 'Rosa', 'Muñoz')")
cursor.execute("INSERT INTO Alumnos VALUES (18, 'Antonio', 'Iglesias')")
cursor.execute("INSERT INTO Alumnos VALUES (19, 'Manuel', 'Medina')")
cursor.execute("INSERT INTO Alumnos VALUES (20, 'Javier', 'Cortes')")
cursor.execute("INSERT INTO Alumnos VALUES (21, 'Pilar', 'Castro')")
cursor.execute("INSERT INTO Alumnos VALUES (22, 'Julia', 'Ortega')")
cursor.execute("INSERT INTO Alumnos VALUES (23, 'Sonia', 'Rubio')")
cursor.execute("INSERT INTO Alumnos VALUES (24, 'Miguel', 'Suarez')")
cursor.execute("INSERT INTO Alumnos VALUES (25, 'Sofia', 'Molina')")
cursor.execute("INSERT INTO Alumnos VALUES (26, 'Alicia', 'Morales')")
cursor.execute("INSERT INTO Alumnos VALUES (27, 'Daniel', 'Ortiz')")
cursor.execute("INSERT INTO Alumnos VALUES (28, 'Jorge', 'Delgado')")
cursor.execute("INSERT INTO Alumnos VALUES (29, 'Isabel', 'Castillo')")
cursor.execute("INSERT INTO Alumnos VALUES (30, 'Carlos', 'Vazquez')")
cursor.execute("INSERT INTO Alumnos VALUES (31, 'Noelia', 'Marin')")
cursor.execute("INSERT INTO Alumnos VALUES (32, 'Lucia', 'Serrano')")
cursor.execute("INSERT INTO Alumnos VALUES (33, 'Alba', 'Vidal')")
cursor.execute("INSERT INTO Alumnos VALUES (34, 'David', 'Cabrera')")
cursor.execute("INSERT INTO Alumnos VALUES (35, 'Irene', 'Campos')")
cursor.execute("INSERT INTO Alumnos VALUES (36, 'Eva', 'Vega')")
cursor.execute("INSERT INTO Alumnos VALUES (37, 'Marcos', 'Herrera')")
cursor.execute("INSERT INTO Alumnos VALUES (38, 'Paula', 'Nunez')")
cursor.execute("INSERT INTO Alumnos VALUES (39, 'Rocio', 'Jimenez')")
cursor.execute("INSERT INTO Alumnos VALUES (40, 'Fernando', 'Pascual')")
cursor.execute("INSERT INTO Alumnos VALUES (41, 'Marta', 'Benitez')")
cursor.execute("INSERT INTO Alumnos VALUES (42, 'Sergio', 'Vicente')")
cursor.execute("INSERT INTO Alumnos VALUES (43, 'Raul', 'Ramirez')")
cursor.execute("INSERT INTO Alumnos VALUES (44, 'Miguel', 'Flores')")
cursor.execute("INSERT INTO Alumnos VALUES (45, 'Sandra', 'Sanz')")
cursor.execute("INSERT INTO Alumnos VALUES (46, 'Nuria', 'Garrido')")
cursor.execute("INSERT INTO Alumnos VALUES (47, 'Carmen', 'Prieto')")
cursor.execute("INSERT INTO Alumnos VALUES (48, 'Rosa', 'Cano')")
cursor.execute("INSERT INTO Alumnos VALUES (49, 'Antonio', 'Reyes')")
cursor.execute("INSERT INTO Alumnos VALUES (50, 'Manuel', 'Carrasco')")
cursor.execute("INSERT INTO Alumnos VALUES (51, 'Javier', 'León')")
cursor.execute("INSERT INTO Alumnos VALUES (52, 'Pilar', 'Herrero')")
cursor.execute("INSERT INTO Alumnos VALUES (53, 'Julia', 'Dominguez')")
cursor.execute("INSERT INTO Alumnos VALUES (54, 'Sonia', 'Lorenzo')")
cursor.execute("INSERT INTO Alumnos VALUES (55, 'Miguel', 'Blanco')")
cursor.execute("INSERT INTO Alumnos VALUES (56, 'Sofia', 'Ramos')")
cursor.execute("INSERT INTO Alumnos VALUES (57, 'Alicia', 'Gil')")
cursor.execute("INSERT INTO Alumnos VALUES (58, 'Daniel', 'Santos')")
cursor.execute("INSERT INTO Alumnos VALUES (59, 'Jorge', 'Lozano')")
cursor.execute("INSERT INTO Alumnos VALUES (60, 'Isabel', 'Guerrero')")
cursor.execute("INSERT INTO Alumnos VALUES (61, 'Carlos', 'Fernandez')")
cursor.execute("INSERT INTO Alumnos VALUES (62, 'Noelia', 'Mendez')")
cursor.execute("INSERT INTO Alumnos VALUES (63, 'Lucia', 'Calvo')")
cursor.execute("INSERT INTO Alumnos VALUES (64, 'Alba', 'Gallego')")
cursor.execute("INSERT INTO Alumnos VALUES (65, 'David', 'Velez')")
cursor.execute("INSERT INTO Alumnos VALUES (66, 'Irene', 'Marquez')")
cursor.execute("INSERT INTO Alumnos VALUES (67, 'Eva', 'Santiago')")
cursor.execute("INSERT INTO Alumnos VALUES (68, 'Marcos', 'Cortes')")
cursor.execute("INSERT INTO Alumnos VALUES (69, 'Paula', 'Navarro')")
cursor.execute("INSERT INTO Alumnos VALUES (70, 'Rocio', 'Herrero')")
cursor.execute("INSERT INTO Alumnos VALUES (71, 'Fernando', 'Garcia')")
cursor.execute("INSERT INTO Alumnos VALUES (72, 'Marta', 'Gomez')")
cursor.execute("INSERT INTO Alumnos VALUES (73, 'Sergio', 'Perez')")
cursor.execute("INSERT INTO Alumnos VALUES (74, 'Raul', 'Gonzalez')")
cursor.execute("INSERT INTO Alumnos VALUES (75, 'Miguel', 'Rodriguez')")
cursor.execute("INSERT INTO Alumnos VALUES (76, 'Sandra', 'Martinez')")
cursor.execute("INSERT INTO Alumnos VALUES (77, 'Nuria', 'Sanchez')")
cursor.execute("INSERT INTO Alumnos VALUES (78, 'Carmen', 'Romero')")
cursor.execute("INSERT INTO Alumnos VALUES (79, 'Rosa', 'Alvarez')")
cursor.execute("INSERT INTO Alumnos VALUES (80, 'Antonio', 'Lopez')")
cursor.execute("INSERT INTO Alumnos VALUES (81, 'Manuel', 'Hernandez')")
cursor.execute("INSERT INTO Alumnos VALUES (82, 'Javier', 'Diaz')")
cursor.execute("INSERT INTO Alumnos VALUES (83, 'Pilar', 'Moreno')")
cursor.execute("INSERT INTO Alumnos VALUES (84, 'Julia', 'Muñoz')")
cursor.execute("INSERT INTO Alumnos VALUES (85, 'Sonia', 'Alonso')")
cursor.execute("INSERT INTO Alumnos VALUES (86, 'Miguel', 'Gutierrez')")
cursor.execute("INSERT INTO Alumnos VALUES (87, 'Sofia', 'Nieto')")
cursor.execute("INSERT INTO Alumnos VALUES (88, 'Alicia', 'Jimenez')")
cursor.execute("INSERT INTO Alumnos VALUES (89, 'Daniel', 'Ruiz')")
cursor.execute("INSERT INTO Alumnos VALUES (90, 'Jorge', 'Vargas')")
cursor.execute("INSERT INTO Alumnos VALUES (91, 'Isabel', 'Medina')")
cursor.execute("INSERT INTO Alumnos VALUES (92, 'Carlos', 'Cruz')")
cursor.execute("INSERT INTO Alumnos VALUES (93, 'Noelia', 'Ortega')")
cursor.execute("INSERT INTO Alumnos VALUES (94, 'Lucia', 'Reyes')")
cursor.execute("INSERT INTO Alumnos VALUES (95, 'Alba', 'Garrido')")
cursor.execute("INSERT INTO Alumnos VALUES (96, 'David', 'Cano')")
cursor.execute("INSERT INTO Alumnos VALUES (97, 'Irene', 'Pascual')")
cursor.execute("INSERT INTO Alumnos VALUES (98, 'Eva', 'Benitez')")
cursor.execute("INSERT INTO Alumnos VALUES (99, 'Marcos', 'Vicente')")
cursor.execute("INSERT INTO Alumnos VALUES (100, 'Paula', 'Ramirez')")
cursor.execute("INSERT INTO Alumnos VALUES (101, 'Rocio', 'Flores')")
cursor.execute("INSERT INTO Alumnos VALUES (102, 'Fernando', 'Sanz')")
cursor.execute("INSERT INTO Alumnos VALUES (103, 'Marta', 'Prieto')")
cursor.execute("INSERT INTO Alumnos VALUES (104, 'Sergio', 'Carrasco')")
cursor.execute("INSERT INTO Alumnos VALUES (105, 'Raul', 'León')")
cursor.execute("INSERT INTO Alumnos VALUES (106, 'Miguel', 'Herrero')")
cursor.execute("INSERT INTO Alumnos VALUES (107, 'Sandra', 'Dominguez')")
cursor.execute("INSERT INTO Alumnos VALUES (108, 'Nuria', 'Lorenzo')")
cursor.execute("INSERT INTO Alumnos VALUES (109, 'Carmen', 'Blanco')")
cursor.execute("INSERT INTO Alumnos VALUES (110, 'Rosa', 'Ramos')")
cursor.execute("INSERT INTO Alumnos VALUES (111, 'Antonio', 'Gil')")
cursor.execute("INSERT INTO Alumnos VALUES (112, 'Manuel', 'Santos')")
cursor.execute("INSERT INTO Alumnos VALUES (113, 'Javier', 'Lozano')")
cursor.execute("INSERT INTO Alumnos VALUES (114, 'Pilar', 'Guerrero')")
cursor.execute("INSERT INTO Alumnos VALUES (115, 'Julia', 'Fernandez')")
cursor.execute("INSERT INTO Alumnos VALUES (116, 'Sonia', 'Mendez')")
cursor.execute("INSERT INTO Alumnos VALUES (117, 'Miguel', 'Calvo')")
cursor.execute("INSERT INTO Alumnos VALUES (118, 'Sofia', 'Gallego')")
cursor.execute("INSERT INTO Alumnos VALUES (119, 'Alicia', 'Velez')")
cursor.execute("INSERT INTO Alumnos VALUES (120, 'Daniel', 'Marquez')")
cursor.execute("INSERT INTO Alumnos VALUES (121, 'Jorge', 'Santiago')")
cursor.execute("INSERT INTO Alumnos VALUES (122, 'Isabel', 'Cortes')")
cursor.execute("INSERT INTO Alumnos VALUES (123, 'Carlos', 'Navarro')")
cursor.execute("INSERT INTO Alumnos VALUES (124, 'Noelia', 'Herrero')")
cursor.execute("INSERT INTO Alumnos VALUES (125, 'Lucia', 'Garcia')")
cursor.execute("INSERT INTO Alumnos VALUES (126, 'Alba', 'Gomez')")
cursor.execute("INSERT INTO Alumnos VALUES (127, 'David', 'Perez')")
cursor.execute("INSERT INTO Alumnos VALUES (128, 'Irene', 'Gonzalez')")
cursor.execute("INSERT INTO Alumnos VALUES (129, 'Eva', 'Rodriguez')")
cursor.execute("INSERT INTO Alumnos VALUES (130, 'Marcos', 'Martinez')")
cursor.execute("INSERT INTO Alumnos VALUES (131, 'Paula', 'Sanchez')")
cursor.execute("INSERT INTO Alumnos VALUES (132, 'Rocio', 'Romero')")
cursor.execute("INSERT INTO Alumnos VALUES (133, 'Fernando', 'Alvarez')")
cursor.execute("INSERT INTO Alumnos VALUES (134, 'Marta', 'Lopez')")
cursor.execute("INSERT INTO Alumnos VALUES (135, 'Sergio', 'Hernandez')")
cursor.execute("INSERT INTO Alumnos VALUES (136, 'Raul', 'Diaz')")
cursor.execute("INSERT INTO Alumnos VALUES (137, 'Miguel', 'Moreno')")
cursor.execute("INSERT INTO Alumnos VALUES (138, 'Sandra', 'Muñoz')")
cursor.execute("INSERT INTO Alumnos VALUES (139, 'Nuria', 'Alonso')")
cursor.execute("INSERT INTO Alumnos VALUES (140, 'Carmen', 'Gutierrez')")
cursor.execute("INSERT INTO Alumnos VALUES (141, 'Rosa', 'Nieto')")
cursor.execute("INSERT INTO Alumnos VALUES (142, 'Antonio', 'Jimenez')")
cursor.execute("INSERT INTO Alumnos VALUES (143, 'Manuel', 'Ruiz')")
cursor.execute("INSERT INTO Alumnos VALUES (144, 'Javier', 'Vargas')")
cursor.execute("INSERT INTO Alumnos VALUES (145, 'Pilar', 'Medina')")
cursor.execute("INSERT INTO Alumnos VALUES (146, 'Julia', 'Cruz')")
cursor.execute("INSERT INTO Alumnos VALUES (147, 'Sonia', 'Ortega')")
cursor.execute("INSERT INTO Alumnos VALUES (148, 'Miguel', 'Reyes')")
cursor.execute("INSERT INTO Alumnos VALUES (149, 'Sofia', 'Garrido')")
cursor.execute("INSERT INTO Alumnos VALUES (150, 'Alicia', 'Cano')")


# Guardamos los cambios
conexion.commit()

# Cerramos la conexión
conexion.close()

# Conectamos con la base de datos
conexion = sqlite3.connect("Alumnos.db")

# Creamos el cursor
cursor = conexion.cursor()

# Realizamos la consulta
cursor.execute("SELECT * FROM Alumnos WHERE nombre = 'Sandra'")
alumnos = cursor.fetchall()

# Mostramos los datos
for alumno in alumnos:
    print(alumno)

# Guardamos los cambios
conexion.commit()

# Cerramos la conexión
conexion.close()