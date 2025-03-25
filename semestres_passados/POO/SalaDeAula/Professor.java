public class Professor extends Pessoa{
    public String disciplina;
    
    Professor(String nomeProfessor, String disciplina){
        super(nomeProfessor);
        this.disciplina = disciplina;
    }

    public void imprimirProfessores(){
        System.out.println();
        System.out.println(nome);
        System.out.println(disciplina);
    }
}