public class App {
    public static void main(String[] args) throws Exception {
        sum(10, 20, 30);

        Car myCar = new Car();
        myCar.addDoors(1);
        myCar.showNumberDoors();
    }

    public static void sum(int a, int b, int c) {
        System.out.println(a + b + c);
    }

    public static class Car {
        public int numberDoors = 4;

        public void addDoors(int numberDoorsAdded) {
            this.numberDoors += numberDoorsAdded;
        }

        public void showNumberDoors() {
            System.out.println(numberDoors);
        }
    }
}
