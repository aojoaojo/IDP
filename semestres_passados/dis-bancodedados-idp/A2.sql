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

insert into Pedidos(data, cliente_id , funcionario_id) values
	('2024-01-01', 6, 1);


-- Inserindo Itens de Pedido
insert into "Itens de Pedido"(Pedido_ID, Produto_ID , Quantidade) values
	(6, 5, 2),
	(2, 2, 1),
	(3, 1, 1);



CREATE VIEW TODOS AS
SELECT Pedidos.ID AS Pedido_ID, Pedidos.Data, 
       Clientes.ID AS Cliente_ID, Clientes.Nome AS Cliente_Nome,
       Clientes.Endereço AS Cliente_Endereço, Clientes.Telefone AS Cliente_Telefone,
       Funcionários.ID AS Funcionário_ID, Funcionários.Nome AS Funcionário_Nome,
       Funcionários.Cargo, Funcionários.Salário,
       "Itens de Pedido".ID AS Item_ID, "Itens de Pedido".Quantidade, 
       Produtos.Nome AS Produto_Nome, Produtos.Preço
FROM Pedidos
INNER JOIN Clientes ON Pedidos.Cliente_ID = Clientes.ID
INNER JOIN Funcionários ON Pedidos.Funcionario_ID = Funcionários.ID
INNER JOIN "Itens de Pedido" ON Pedidos.ID = "Itens de Pedido".Pedido_ID
INNER JOIN Produtos ON "Itens de Pedido".Produto_ID = Produtos.ID;

CREATE VIEW TODOS_SEM_FILTRO AS
SELECT Pedidos.ID AS Pedido_ID, Pedidos.Data, 
       Clientes.ID AS Cliente_ID, Clientes.Nome AS Cliente_Nome,
       Clientes.Endereço AS Cliente_Endereço, Clientes.Telefone AS Cliente_Telefone,
       Funcionários.ID AS Funcionário_ID, Funcionários.Nome AS Funcionário_Nome,
       Funcionários.Cargo, Funcionários.Salário,
       "Itens de Pedido".ID AS Item_ID, "Itens de Pedido".Quantidade, 
       Produtos.Nome AS Produto_Nome, Produtos.Preço
FROM Pedidos, Funcionários, produtos, "Itens de Pedido", Clientes;


-- questao 1

select t.cliente_nome
from todos t
where quantidade >=1
and preço < 1000;

-- questao 2

select c.nome, f.nome 
from clientes c, funcionários f, pedidos p 
where c.id = p.cliente_id 
and f.id = p.funcionario_id
and p."data" > '01-03-2023'
union (select c.nome, f.nome 
from clientes c
left join pedidos p on c.id = p.cliente_id
left join funcionários f on p.funcionario_id = f.id 
where p.id is NULL);

-- questao 3

















