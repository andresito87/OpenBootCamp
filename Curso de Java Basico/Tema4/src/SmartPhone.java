public class SmartPhone extends SmartDevice{
    protected String color;
    protected double diskSize;

    public SmartPhone() {}
    public SmartPhone(String name, String brand, String serialNumber,double price, String model, String color, double diskSize) {
        super(name, brand, serialNumber, model, price);
        this.model = model;
        this.color = color;
        this.diskSize = diskSize;
    }

    @Override
    public String toString() {
        return "SmartPhone{" +
                "color='" + color + '\'' +
                ", diskSize=" + diskSize +
                ", name='" + name + '\'' +
                ", model='" + model + '\'' +
                ", brand='" + brand + '\'' +
                ", serialNumber='" + serialNumber + '\'' +
                ", price=" + price +
                '}';
    }
}
