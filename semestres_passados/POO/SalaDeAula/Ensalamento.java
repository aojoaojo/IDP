public class Ensalamento {

	public static final int a = 13;
	public static final int b = 3;

	public static void main(String[] args) {

		Aluno vetorAluno[] = new Aluno[a];

		String[] nome = { "Alfredo", "Peterson", "Wendel", "Ian", "Debra", "Luana", "Bruno", "Romeu", "Julieta",
				"Maria", "Capitú", "Bentinho", "Amélia" };

		Professor vetorProfessores[] = new Professor[b];

		String[] professores = { "Mia", "Saulo", "Paula" };

		String[] disciplinas = { "POO", "Estrutura de Dados", "BI" };

		String[] cursos = { "C.C.", "C.C.", "Adm" };

		Disciplina disciplina[] = new Disciplina[b];

		for (int i = 0; i < b; i++) {

			disciplina[i] = new Disciplina(disciplinas[i], cursos[i]);

		}
		for (int i = 0; i < a; i++) {

			if (i % 2 == 0) {
				vetorAluno[i] = new Aluno(nome[i], "Administração");
			}

			else {
				vetorAluno[i] = new Aluno(nome[i], "Ciência da Computação");
			}
		}

		System.out.println("Alunos: ");

		for (int i = 0; i < a; i++) {
			vetorAluno[i].imprimirAlunos();
		}

		for (int i = 0; i < b; i++) {
			vetorProfessores[i] = new Professor(professores[i], disciplina[i].nome);
		}

		System.out.println();

		System.out.println("\n////////////////////////////////////////////////////////");

		System.out.println("\nProfessores: ");

		for (int i = 0; i < b; i++) {
			vetorProfessores[i].imprimirProfessores();
		}

		System.out.println("\n////////////////////////////////////////////////////////");
		System.out.println("\nDisciplinas: ");

		for (int i = 0; i < b; i++) {
			disciplina[i].imprimirDisciplina();
		}

	}
}
