import java.util.Scanner;

public class TestaTributavel {
    public static void main(String[] args) {

        while (true) {

            // receba o valor que será depositado na conta
            Scanner sc = new Scanner(System.in);
            System.out.println("Digite o valor a ser depositado: ");
            double valor = sc.nextDouble();

            // escolha o tipo de conta
            System.out.println("Digite o tipo de conta: ");
            System.out.println("1 - Conta Corrente");
            System.out.println("2 - Conta Poupança");
            System.out.println("3 - Seguro de Vida");
            System.out.println("4 - Sair");
            int tipoConta = sc.nextInt();
            if (tipoConta == 1) {
                ContaCorrente cc = new ContaCorrente();
                cc.deposita(valor);
                System.out.println("Tributos a serem pagos para conta corrente: " + cc.calculaTributos() + " reais");
            } else if (tipoConta == 2) {
                ContaPoupanca cp = new ContaPoupanca();
                cp.deposita(valor);
                System.out.println("Não há tributos para conta poupança!");
            } else if (tipoConta == 3) {
                SeguroDeVida sv = new SeguroDeVida();
                sv.calculaTributos();
                System.out.println("Tributos para seguro de vida: " + sv.calculaTributos() + " reais");
            } else if (tipoConta == 4) {
                System.out.println("Saindo da conta...");
                break;
            } else {
                System.out.println("Tipo de conta inválido!");
            }
        }

    }
}