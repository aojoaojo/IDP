public class Triangulo{

    private final double base;
    private final double altura;

    Triangulo(double base, double altura){

        this.base = base;
        this.altura = altura;
    }
    
    public void imprimirBaseEAlturaTriangulo(){
        System.out.println();
        System.out.println("Base do Triangulo: " + base);
        System.out.println("Altura do Triangulo: " + altura);
    }
    
    public void imprimirAreaTriangulo(){
        
        double area = (base * altura)/2;
        System.out.println();
        System.out.println("Area do triangulo: " + area);
    
    }

    public double getBase() {
        return base;
    }

    public double getAltura() {
        return altura;
    }
}