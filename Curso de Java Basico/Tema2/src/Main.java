public class Main {
    public static void main(String[] args) {

        double price = 120;
        double priceWithIva = calculatePriceWithIva(price);
        System.out.println(priceWithIva);

    }
    public static double calculatePriceWithIva(double price) {
        double tax = 0.21;
        return price + price * tax;
    }
}