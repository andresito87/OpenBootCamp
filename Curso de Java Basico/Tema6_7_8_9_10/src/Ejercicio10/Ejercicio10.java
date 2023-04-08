package Ejercicio10;

//Funcion que copia el contenido de un archivo en una arraylist y lo muestra por
//pantalla concateando los elementos de la arraylist

import java.io.*;
import java.util.ArrayList;

public class Ejercicio10 {

    public static void main(String[] args) {

        //obtener la ruta de donde se encuentran los archivos mediante user.dir
        String ruta = System.getProperty("user.dir")+"\\Tema6_7_8_9_10\\src\\Ejercicio10";

        File archivoEntrada = new File(ruta+"\\entrada.txt");
        StringBuilder resultado= new StringBuilder();

        try {
            ArrayList<String> lista = lectorArchivo(archivoEntrada);
            for (String linea : lista) {
                resultado.append(linea).append(" ");
            }
        } catch (FileNotFoundException ex) {
            System.out.println("No se ha encontrado el archivo");
        } catch (IOException ex) {
            System.out.println("Error de entrada/salida");
        }

        System.out.println(resultado);
    }

    public static ArrayList<String> lectorArchivo(File archivo) throws FileNotFoundException,
            IOException {
        BufferedReader br = new BufferedReader(new FileReader(archivo));
        ArrayList<String> lista = new ArrayList<>();
        String linea;
            while ((linea = br.readLine()) != null) {
                lista.add(linea);
            }

        return lista;
    }

}
