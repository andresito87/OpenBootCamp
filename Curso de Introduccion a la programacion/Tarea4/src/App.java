public class App {
    public static void main(String[] args) throws Exception {
        Customer customer = new Customer();
        customer.setAge(35);
        customer.setCredit(35000);
        customer.setName("Andres");
        customer.setNumberPhone(952345682);
        System.out.println(customer.getAge());
        System.out.println(customer.getCredit());
        System.out.println(customer.getName());
        System.out.println(customer.getNumberPhone());
        Worker worker = new Worker();
        worker.setAge(30);
        worker.setName("Jose");
        worker.setNumberPhone(952345665);
        worker.setSalary(12000);
        System.out.println(worker.getAge());
        System.out.println(worker.getName());
        System.out.println(worker.getNumberPhone());
        System.out.println(worker.getSalary());
    }

    public static class Person {
        int age;
        String name;
        int numberPhone;

        public int getAge() {
            return age;
        }

        public void setAge(int age) {
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public int getNumberPhone() {
            return numberPhone;
        }

        public void setNumberPhone(int numberPhone) {
            this.numberPhone = numberPhone;
        }
    }

    public static class Customer extends Person {
        public double credit;

        public double getCredit() {
            return credit;
        }

        public void setCredit(double credit) {
            this.credit = credit;
        }
    }

    public static class Worker extends Person {
        private double salary;

        public double getSalary() {
            return salary;
        }

        public void setSalary(double salary) {
            this.salary = salary;
        }
    }
}
