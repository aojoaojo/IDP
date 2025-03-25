-- Criando tabela Clientes
create table Clientes (
    ID serial primary key,
    Nome varchar(255) not null,
    Endereço varchar(255) not null,
    Telefone varchar(13) not null
);

create table Produtos (
	ID serial primary key,
	Nome varchar(255) not null,
	Preço decimal not null
);

create table Funcionários (
	ID serial primary key,
	Nome varchar(255) not null,
	Cargo varchar(255) not null,
	Salário decimal not null
);

create table Pedidos (
	ID serial primary key,
	Data date not null,
	Cliente_ID int not null,
	Funcionário_ID int not null,
	foreign key (Cliente_ID) references Clientes(ID),
	foreign key (Funcionário_ID) references Funcionários(ID)
);

create table Itens_de_pedidos (
	ID serial primary key,
	Pedido_ID int not null,
	Produto_ID int not null,
	foreign key (Pedido_ID) references Pedidos(ID),
	foreign key (Produto_ID) references Produtos(ID),
	Quantidade int not null
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
	('Ciclano','Médico', 200),
	('Beltrano', 'Auditor', 25000);

-- Inseriondo Clientes
insert into Clientes(Nome, Endereço, telefone) values
	('Carlos', 'Sobradinho', '5561525896325'),
	('Caio','Asa Norte', '5561525852325'),
	('Rafael', 'Noroeste', '5561525843325'),
	('Brisa','Sudoeste', '5561525745325'),
	('Letícia','Asa Sul', '5561525320025'),
	('Jairo', 'Rua A', '5561525896325');

-- Inseriondo Pedidos
insert into Pedidos(data, cliente_id , Funcionário_ID) values
	('2022-01-01', 1, 1),
	('2022-01-02',2, 1),
	('2022-02-01',3, 1),
	('2023-01-01',4, 1),
	('2024-01-01',6, 1),
	('2022-01-01', 6, 1);

-- Inserindo Itens de Pedido
insert into Itens_de_pedidos(Pedido_ID, Produto_ID , Quantidade) values
	(6, 5, 2),
	(2, 2, 1),
	(3, 1, 1);


--quest 1
select c.nome
from Clientes c, Produtos p, Itens_de_pedidos idp, Pedidos p2
where c.ID = p2.Cliente_ID
and p2.ID = idp.Pedido_ID
and p.ID = idp.Produto_ID
and p.Preço > 1000;

--quest 2
select distinct c.nome, f.nome
from Clientes c, Funcionários f, Itens_de_pedidos idp, Pedidos p2
where c.ID = p2.Cliente_ID
and p2.Funcionário_ID = f.id
and p2.data > '01-03-2023';

--quest 3









