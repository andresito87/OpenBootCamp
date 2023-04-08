package Ejercicio8;

//Crea una función DividePorCero. Esta, debe generar una excepción ("throws") a su llamante
// del tipo ArithmeticException que será capturada por su llamante (desde "main", por ejemplo).
// Si se dispara la excepción, mostraremos el mensaje "Esto no puede hacerse". Finalmente,
// mostraremos en cualquier caso: "Demo de código".
public class Ejercicio8 {
    public static void main(String[] args) {
        try{
            DividePorCero();
        }catch(ArithmeticException ex){
            System.out.println("Esto no puede hacerse");
        }finally {
            System.out.println("Demo de código");
        }
    }

    public static void DividePorCero() throws ArithmeticException{
        System.out.println(5/0);
    }
}
