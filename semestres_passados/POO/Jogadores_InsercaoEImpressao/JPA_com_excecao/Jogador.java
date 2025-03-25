public class Jogador {
    private String nome;
    private String funcao;
    private String time;
    private String patente;

    public Jogador(String nome, String funcao, String time, String patente) {
        this.nome = nome;
        this.funcao = funcao;
        this.time = time;
        this.patente = patente;
    }

    public String getNome() {
        return nome;
    }

    public String getFuncao() {
        return funcao;
    }

    public String getTime() {
        return time;
    }

    public String getPatente() {
        return patente;
    }    

    public void imprimeJogador() {
        System.out.println("Nome: " + this.nome);
        System.out.println("Função: " + this.funcao);
        System.out.println("Time: " + this.time);
        System.out.println("Patente: " + this.patente);
    }
}
