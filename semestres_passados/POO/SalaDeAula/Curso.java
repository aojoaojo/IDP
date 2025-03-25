public class Curso{

    public String nome;
    public String disciplina[];
    

    Curso(String nome, String disciplina[]){
        this.nome = nome;
        this.disciplina = disciplina;
    }

    public void imprimirCurso(){
        System.out.println();
        System.out.println(nome);
        System.out.println(disciplina);
    }
}