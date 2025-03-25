import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        
        double lado;
        double ladoMaior;
    
        
        while(true){
            Scanner input = new Scanner(System.in);
            
            System.out.println("\nEscolha a opção desejada:");
            System.out.println("1 - Quadrado");
            System.out.println("2 - Triangulo");
            System.out.println("3 - Círculo");
            System.out.println("4 - Retângulo");
            System.out.println("5 - Sair");
            
            int a = input.nextInt();
            
            System.out.println("Escolhido: " + a);
            
            switch(a){
                case 1:
                    System.out.println("\nDigite o tamanho do lado do quadrado: ");
                    lado = input.nextDouble();
                    System.out.println("\nDeseja calcular a área ou o perímetro: ");
                    System.out.println("1 - Área");
                    System.out.println("2 - Perímetro");
                    int b = input.nextInt();
                    if(b == 1){
                        Quadrado teste = new Quadrado(lado);
                        teste.imprimirArea();
                    }
                    else if(b == 2){
                        Quadrado teste = new Quadrado(lado);
                        teste.imprimirPerimetro();
                    }
                    else{
                        System.out.println("\nOpção inválida!");
                    }
                    break;
                case 2:
                    System.out.println("\nDigite o tamanho da base do triângulo: ");
                    lado = input.nextDouble();
                    System.out.println("\nDigite o tamanho da altura do triângulo: ");
                    ladoMaior = input.nextDouble();
                    System.out.println("\nDeseja calcular a área ou o perímetro: ");
                    System.out.println("1 - Área");
                    System.out.println("2 - Perímetro");
                    int c = input.nextInt();
                    if(c == 1){
                        Triangulo teste = new Triangulo(ladoMaior, lado);
                        teste.imprimirAreaTriangulo();
                    }
                    else if(c == 2){
                        Triangulo teste = new Triangulo(ladoMaior, lado);
                        teste.imprimirBaseEAlturaTriangulo();
                    }
                    else{
                        System.out.println("\nOpção inválida!");
                    }
                    break;
                case 3: 
                    System.out.println("\nDigite o tamanho do raio do círculo: ");
                    lado = input.nextDouble();
                    System.out.println("\nDeseja calcular a área ou o perímetro: ");
                    System.out.println("1 - Área");
                    System.out.println("2 - Perímetro");
                    int d = input.nextInt();
                    if(d == 1){
                        Circulo teste = new Circulo(lado);
                        teste.imprimirAreaCirculo();
                    }
                    else if(d == 2){
                        Circulo teste = new Circulo(lado);
                        teste.imprimirPerimetroCirculo();
                    }
                    else{
                        System.out.println("\nOpção inválida!");
                    }
                    break;
                case 4:
                    System.out.println("\nDigite o tamanho da base do retângulo: ");
                    lado = input.nextDouble();
                    System.out.println("\nDigite o tamanho da altura do retângulo: ");
                    ladoMaior = input.nextDouble();
                    System.out.println("\nDeseja calcular a área ou o perímetro: ");
                    System.out.println("1 - Área");
                    System.out.println("2 - Perímetro");
                    int e = input.nextInt();
                    if(e == 1){
                        Retangulo teste = new Retangulo(ladoMaior, lado);
                        teste.imprimirArea();
                    }
                    else if(e == 2){
                        Retangulo teste = new Retangulo(ladoMaior, lado);
                        teste.imprimirPerimetro();
                    }
                    else{
                        System.out.println("\nOpção inválida!");
                    }
                    break;
                case 5:
                    System.out.println("\nSaindo...");
                    System.exit(0);
                    break;
                default:
            }
    
        }

    }
}