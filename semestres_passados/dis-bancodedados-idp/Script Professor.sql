-- CRIAÇÃO DE TABELAS 
create table clientes (
	id serial primary key, 
	nome varchar(255), 
	endereco varchar(255), 
	telefone varchar(14)
	);

create table produtos (
	id serial primary key,
	nome varchar(150),
	preço decimal(10, 2)
	);
	
create table funcionarios (
	id serial primary key,
	nome varchar(255),
	cargo varchar(100),
	salario decimal(10, 2)
	);
	
create table pedidos (
	id serial primary key,
	cliente_id int,
	funcionario_id int,
	data_ date,
	foreign key (cliente_id) references clientes(id),
	foreign key (funcionario_id) references funcionarios(id)
	);
	
create table itens_do_pedido (
	id serial primary key,
	pedido_id int,
	produto_id int,
	quantidade int,
	foreign key (pedido_id) references pedidos(id),
	foreign key (produto_id) references produtos(id)
	);
	
-- INSERINDO DADOS DAS TABELAS
insert into clientes(nome, endereco, telefone) values
	('maria', 'rua a', '12345'),
	('joao', 'av b', '12345'),
	('ana', 'rua c', '12345'),
	('pedro', 'rua a', '12345'),
	('carlos', 'brasilia', '12345');
	
insert into produtos(nome, preço) values
	('geladeira', 3000),
	('fogão', 1500),
	('microondas', 500),
	('lava-louças', 2000);
	
insert into funcionarios(nome, cargo, salario) values 
	('paulo', 'vendedor', 2000),
	('luiz', 'gerente', 5100),
	('ana', 'caixa', 1500),
	('mariana', 'estoquista', 1800);
	
insert into pedidos(cliente_id, funcionario_id, data_) values 
	(1, 1, '2022-03-10'),
	(1, 2, '2022-03-11'),
	(2, 2, '2022-03-12'),
	(1, 3, '2023-03-02'),
	(5, 1, '2023-03-03'),
	(5, 2, '2023-03-03');

insert into itens_do_pedido(pedido_id, produto_id, quantidade) values
	(1, 1, 1),
	(2, 2, 2),
	(3, 1, 3),
	(3, 2, 5),
	(3, 3, 101),
	(5, 1, 2),
	(5, 2, 3),
	(6, 1, 10),
	(6, 2, 3);

-- 1
select c.nome
from clientes c
join pedidos p on c.id = p.cliente_id
join itens_do_pedido idp on idp.pedido_id = p.id 
join produtos p2 on p2.id = idp.produto_id
where p2.preço  < 1000;

-- 2
select distinct c.nome as nome_cliente, f.nome as nome_funcionario
from clientes c
left join pedidos p on c.id = p.cliente_id
left join funcionarios f on f.id = p.funcionario_id
where p.data_  > '2023-03-01' or p.data_ is null;

-- 3
select distinct c.nome as nome_cliente, f.nome as nome_funcionario
from clientes c 
join pedidos p ON p.cliente_id = c.id
right join funcionarios f on p.funcionario_id = f.id;

-- 4
select c.nome
from clientes c
left join pedidos p on p.cliente_id = c.id
where p.id is null;


with id_clientes_sem_pedido as (
	select c.id
		from clientes c
		left join pedidos p on p.cliente_id = c.id
	except
	select c.id
		from clientes c
		join pedidos p on p.cliente_id = c.id
	)
select c.nome from clientes c
join id_clientes_sem_pedido on c.id = id_clientes_sem_pedido.id;

-- 5
select distinct p.nome
from produtos p
join itens_do_pedido idp on idp.produto_id = p.id
join pedidos p2 on p2.id = idp.pedido_id
join funcionarios f on f.id = p2.id
where f.cargo ilike '%vendedor%';

-- 6
(select c.nome
from clientes c
left join pedidos p on p.cliente_id = c.id
where p.id is null) 
union all
(select f.nome
from funcionarios f 
left join pedidos p on p.funcionario_id  = f.id
where p.id is null);

(with id_clientes_sem_pedido as  (
		select c.id
		from clientes c 
		left join pedidos p on p.cliente_id = c.id
	except
		select c.id
		from clientes c 
		join pedidos p on p.cliente_id = c.id
	)
select c.nome from clientes c
join id_clientes_sem_pedido on c.id = id_clientes_sem_pedido.id
)
	union all	
(with id_funcionarios_sem_pedido as (
		select f.id
		from funcionarios f
		left join pedidos p on p.funcionario_id = f.id
	except
		select f.id
		from funcionarios f
		join pedidos p on p.funcionario_id = f.id
	)
select f.nome from funcionarios f
join id_funcionarios_sem_pedido on f.id = id_funcionarios_sem_pedido.id
);

-- 7
select c.nome as nome_cliente, p2.nome  as nome_produto
from clientes c 
join pedidos p on p.cliente_id = c.id
join itens_do_pedido idp on idp.pedido_id = p.id
join produtos p2 on p2.id = idp.produto_id
where idp.quantidade > 100;

-- 8
select p2.nome as nome_produto, f.nome as nome_funcionario, c.nome as nome_cliente
from clientes c
join pedidos p on p.cliente_id = c.id
join funcionarios f on p.funcionario_id = f.id
join itens_do_pedido idp on idp.pedido_id = p.id
join produtos p2 on p2.id = idp.produto_id
where p2.preço > 100 and c.endereco ilike '%brasilia%';

-- 9
select p2.nome, sum(idp.quantidade) as soma_quantidade
from clientes c
join pedidos p on p.cliente_id = c.id
join funcionarios f on p.funcionario_id = f.id
join itens_do_pedido idp on idp.pedido_id = p.id
join produtos p2 on p2.id = idp.produto_id
where f.salario > 5000 and c.endereco ilike '%brasilia%'
group by p2.id, idp.quantidade
order by soma_quantidade desc
limit 1;

-- 10
(select distinct c.nome as nome_cliente, f.nome as nome_funcionario
from clientes c
join pedidos p on p.cliente_id = c.id
join funcionarios f on p.funcionario_id = f.id)
union
(select distinct c.nome as nome_cliente, f.nome as nome_funcionario
from clientes c
left join pedidos p on p.cliente_id = c.id
left join funcionarios f on p.funcionario_id = f.id
where p.id is null)
union
(select distinct c.nome as nome_cliente, f.nome as nome_funcionario
from funcionarios f
left join pedidos p on p.funcionario_id = f.id
left join clientes c on p.cliente_id = c.id
where p.id is null);



	