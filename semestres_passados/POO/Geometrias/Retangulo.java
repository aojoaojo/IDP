public class Retangulo{

    private final double ladoMaior;
    private final double ladoMenor;

    Retangulo(double ladoMaior, double ladoMenor){

        this.ladoMaior = ladoMaior;
        this.ladoMenor = ladoMenor;
    }
    
    public void imprimirTamanhoLado(){
        System.out.println();
        System.out.println("Lado maior do retangulo: " + ladoMaior);
        System.out.println("Lado menor do retangulo: " + ladoMenor);
    }
    
    public void imprimirArea(){
        
        double area = ladoMaior * ladoMenor;
        System.out.println();
        System.out.println("Area do retangulo: " + area);
    
    }

    public void imprimirPerimetro(){
        double perimetro = (ladoMaior * 2) + (ladoMenor * 2);
        System.out.println();
        System.out.println("Perimetro do retangulo: " + perimetro);
    }

    public double getLadoMaior() {
        return ladoMaior;
    }

    public double getLadoMenor() {
        return ladoMenor;
    }
}