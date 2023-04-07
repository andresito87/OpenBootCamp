public class MotoCRUDImp implements VehiculoCRUD {
    private Moto[] motos;
    private int numMotos;

    public MotoCRUDImp() {
        motos = new Moto[10];
        numMotos = 0;
    }

    @Override
    public void create(Vehiculo vehiculo) {
        motos[numMotos] = (Moto) vehiculo;
        numMotos++;
    }

    public String read(String matricula) {
        for (int i = 0; i < numMotos; i++) {
            if (motos[i].getMatricula().equals(matricula)) {
                return motos[i].toString();
            }
        }
        return null;
    }

    public void update(String matricula) {
        for (int i = 0; i < numMotos; i++) {
            if (motos[i].getMatricula().equals(matricula)) {
                motos[i].setPrecio(motos[i].getPrecio() * 1.1);
            }
        }
    }

    public void delete(String matricula) {
        for (int i = 0; i < numMotos; i++) {
            if (motos[i].getMatricula().equals(matricula)) {
                motos[i] = motos[numMotos - 1];
                numMotos--;
            }
        }
    }

}
