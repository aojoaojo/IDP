CREATE TABLE departamentos (
  id_departamento SERIAL PRIMARY KEY,
  nome_departamento TEXT NOT NULL
);

CREATE TABLE funcionarios (
  id_funcionario SERIAL PRIMARY KEY,
  nome TEXT NOT NULL,
  salario NUMERIC(10,2) NOT NULL,
  id_departamento INTEGER references departamentos(id_departamento) NOT NULL
);

insert into departamentos (id_departamento, nome_departamento) values
(1,'Vendas'),
(2,'Marketing'),
(3,'TI')
;

insert into funcionarios (nome, salario, id_departamento) values
('João',5000,1),
('Maria',6000,2),
('Carlos',5500,1),
('Ana',4500,2),
('Paulo',7000,3),
('Lucia',6500,2)
;

-- Selecionar nomes e número de departamentos dos funcionários do departamento 1
SELECT nome, id_departamento
FROM funcionarios
WHERE id_departamento = 1
union all
-- Selecionar nomes e códigos de departamentos
SELECT nome_departamento, id_departamento
FROM departamentos;

-- f é o apelido para funcionários e d é o apelido para departamentos
SELECT f.nome, d.nome_departamento
FROM funcionarios f, departamentos d
WHERE f.id_departamento = d.id_departamento
AND f.id_departamento = 1;
-- Os apelidos são opcionais, mas não usá-los deixaria o comando muito extenso (faça o teste)

-- f é o apelido para funcionários e d é o aplicado para departamentos
SELECT f.nome, d.nome_departamento
FROM funcionarios f
join departamentos d on f.id_departamento = d.id_departamento 
where d.id_departamento = 1;
-- Os apelidos são opcionais, mas não usá-los deixaria o comando muito extenso (faça o teste)

insert into departamentos (id_departamento, nome_departamento) values
(4,'RH');

select nome_departamento from departamentos d
where id_departamento = (select d.id_departamento from departamentos d
except
select f.id_departamento from funcionarios f);

create view funcionarios_sem_departamento
as select d.id_departamento from departamentos d
except
select f.id_departamento from funcionarios f;

select 'O departamento ' || d.nome_departamento || ' não possui funcionários' 
from funcionarios_sem_departamento fsp, departamentos d
where fsp.id_departamento = d.id_departamento;

SELECT f.nome, d.nome_departamento
FROM funcionarios f
join departamentos d on f.id_departamento = d.id_departamento 
where d.id_departamento = 1;


