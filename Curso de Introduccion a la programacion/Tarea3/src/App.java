public class App {
    public static void main(String[] args) throws Exception {
        Person persona = new Person();
        persona.setAge(35);
        persona.setName("Andres");
        persona.setNumberPhone(952347621);
        System.out.println(persona.getAge());
        System.out.println(persona.getName());
        System.out.println(persona.getNumberPhone());
    }

    public static class Person {
        private int age;
        private String name;
        private int numberPhone;

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
}
