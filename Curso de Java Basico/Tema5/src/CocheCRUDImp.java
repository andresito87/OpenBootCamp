public class CocheCRUDImp implements VehiculoCRUD {
    private Coche[] coches;
    private int numCoches;

    public CocheCRUDImp() {
        coches = new Coche[10];
        numCoches = 0;
    }

    @Override
    public void create(Vehiculo vehiculo) {
        coches[numCoches] = (Coche) vehiculo;
        numCoches++;
    }

    public String read(String matricula) {
        for (int i = 0; i < numCoches; i++) {
            if (coches[i].getMatricula().equals(matricula)) {
                return coches[i].toString();
            }
        }
        return null;
    }


    public void update(String matricula) {
        for (int i = 0; i < numCoches; i++) {
            if (coches[i].getMatricula().equals(matricula)) {
                coches[i].setPrecio(coches[i].getPrecio() * 1.1);
            }
        }
    }

    public void delete(String matricula) {
        for (int i = 0; i < numCoches; i++) {
            if (coches[i].getMatricula().equals(matricula)) {
                coches[i] = coches[numCoches - 1];
                numCoches--;
            }
        }
    }

    public void update(Coche coche) {
        for (int i = 0; i < numCoches; i++) {
            if (coches[i].getMatricula().equals(coche.getMatricula())) {
                coches[i] = coche;
            }
        }
    }

    public void delete(Coche coche) {
        for (int i = 0; i < numCoches; i++) {
            if (coches[i].getMatricula().equals(coche.getMatricula())) {
                coches[i] = coches[numCoches - 1];
                numCoches--;
            }
        }
    }
}
