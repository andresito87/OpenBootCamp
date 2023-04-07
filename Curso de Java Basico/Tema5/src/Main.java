public class Main {
    public static void main(String[] args) {

        VehiculoCRUD cochesCRUD = new CocheCRUDImp();
        cochesCRUD.create(new Coche("2345TYU", "Ford", "Mondeo", "blanco",100, 6, 5, 6, 15_000));
        cochesCRUD.create(new Coche("1234MNP", "Fiat", "Punto", "negro",60, 6, 5, 3, 10_000));
        cochesCRUD.create(new Coche("5678RTB", "Renault", "Megane", "rojo",80, 6, 5, 6, 25_000));

        VehiculoCRUD motosCRUD = new MotoCRUDImp();
        motosCRUD.create(new Moto("6789PYW", "Yamaha", "RTX", "blanco", 12_000, 3));


        System.out.println(cochesCRUD.read("2345TYU"));
        System.out.println(motosCRUD.read("6789PYW"));


    }
}