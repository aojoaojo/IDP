public class Quadrado{

    private final double lado;

    Quadrado(double lado){

        this.lado = lado;
    }
    
    public void imprimirTamanhoLado(){
        System.out.println();
        System.out.println("Lado do quadrado: " + lado);
    }
    
    public void imprimirArea(){
        double area = lado * lado;
        System.out.println();
        System.out.println("Area do quadrado: " + area);    
    }

    public void imprimirPerimetro(){
        double perimetro = lado * 4;
        System.out.println();
        System.out.println("Perimetro do quadrado: " + perimetro);
    }

    public double getLado() {
        return lado;
    }
}