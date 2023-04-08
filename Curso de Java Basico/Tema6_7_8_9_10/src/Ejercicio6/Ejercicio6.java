package Ejercicio6;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.LinkedList;

//Crea un ArrayList de tipo String, con 4 elementos. Cópialo en una LinkedList.
// Recorre ambos mostrando únicamente el valor de cada elemento.
public class Ejercicio6 {
    public static void main(String[] args) {
        ArrayList<String> lenguajes=new ArrayList<>();
        lenguajes.add("Java");
        lenguajes.add("Javascript");
        lenguajes.add("C++");
        lenguajes.add("Php");

        LinkedList<String> lenguajes2 =new LinkedList<>();
        for (String lenguaje:lenguajes) {
            lenguajes2.add(lenguaje);
        }
        //lenguajes2.addAll(lenguajes);

        System.out.println(lenguajes);
        System.out.println(lenguajes2);
    }
}
