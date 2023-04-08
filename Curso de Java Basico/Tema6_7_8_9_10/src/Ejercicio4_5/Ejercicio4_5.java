package Ejercicio4_5;

import java.util.Vector;

//1.-Crea un "Vector" del tipo de dato que prefieras, y añádele 5 elementos.
// Elimina el 2o y 3er elemento y muestra el resultado final.
//2.-Indica cuál es el problema de utilizar un Vector con la capacidad por
// defecto si tuviésemos 1000 elementos para ser añadidos al mismo.
//El problema de utilizar un vector con la capacidad por defecto si tuviésemos 1000 elementos
// para ser añadidos al mismo es que el vector tendría que redimensionarse varias veces durante
// la inserción de los elementos, lo que puede llevar a un alto costo computacional y de rendimiento.
//
//Cuando se crea un vector, por defecto tiene una capacidad inicial que depende del compilador
// utilizado y del sistema operativo. Si se intenta agregar más elementos de los que puede contener
// la capacidad inicial, el vector se redimensionará automáticamente para ajustarse a la nueva
// cantidad de elementos. Este proceso implica la creación de un nuevo bloque de memoria,
// la copia de los elementos existentes en el vector original a la nueva ubicación de memoria
// y la liberación de la memoria antigua.
//
//En el caso de agregar 1000 elementos a un vector con la capacidad por defecto, el vector
// tendría que redimensionarse varias veces durante la inserción, lo que generaría un costo
// computacional adicional y reduciría el rendimiento del programa. Para evitar esto, es
// recomendable especificar una capacidad inicial adecuada al tamaño previsto del vector,
// para que tenga suficiente espacio para alojar los elementos sin tener que realizar muchas redimensiones.
public class Ejercicio4_5 {
    public static void main(String[] args) {
        Vector<String> miVector=new Vector<>();

        miVector.add("Hola");
        miVector.add("esto es");
        miVector.add("un vector");
        miVector.add("en Java");

        System.out.println(miVector);
        miVector.remove(2);
        System.out.println(miVector);
        miVector.remove(1);
        System.out.println(miVector);
    }
}
