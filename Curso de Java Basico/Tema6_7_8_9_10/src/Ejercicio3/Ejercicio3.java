package Ejercicio3;

//Crea un array bidimensional de enteros y recórrelo,
// mostrando la posición y el valor de cada elemento en ambas dimensiones.
public class Ejercicio3 {
    public static void main(String[] args) {
        int [][] numeros = {{2, 4, 5, 7, 9, 67}, {4, 8, 1, 2, 4, 5}, {4, 8, 1, 4, 5, 7}};
        for (int i=0;i<numeros.length;i++) {
            for(int j=0;j<numeros[i].length;j++){
                System.out.println("Numero "+numeros[i][j]+" en la posicion i:"+i+" y en la posicion j:"+j);
            }
        }
    }
}
