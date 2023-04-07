public class Main {
    public static void main(String[] args) {
        String[] nombres = {"Andres", "Juan", "Pedro", "Maria"};
        StringBuilder resultado = new StringBuilder();
        for (String nombre : nombres) {
            resultado.append(nombre).append(" ");
        }
        System.out.println(resultado);
    }
}