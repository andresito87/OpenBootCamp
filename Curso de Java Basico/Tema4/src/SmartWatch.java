public class SmartWatch extends SmartDevice {
    protected double screenSize;
    protected double batteryLife;

    public SmartWatch() {}
    public SmartWatch(String name, String model, String brand, String serialNumber, double price,
                      double screenSize, double batteryLife) {
        super(name, model, brand, serialNumber, price);
        this.screenSize = screenSize;
        this.batteryLife = batteryLife;
        this.price = price;
    }

    @Override
    public String toString() {
        return "SmartWatch{" +
                "screenSize=" + screenSize +
                ", batteryLife=" + batteryLife +
                ", name='" + name + '\'' +
                ", model='" + model + '\'' +
                ", brand='" + brand + '\'' +
                ", serialNumber='" + serialNumber + '\'' +
                ", price=" + price +
                '}';
    }
}

