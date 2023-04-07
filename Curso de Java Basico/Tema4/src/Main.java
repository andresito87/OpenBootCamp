public class Main {
    public static void main(String[] args) {

        SmartDevice[] smartDevices = new SmartDevice[3];
        smartDevices[0] = new SmartPhone("iPhone 12", "Apple", "123456789", 999.99, "iPhone 12", "Black", 128);
        smartDevices[1] = new SmartWatch("Apple Watch", "Apple", "987654321", "234234", 70.99, 7.5, 18);
        smartDevices[2] = new SmartWatch("Samsung Galaxy Watch", "Samsung", "123456789", "45666789", 99.99, 5.5, 20);

        for (SmartDevice smartDevice : smartDevices) {
            System.out.println(smartDevice);
        }

    }
}