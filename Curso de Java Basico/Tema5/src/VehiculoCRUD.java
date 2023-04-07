public interface VehiculoCRUD {
    public void create(Vehiculo vehiculo);
    public String read(String matricula);
    public void update(String matricula);
    public void delete(String matricula);

}
