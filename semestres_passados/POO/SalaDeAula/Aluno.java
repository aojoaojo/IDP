public class Aluno extends Pessoa{

    public String curso;
    

    Aluno(String nome, String curso){
        super(nome);
        this.curso = curso;
    }

    public void imprimirAlunos(){
        System.out.println();
        System.out.println(nome);
        System.out.println(curso);
    }
}