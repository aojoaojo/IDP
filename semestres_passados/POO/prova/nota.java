//QUESTÃO 6:
import java.util.Scanner;

public class nota {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite a média final do aluno: ");
        final double media = scanner.nextDouble();
        final double recuperacao = 30;
        final double aprovado = 70;
        final double notaMaxima = 100;

        if (media >= aprovado && media <= notaMaxima) {
            System.out.println("Aprovado");
        } else if (media >= recuperacao && media < aprovado) {
            System.out.println("Em recuperação");
        } else if(media > notaMaxima || media < 0){
            System.out.println("Nota inválida");
        }else {
            System.out.println("Reprovado");
        }
    }
}