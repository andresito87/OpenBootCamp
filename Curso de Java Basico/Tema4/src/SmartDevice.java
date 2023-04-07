public class SmartDevice {
    protected String name;

    protected String model;
    protected String brand;
    protected String serialNumber;

    protected double price;

    public SmartDevice() {}

    public SmartDevice(String name, String model, String brand, String serialNumber, double price) {
        this.name = name;
        this.model = model;
        this.brand = brand;
        this.serialNumber = serialNumber;
        this.price = price;
    }

    @Override
    public String toString() {
        return "SmartDevice{" +
                "name='" + name + '\'' +
                ", model='" + model + '\'' +
                ", brand='" + brand + '\'' +
                ", serialNumber='" + serialNumber + '\'' +
                ", price=" + price +
                '}';
    }
}
