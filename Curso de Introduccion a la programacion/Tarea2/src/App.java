public class App {
    public static void main(String[] args) throws Exception {

        int number = 1;
        if (number > 0) {
            System.out.println("Es positivo");
        } else if (number < 0) {
            System.out.println("Es negativo");
        } else {
            System.out.println("Es 0");
        }

        while (number < 3) {
            number++;
            System.out.println(number);
        }

        do {
            number++;
            System.out.println(number);
        } while (number < 4);

        for (int i = 0; i <= 3; i++) {
            System.out.println(i);
        }

        String season = "Otoño";
        switch (season) {
            case "Primavera":
                System.out.println("Es Primavera");
                break;
            case "Verano":
                System.out.println("Es Verano");
                break;
            case "Otoño":
                System.out.println("Es Otoño");
                break;
            case "Invierno":
                System.out.println("Es Invierno");
                break;
        }
    }
}
