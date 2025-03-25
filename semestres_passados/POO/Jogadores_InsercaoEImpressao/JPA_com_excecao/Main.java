package JPA_com_excecao;

public class Main {
    public static void main(String[] args) {
        Jogador jogador1 = new Jogador("Rafael", "Mid", "FURIA", "Challanger");
        Jogador jogador2 = new Jogador("Lucas", "Top", "FURIA", "Mestre");
        Jogador jogador3 = new Jogador("João", "Jungler", "FURIA", "Prata");

        jogador1.imprimeJogador();
        jogador2.imprimeJogador();
        jogador3.imprimeJogador();
        
        Jogador jogador4 = new Jogador("Rafael", "Mid", "FURIA", "Challanger");
        Jogador jogador5 = new Jogador("Lucas", "Top", "FURIA", "Mestre");
        Jogador jogador6 = new Jogador("João", "Jungler", "FURIA", "Prata");

        jogador4.imprimeJogador();
        jogador5.imprimeJogador();
        jogador6.imprimeJogador();

    }
}
