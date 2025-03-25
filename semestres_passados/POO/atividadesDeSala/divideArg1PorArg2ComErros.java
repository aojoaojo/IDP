//inclua uma biblioteca para receber o input do usuário
import java.util.Scanner;

public class dividir {

    public static void main(String[] args) {
        try {
            int dividendo = Integer.parseInt(args[0]);
            int divisor = Integer.parseInt(args[1]);
            int resultado = dividir(dividendo, divisor);
            System.out.println("O resultado é: " + resultado);
        } catch (ArrayIndexOutOfBoundsException aiobe) {
            System.out.println("Por favor, forneça os dois argumentos para o cálculo ocorrer de forma correta\n");    
            System.err.println(aiobe);
        } catch (NumberFormatException nfe) {
            System.out.println("Insira um número inteiro");
        } catch (Exception e) {
            System.out.println("Ocorreu um erro inesperado");
        }
    }

    private static int dividir(int dividendo, int divisor) {
        return dividendo / divisor;
    }
}