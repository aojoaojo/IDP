import java.lang.Math;

public class Circulo{

    private final double raio;

    Circulo(double raio){
        this.raio = raio;
    }
    
    public void imprimirTamanhoLadoCirculo(){
        System.out.println();
        System.out.println("Raio do Círculo: " + raio);
    }
    
    public void imprimirAreaCirculo(){
        double area = (Math.PI * (Math.pow(raio, 2)))/2;
        System.out.println();
        System.out.println("Area do Círculo: " + area);
    }

    public void imprimirPerimetroCirculo(){
        double perimetro = 2 * Math.PI * raio;
        System.out.println();
        System.out.println("Perimetro do Círculo: " + perimetro);
    }

    public double getRaio() {
        return raio;
    }
}