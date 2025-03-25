-- Criando tabela Clientes
create table Clientes (
    ID serial primary key,
    Nome varchar(255) not null,
    Endereço varchar(255) not null,
    Telefone varchar(13) not null
);

-- Criando tabela Produtos
create table Produtos (
    ID serial primary key,
    Nome varchar(255) not null,
    Preço decimal not null
);

-- Criando tabela Funcionários
create table Funcionários (
    ID serial primary key,
    Nome varchar(255) not null,
    Cargo varchar(255) not null,
    Salário decimal not null
);

-- Criando tabela pedidos
create table Pedidos (
    ID serial primary key,
    Data date not null,
    Cliente_ID int not null,
    Funcionario_ID int not null,
    foreign key (cliente_ID) references Clientes (ID),
    foreign key (Funcionario_ID) references Funcionários (ID)
);

-- Criando tabela itens de pedido
create table "Itens de Pedido" (
    ID serial primary key,
    Pedido_ID int not null,
    Produto_ID int not null,
    Quantidade int not null,
    foreign key (Pedido_ID) references Pedidos (ID),
    foreign key (Produto_ID) references Produtos (ID)
);

-- Inserindo na Tabela Produtos
insert into Produtos(Nome, Preço) values
	('Vassoura', 10),
	('Chiclete', 3.5),
	('Melancia', 15),
	('Shampoo', 40);

insert into Produtos(Nome, Preço) values
	('Ferrari', 540000),
	('Bicicleta', 1500),
	('Bolinha de gude de ouro', 4000),
	('Tenis nike', 400);

-- Inserindo funcionário na tabela Funcinários
insert into Funcionários(Nome, Cargo, Salário) values
	('Joao', 'Herdeiro', 550000),
	('Nilson','CEO de empresa multibilionária', 50000),
	('Laura', 'Chefa', 20000),
	('Fulano','Operador', 400),
	('Ciclano','Médico', 200);
insert into Funcionários(Nome, Cargo, Salário) values
	('Beltrano', 'Auditor', 25000);

-- Inseriondo Clientes
insert into Clientes(Nome, Endereço, telefone) values
	('Carlos', 'Sobradinho', '5561525896325'),
	('Caio','Asa Norte', '5561525852325'),
	('Rafael', 'Noroeste', '5561525843325'),
	('Brisa','Sudoeste', '5561525745325'),
	('Letícia','Asa Sul', '5561525320025');
insert into Clientes(Nome, Endereço, telefone) values
	('Jairo', 'Rua A', '5561525896325');

-- Inseriondo Pedidos
insert into Pedidos(data, cliente_id , funcionario_id) values
	('2022-01-01', 1, 1),
	('2022-01-02',2, 1),
	('2022-02-01',3, 1),
	('2023-01-01',4, 1),
	('2022-01-01',6, 1);
insert into Pedidos(data, cliente_id , funcionario_id) values
	('2022-01-01', 6, 1);

-- Inserindo Itens de Pedido
insert into "Itens de Pedido"(Pedido_ID, Produto_ID , Quantidade) values
	(6, 5, 2),
	(2, 2, 1),
	(3, 1, 1);

-- QUESTAO 1
-- Selecionando nome e preço dos produtos e ordenando de forma decrescente
select Nome, Preço
from Produtos
order by Preço desc;

-- QUESTAO 2
-- Selecionando nome e preço dos produtos que custam mais de 1000 reais
select Nome, Preço
from Produtos
where Preço > 1000;

-- QUESTAO 3
-- Selecionando nome e salário dos funcionários que ganham mais de 5000 reais
select Nome, Salário
from Funcionários
where Salário > 5000
order by salário desc;

-- QUESTAO 4
-- Selecionando nome e endereço dos clientes que fizeram pedido na data 2022-01-01
select Nome, Endereço
from Clientes c, pedidos p 
where c.ID = p.cliente_ID
and p."data" = '2022-01-01';

-- QUESTAO 5
-- Selecione o nome dos produtos comprados pelos clientes que moram na "Rua A"
select p.Nome
from produtos p, clientes c, pedidos p2, "Itens de Pedido" idp 
where c.ID = p2.cliente_id
and p.id = idp.produto_id
and p2.id = idp.pedido_id 
and c.endereço  = 'Rua A';

-- Mesma coisa, mas dessa vez o nome não repete, independete da quantidade de vezes que o produto foi vendido e o 'rua A' pode aparecer em qualquer lugar da string
select distinct p.Nome
from produtos p, clientes c, pedidos p2, "Itens de Pedido" idp 
where c.ID = p2.cliente_id
and p.id = idp.produto_id
and p2.id = idp.pedido_id 
and c.endereço  ilike 'Rua A';

-- QUESTAO 6
-- Exiba em ordem alfabética o nome dos clientes que fizeram um pedido maior que 2000 reais 
select c.Nome
from produtos p, clientes c, pedidos p2, "Itens de Pedido" idp 
where c.ID = p2.cliente_id
and p.id = idp.produto_id
and p2.id = idp.pedido_id 
and p.preço > 2000
order by c.nome;

-- QUESTAO 7
-- Exiba o texto "os funcionarios "
select 'o vendedor', f.nome,'foi responsável pelo pedido', p2.id,'realizado pelo cliente', c.nome
from produtos p, clientes c, pedidos p2, "Itens de Pedido" idp, funcionários f 
where c.ID = p2.cliente_id
and p.id = idp.produto_id
and p2.id = idp.pedido_id
and p2.funcionario_ID = f.id;

-- QUESTAO 8
-- Exiba o texto "os funcionarios "

select distinct ' o vendedor ' || f.nome || ' vendeu o produto ' || p.nome || ' para o cliente ' || c.nome
from produtos p, clientes c, pedidos p2, "Itens de Pedido" idp, funcionários f 
where c.ID = p2.cliente_id
and p.id = idp.produto_id
and p2.id = idp.pedido_id
and p2.funcionario_ID = f.id;


-- QUESTAO 9
-- Exiba o texto "os funcionarios "

create view todos_vendedores as
select f.id from Funcionários f;

create view vendedores_pedidos as
select p.funcionario_id from Pedidos p;

create view vendedores_sem_pedidos as
(select * from todos_vendedores) except (select * from vendedores_pedidos);

select 'O vendedor ' || f.nome || ' não realizou vendas' 
from vendedores_sem_pedidos vsp, funcionários f
where vsp.id = f.id;

-- QUESTAO 10
-- Exiba o texto "os funcionarios "

create view todos_clientes as
select c.id from clientes c ;

create view clientes_pedidos as
select p.cliente_id from Pedidos p;

create view clientes_sem_pedidos as
(select * from todos_clientes) except (select * from clientes_pedidos);

select 'O cliente ' || c.nome || ' não realizou nenhum pedido' 
from clientes_sem_pedidos csp, clientes c 
where csp.id = c.id;









