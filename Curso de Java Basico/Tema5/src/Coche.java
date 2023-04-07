public class Coche extends Vehiculo{
    private int potencia;
    private int cilindrada;
    private int numPuertas;
    private int numPlazas;

    public Coche() {}

    public Coche(String matricula, String marca, String modelo, String color, int potencia, int cilindrada, int numPuertas, int numPlazas, double precio) {
        super(matricula, marca, modelo, color, precio);
        this.potencia = potencia;
        this.cilindrada = cilindrada;
        this.numPuertas = numPuertas;
        this.numPlazas = numPlazas;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getPotencia() {
        return potencia;
    }

    public void setPotencia(int potencia) {
        this.potencia = potencia;
    }

    public int getCilindrada() {
        return cilindrada;
    }

    public void setCilindrada(int cilindrada) {
        this.cilindrada = cilindrada;
    }

    public int getNumPuertas() {
        return numPuertas;
    }

    public void setNumPuertas(int numPuertas) {
        this.numPuertas = numPuertas;
    }

    public int getNumPlazas() {
        return numPlazas;
    }

    public void setNumPlazas(int numPlazas) {
        this.numPlazas = numPlazas;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    @Override
    public String toString() {
        return "Coche{" +
                "matricula='" + matricula + '\'' +
                ", marca='" + marca + '\'' +
                ", modelo='" + modelo + '\'' +
                ", color='" + color + '\'' +
                ", potencia=" + potencia +
                ", cilindrada=" + cilindrada +
                ", numPuertas=" + numPuertas +
                ", numPlazas=" + numPlazas +
                ", precio=" + precio +
                '}';
    }
}
