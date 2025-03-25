//QUESTÃO 2:
public class AcessoVisitante {

    private Visitante visitante;
    private PontoControle pontoControle;
    private LocalDateTime dataHora;

    public AcessoVisitante(Visitante visitante, PontoControle pontoControle, LocalDateTime dataHora) {
        this.visitante = visitante;
        this.pontoControle = pontoControle;
        this.dataHora = dataHora;
    }
}