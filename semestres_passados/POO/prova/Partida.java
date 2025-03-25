package prova;

//O Campeonato Brasileirix de Futebol experimentará um novo sistema de pontuação, sobre o
//resultado da partida, na próxima edição do evento. Atualmente, utiliza-se o tradicional 3-1-0 para
//vitória-empate-derrota. Pretende-se experimentar o seguinte critério de pontuação para as equipes
//ao final das partidas: 5 pontos para vitória por goleada, 4 pontos para vitória normal, 2 pontos para
//empate, 1 ponto para derrota normal e 0 pontos para derrota por goleada. A goleada é a diferença
//de 3 ou mais gols entre as duas equipes.
//Implemente uma especialização da classe ResultadoPartida para realizar o processamento do
//resultado da partida:
//⇒ Como entrada, você já receberá um objeto do tipo Partida com os 4 atributos preenchidos
//corretamente. Ver no quadro a seguir um exemplo de uso dessas classes.
//⇐ Como resultado, deseja-se obter a pontuação das equipes em um objeto do tipo Pontuacao

//public class Programa {
//2 public static void main ( String [ ] args ) {
//    3 ProcessadorPartidaNov Sistema processador = new ProcessadorPartidaNovoSistema ( );
//    4 Partidapartida1 = new Partida ( " Porangatú " , 1 , "Minaçú " , 3 ) ;
//    5 Pontuacao pontPartida 1 = processador.processarPontuacao (partida1 ) ;
//    6 }
//    7 }

public class Partida {
    private String time1;
    private String time2;
    private Integer golsTime1;
    private Integer golsTime2;

    public Partida(String time1, Integer golsTime1, String time2, Integer golsTime2) {
        this.time1 = time1;
        this.time2 = time2;
        this.golsTime1 = golsTime1;
        this.golsTime2 = golsTime2;
    }

// QUESTÃO 5:
    public int ProcessadorPontuacao(Partida partida) {
        int pontuacao = 0;
        if (partida.golsTime1 > partida.golsTime2) {
            if (partida.golsTime1 - partida.golsTime2 >= 3) {
                pontuacao = 5;
            } else {
                pontuacao = 4;
            }
        } else if (partida.golsTime1 < partida.golsTime2) {
            if (partida.golsTime2 - partida.golsTime1 >= 3) {
                pontuacao = 0;
            } else {
                pontuacao = 1;
            }
        } else {
            pontuacao = 2;
        }
        return pontuacao;
    }

    public String getTime1() {
        return time1;
    }

    public String getTime2() {
        return time2;
    }

    public Integer getGolsTime1() {
        return golsTime1;
    }

    public Integer getGolsTime2() {
        return golsTime2;
    }
    
}