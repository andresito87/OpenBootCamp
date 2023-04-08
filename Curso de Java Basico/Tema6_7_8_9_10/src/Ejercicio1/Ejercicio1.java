package Ejercicio1;

public class Ejercicio1 {
    /*Dada la función:
    public static String reverse(String texto) { }
    Escribe el código que devuelva una cadena al revés. Por ejemplo, la cadena "hola mundo",
    debe retornar "odnum aloh".*/
    public static void main(String[] args) {
        System.out.println(reverse("hola mundo"));
    }
    public static String reverse(String texto) {
        String stringReversed="";
        for (int i=texto.length()-1;i>=0;i--){
            stringReversed+=texto.charAt(i);
        }

        return stringReversed;
    }
}
