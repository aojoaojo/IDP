-- Criando tabela de Clientes
CREATE TABLE Clientes (
  ID int PRIMARY KEY,
  Nome varchar(50) NOT NULL,
  Endereço varchar(100) NOT NULL,
  Telefone varchar(20) NOT NULL
);

-- Inserindo exemplos de dados na tabela de Clientes
INSERT INTO Clientes (ID, Nome, Endereço, Telefone)
VALUES
  (1, 'João Silva', 'Rua A, 123', '(11) 9999-9999'),
  (2, 'Maria Santos', 'Av. B, 456', '(22) 8888-8888'),
  (3, 'José Oliveira', 'Rua C, 789', '(33) 7777-7777');

-- Criando tabela de Produtos
CREATE TABLE Produtos (
  ID int PRIMARY KEY,
  Nome varchar(50) NOT NULL,
  Preço decimal(10,2) NOT NULL
);

-- Inserindo exemplos de dados na tabela de Produtos
INSERT INTO Produtos (ID, Nome, Preço)
VALUES
  (1, 'Camisa Polo', 49.99),
  (2, 'Calça Jeans', 79.99),
  (3, 'Tênis Esportivo', 129.99);

-- Criando tabela de Funcionários
CREATE TABLE Funcionários (
  ID int PRIMARY KEY,
  Nome varchar(50) NOT NULL,
  Cargo varchar(50) NOT NULL,
  Salário decimal(10,2) NOT NULL
);

-- Inserindo exemplos de dados na tabela de Funcionários
INSERT INTO Funcionários (ID, Nome, Cargo, Salário)
VALUES
  (1, 'Ana Souza', 'Gerente', 5000.00),
  (2, 'Paulo Santos', 'Vendedor', 2000.00),
  (3, 'Rafaela Oliveira', 'Assistente Administrativo', 3000.00);

-- Criando tabela de Pedidos
CREATE TABLE Pedidos (
  ID int PRIMARY KEY,
  Data date NOT NULL,
  Cliente_ID int NOT NULL,
  Funcionário_ID int NOT NULL,
  FOREIGN KEY (Cliente_ID) REFERENCES Clientes(ID),
  FOREIGN KEY (Funcionário_ID) REFERENCES Funcionários(ID)
);

-- Inserindo exemplos de dados na tabela de Pedidos
INSERT INTO Pedidos (ID, Data, Cliente_ID, Funcionário_ID)
VALUES
  (1, '2022-05-01', 1, 2),
  (2, '2022-05-03', 2, 3),
  (3, '2022-05-05', 3, 1);

-- Criando tabela de Itens de Pedido
CREATE TABLE Itens_de_Pedido (
  ID int PRIMARY KEY,
  Pedido_ID int NOT NULL,
  Produto_ID int NOT NULL,
  Quantidade int NOT NULL,
  FOREIGN KEY (Pedido_ID) REFERENCES Pedidos(ID),
  FOREIGN KEY (Produto_ID) REFERENCES Produtos(ID)
);

-- Inserindo exemplos de dados na tabela de Itens de Pedido
INSERT INTO Itens_de_Pedido (ID, Pedido_ID, Produto_ID, Quantidade)
VALUES
  (1, 1, 1, 2),
  (2, 1, 2, 1),
  (3, 2, 3, 1),
  (4, 3, 1, 3);


-- Selecione o nome dos clientes que fizeram pedidos de pelo menos um produto com preço inferior a R$ X:
SELECT DISTINCT c.Nome
FROM Clientes c
INNER JOIN Pedidos p ON c.ID = p.Cliente_ID
INNER JOIN Itens_de_Pedido ip ON p.ID = ip.Pedido_ID
INNER JOIN Produtos prod ON ip.Produto_ID = prod.ID
WHERE prod.Preço < 10;


--  Selecione o nome e o cargo dos funcionários com salário superior a R$ X:
SELECT Nome, Cargo
FROM Funcionários
WHERE Salário > 500;

--  Selecione o nome e o preço dos produtos que foram pedidos pelos clientes que residem no endereço 'Rua X':
SELECT DISTINCT prod.Nome, prod.Preço
FROM Produtos prod
INNER JOIN Itens_de_Pedido ip ON prod.ID = ip.Produto_ID
INNER JOIN Pedidos p ON ip.Pedido_ID = p.ID
INNER JOIN Clientes c ON p.Cliente_ID = c.ID
WHERE c.Endereço = 'Rua X';

--  Selecione o nome dos clientes que não fizeram pedidos:
SELECT c.Nome
FROM Clientes c
WHERE c.ID NOT IN (SELECT DISTINCT p.Cliente_ID FROM Pedidos p);

--  Selecione o nome do produto mais vendido:
SELECT prod.Nome
FROM Produtos prod
INNER JOIN Itens_de_Pedido ip ON prod.ID = ip.Produto_ID
GROUP BY prod.Nome
ORDER BY SUM(ip.Quantidade) DESC
LIMIT 1;


--  Selecione o nome dos clientes que fizeram pelo menos um pedido em todas as datas em que a loja esteve aberta:
SELECT c.Nome
FROM Clientes c
WHERE NOT EXISTS (
    SELECT DISTINCT p.Data
    FROM Pedidos p
    WHERE NOT EXISTS (
        SELECT DISTINCT c.ID
        FROM Clientes c
        INNER JOIN Pedidos p2 ON c.ID = p2.Cliente_ID
        WHERE p2.Data = p.Data
    )
);


--  Selecione o nome do produto com preço máximo:
SELECT Nome
FROM Produtos
WHERE Preço = (SELECT MAX(Preço) FROM Produtos);


--  Selecione o nome e a quantidade vendida de todos os produtos que foram vendidos pelo menos uma vez:
SELECT prod.Nome, SUM(ip.Quantidade)
FROM Produtos prod
INNER JOIN Itens_de_Pedido ip ON prod.ID = ip.Produto_ID
GROUP BY prod.Nome;

--Uma maneira de selecionar uma relação com nome de clientes e nome de funcionários que não estão envolvidos em nenhum pedid
--seria utilizar a operação de junção externa esquerda para unir a tabela de clientes com a tabela de pedidos, usando a coluna de chave
--estrangeira do cliente como critério de junção. Em seguida, podemos selecionar as linhas que possuem valores nulos na coluna de chave estrangeira
--da tabela de pedidos, o que indica que não há nenhum pedido associado a esse cliente.
--Podemos então unir o resultado anterior com a tabela de funcionários, também usando a operação de junção externa esquerda,
--dessa vez utilizando a coluna de chave estrangeira do funcionário como critério de junção. Novamente, podemos selecionar as linhas que possuem 
--valores nulos na coluna de chave estrangeira da tabela de pedidos, o que indica que não há nenhum pedido associado a esse funcionário.
--Duas expressões que levariam a esse resultado seriam:

--Utilizando subconsultas:
SELECT c.nome, f.nome 
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.Cliente_ID
LEFT JOIN Funcionários f ON p.Funcionário_ID = f.id
WHERE p.id IS NULL
AND f.id NOT IN (SELECT id FROM pedidos);

--Utilizando a cláusula EXISTS:
SELECT c.nome, f.nome
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.Cliente_ID
LEFT JOIN Funcionários f ON p.Funcionário_ID = f.id
WHERE NOT EXISTS (SELECT * FROM pedidos p2 WHERE c.id = p2.Cliente_ID)
AND NOT EXISTS (SELECT * FROM pedidos p3 WHERE f.id = p3.Funcionário_ID);




































