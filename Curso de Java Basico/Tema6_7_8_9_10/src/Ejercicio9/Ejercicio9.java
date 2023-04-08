package Ejercicio9;

import java.io.*;

//Utilizando InputStream y PrintStream, crea una función que reciba dos parámetros:
// "fileIn" y "fileOut". La tarea de la función será realizar la copia del fichero
// dado en el parámetro "fileIn" al fichero dado en "fileOut".
public class Ejercicio9 {

    public static void main(String[] args) {

        //obtener la ruta de donde se encuentran los archivos mediante user.dir
        String ruta = System.getProperty("user.dir")+"\\Tema6_7_8_9_10\\src\\Ejercicio9";

        System.out.println(ruta);
        File archivoEntrada = new File(ruta+"\\entrada.txt");
        File archivoSalida = new File(ruta+"\\salida.txt");

        copiarArchivos(archivoEntrada, archivoSalida);
    }

    public static void copiarArchivos(File archivoEntrada, File archivoSalida) {

        try (BufferedReader br = new BufferedReader(new FileReader(archivoEntrada));
             BufferedWriter bw = new BufferedWriter(new FileWriter(archivoSalida));) {

            String linea;
            while ((linea = br.readLine()) != null) {
                bw.write(linea);
                bw.newLine();
            }
        } catch (FileNotFoundException ex) {
            System.out.println("No se ha encontrado el archivo");
        } catch (IOException ex) {
            System.out.println("Error de entrada/salida");
        }

    }
}