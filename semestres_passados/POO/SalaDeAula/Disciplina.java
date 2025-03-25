public class Disciplina{

    public String nome;
    public String curso;
    

    Disciplina(String nome, String curso){
        this.nome = nome;
        this.curso = curso;
    }

    public void imprimirDisciplina(){
        System.out.println();
        System.out.println(nome);
        System.out.println(curso);
    }
}
