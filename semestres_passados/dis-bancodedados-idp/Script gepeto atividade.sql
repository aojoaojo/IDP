-- Consulta 1: Selecione o nome dos clientes que fizeram pedidos de pelo menos um produto com preço inferior a R$ 1000.
SELECT c.Nome
FROM Clientes c
WHERE EXISTS (
    SELECT 1
    FROM Pedidos p
    INNER JOIN "Itens de Pedido" ip ON p.ID = ip.Pedido_ID
    INNER JOIN Produtos pr ON ip.Produto_ID = pr.ID
    WHERE p.Cliente_ID = c.ID AND pr.Preço < 1000
);

-- Consulta 2: Selecione o nome dos clientes e nome dos funcionários envolvidos em pedidos feitos depois de 01/03/2023. Inclua também o nome dos clientes que não fizeram pedidos.
SELECT c.Nome, f.Nome
FROM Clientes c
FULL JOIN Pedidos p ON c.ID = p.Cliente_ID
LEFT JOIN Funcionários f ON p.Funcionario_ID = f.ID
WHERE p.Data > '2023-03-01' OR p.ID IS NULL;

-- Consulta 3: Selecione o nome dos clientes e nome dos funcionários envolvidos em quaisquer pedidos. Inclua também o nome dos funcionários que não venderam pedidos para clientes.
SELECT c.Nome, f.Nome
FROM Clientes c
LEFT JOIN Pedidos p ON c.ID = p.Cliente_ID
FULL JOIN Funcionários f ON p.Funcionario_ID = f.ID;

-- Consulta 4: Selecione o nome dos clientes que não fizeram nenhum pedido. Liste, pelo menos, duas expressões que levariam a esse resultado.
SELECT c.Nome
FROM Clientes c
LEFT JOIN Pedidos p ON c.ID = p.Cliente_ID
WHERE p.ID IS NULL;

SELECT c.Nome
FROM Clientes c
WHERE NOT EXISTS (
    SELECT 1
    FROM Pedidos p
    WHERE p.Cliente_ID = c.ID
);

-- Consulta 5: Selecione os nomes dos produtos que foram vendidos por funcionários que têm como cargo 'Vendedor'.
SELECT pr.Nome
FROM Produtos pr
INNER JOIN "Itens de Pedido" ip ON pr.ID = ip.Produto_ID
INNER JOIN Pedidos p ON ip.Pedido_ID = p.ID
INNER JOIN Funcionários f ON p.Funcionario_ID = f.ID
WHERE f.Cargo = 'Vendedor';

-- Consulta 6: Selecione uma relação com nome de clientes e nome de funcionários que não estão envolvidos em nenhum pedido. Liste, pelo menos, duas expressões que levariam a esse resultado.
SELECT c.Nome, f.Nome
FROM Clientes c
CROSS JOIN Funcionários f
WHERE NOT EXISTS (
    SELECT 1
    FROM Pedidos p
    WHERE p.Cliente_ID = c.ID AND p.Funcionario_ID = f.ID
);

SELECT c.Nome, f.Nome
FROM Clientes c
CROSS JOIN Funcionários f
LEFT JOIN Pedidos p ON c.ID = p.Cliente_ID AND f.ID = p.Funcionario_ID
WHERE p.ID IS NULL;

-- Consulta 7: Selecione os nomes dos produtos e nomes dos clientes que compraram produtos cuja quantidade supera 100 unidades.
SELECT pr.Nome, c.Nome
FROM Produtos pr
INNER JOIN "Itens de Pedido" ip ON pr.ID = ip.Produto_ID
INNER JOIN Pedidos p ON ip.Pedido_ID = p.ID
INNER JOIN Clientes c ON p.Cliente_ID = c
