//QUESTÃO 3:
public class AcessoVisitante implements Valido {

    private Visitante visitante;
    private PontoControle pontoControle;
    private LocalDateTime dataHora;

    public AcessoVisitante(Visitante visitante, PontoControle pontoControle, LocalDateTime dataHora) {
        this.visitante = visitante;
        this.pontoControle = pontoControle;
        this.dataHora = dataHora;
    }

    @Override
    public boolean estahValido() {
        return visitante.estahValido() && pontoControle.estahValido();
    }
}