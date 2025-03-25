CREATE TABLE Alunos (
  ID_Aluno SERIAL PRIMARY KEY,
  Nome_Aluno VARCHAR(255),
  CPF VARCHAR(14)
);

CREATE TABLE Disciplinas (
  ID_Disciplina SERIAL PRIMARY KEY,
  Nome_Disciplina VARCHAR(255),
  Carga_Horaria INT
);

CREATE TABLE Notas (
  ID_Nota SERIAL PRIMARY KEY,
  ID_Aluno INT,
  ID_Disciplina INT,
  Nota DECIMAL(5,2)
);

INSERT INTO Alunos (Nome_Aluno, CPF) VALUES
('João da Silva', '111.111.111-11'),
('Maria Souza', '222.222.222-22'),
('Fernando Santos', '333.333.333-33'),
('Ana Paula Vieira', '444.444.444-44'),
('Lucas Pereira', '555.555.555-55'),
('Juliana Oliveira', '666.666.666-66'),
('Rodrigo Almeida', '777.777.777-77'),
('Patricia Gomes', '888.888.888-88'),
('Gustavo Lima', '999.999.999-99'),
('Luana Martins', '000.000.000-00');

INSERT INTO Disciplinas (Nome_Disciplina, Carga_Horaria) VALUES
('Matemática', 80),
('Português', 60),
('História', 50),
('Geografia', 50),
('Ciências', 70),
('Inglês', 40);

-- Inserção de exemplos de notas
INSERT INTO Notas (ID_Aluno, ID_Disciplina, Nota) VALUES
-- Notas do João da Silva
(1, 1, NULL),
(1, 2, 9.0),
(1, 3, 7.0),
(1, 4, 8.0),
(1, 5, 6.5),
(1, 6, 7.5),
-- Notas da Maria Souza
(2, 1, 9.0),
(2, 2, 7.5),
(2, 3, 8.0),
(2, 4, NULL),
(2, 5, 7.0),
(2, 6, 8.5),
-- Notas do Fernando Santos
(3, 1, 6.5),
(3, 2, 8.0),
(3, 3, 6.0),
(3, 4, 7.0),
(3, 5, 8.5),
(3, 6, 9.0),
-- Notas da Ana Paula Vieira
(4, 1, 7.5),
(4, 2, 9.0),
(4, 3, 7.5),
(4, 4, 8.0),
(4, 5, 9.5),
(4, 6, 7.0),
-- Notas do Lucas Pereira
(5, 1, 9.0),
(5, 2, 8.5),
(5, 3, 7.0),
(5, 4, 9.0),
(5, 5, 8.0),
(5, 6, 7.5),
-- Notas da Juliana Oliveira
(6, 1, 8.0),
(6, 2, 7.0),
(6, 3, 8.5),
(6, 4, 9.0),
(6, 5, 6.5),
(6, 6, 9.5),
-- Notas do Rodrigo Almeida
(7, 1, 7.0),
(7, 2, 8.5),
(7, 3, 9.0),
(7, 4, 6.5),
(7, 5, 7.5),
(7, 6, 8.0),
-- Notas da Patricia Gomes
(8, 1, 8.5),
(8, 2, 7.5),
(8, 3, 8.0),
(8, 4, 9.5),
(8, 5, 7.0),
(8, 6, 6.5),
-- Notas do Gustavo Lima
(9, 1, 6.0),
(9, 2, 7.5),
(9, 3, 8.5),
(9, 4, 6.5),
(9, 5, 9.0),
(9, 6, 8.0),
-- Notas da Luana Martins
(10, 1, 7.5),
(10, 2, 8.0),
(10, 3, 7.3),
(10, 4, 3.0),
(10, 5, 5.4),
(10, 6, 4.2);

-- Selecione os alunos que tiraram nota maior ou igual a 7 na disciplina de “Matemática”;
SELECT Alunos.Nome_Aluno, Notas.Nota
FROM Alunos
INNER JOIN Notas ON Alunos.ID_Aluno = Notas.ID_Aluno
INNER JOIN Disciplinas ON Notas.ID_Disciplina = Disciplinas.ID_Disciplina
WHERE Disciplinas.Nome_Disciplina = 'Matemática' AND Notas.Nota >= 7;

-- Lista o nome e o CPF dos alunos que não possuem notas cadastradas no sistema;
SELECT  Alunos.nome_aluno, Alunos.cpf
FROM alunos
inner join notas on alunos.id_aluno  = notas.id_aluno
inner join disciplinas on notas.id_disciplina  = disciplinas.id_disciplina
where notas.nota is null;

-- Selecione o nome das disciplinas que possuem carga horária maior que 60 horas;
select disciplinas.nome_disciplina
from disciplinas
where carga_horaria > 60;

-- Liste o nome das disciplinas e a média geral de notas dos alunos;
SELECT Disciplinas.Nome_Disciplina, AVG(Notas.Nota) AS Media_Geral
FROM Disciplinas
INNER JOIN Notas ON Disciplinas.ID_Disciplina = Notas.ID_Disciplina
GROUP BY Disciplinas.Nome_Disciplina;


drop table notas;

drop table alunos;



select Disciplias.Nome_Disciplina







