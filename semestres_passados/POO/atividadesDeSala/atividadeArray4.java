import java.util.Scanner;

public class atividade {
    public static void main(String[] args) {
        try{
            int[] vetor = new int[5];
            Scanner banana = new Scanner(System.in);
            System.out.println("Insira um número inteiro: ");
            vetor[1] = banana.nextInt();
            System.out.println("Insira outro número inteiro: ");
            vetor[2] = banana.nextInt();
            System.out.println("Insira outro número inteiro: ");
            vetor[3] = banana.nextInt();
            vetor[4]= vetor[1] + vetor[2] + vetor[3];
            System.out.println("A soma dos 3 valores é: " + vetor[4]);
        } catch (java.util.InputMismatchException e){
            System.out.println("Tipo errado inserido, a aplicação requer um número inteiro");
        }
    }   
}
