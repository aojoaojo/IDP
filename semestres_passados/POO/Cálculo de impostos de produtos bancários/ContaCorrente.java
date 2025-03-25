//A interface Tributavel possui o método calculaTributos() que retorna um double. A classe ContaCorrente implementa a interface Tributavel e sobrescreve o método calculaTributos().

public class ContaCorrente extends Conta implements Tributavel {
    // outros atributos e métodos aqui!
    public double calculaTributos() {
        return this.getSaldo() * 0.01;
    }
}
