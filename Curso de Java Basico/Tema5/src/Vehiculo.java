public class Vehiculo {
    protected String matricula;
    protected String marca;
    protected String modelo;
    protected String color;
    protected double precio;

    public Vehiculo() {}

    public Vehiculo(String matricula, String marca, String modelo, String color, double precio) {
        this.matricula = matricula;
        this.marca = marca;
        this.modelo = modelo;
        this.color = color;
        this.precio = precio;
    }

    @Override
    public String toString() {
        return "Vehiculo{" +
                "matricula='" + matricula + '\'' +
                ", marca='" + marca + '\'' +
                ", modelo='" + modelo + '\'' +
                ", color='" + color + '\'' +
                ", precio=" + precio +
                '}';
    }
}
