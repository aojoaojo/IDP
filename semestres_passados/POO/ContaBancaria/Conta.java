public class Conta{

    private final String nomeCliente;
    private final int agencia;
    private final int numero;
    private double saldo;

    Conta(String nome,int agencia, int numero, double saldo){

        this.nomeCliente = nome;
        this.agencia = agencia;
        this.numero = numero;
        this.saldo = saldo;
    }

    public void imprimirConta(){
        System.out.println();
        System.out.println(nomeCliente);
        System.out.println(agencia);
        System.out.println(numero);
        System.out.println(saldo);
        System.out.println();
    }

    public int getAgencia() {
        return agencia;
    }
    public String getNomeCliente() {
        return nomeCliente;
    }
    public int getNumero() {
        return numero;
    } 
    public double getSaldo() {
        return saldo;
    }
}