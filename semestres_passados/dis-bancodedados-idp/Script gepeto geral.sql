-- Consulta 1: Exemplo de consulta simples
SELECT *
FROM Tabela;

-- Consulta 2: Utilização de cláusula WHERE para filtrar resultados
SELECT *
FROM Tabela
WHERE Coluna = valor;

-- Consulta 3: Utilização de cláusula ORDER BY para ordenar resultados
SELECT *
FROM Tabela
ORDER BY Coluna;

-- Consulta 4: Uso de cláusula JOIN para combinar dados de várias tabelas
SELECT *
FROM Tabela1
JOIN Tabela2 ON Tabela1.Chave = Tabela2.Chave;

-- Consulta 5: Utilização de funções de agregação (COUNT, SUM, AVG, etc.)
SELECT COUNT(*) AS Total
FROM Tabela;

-- Consulta 6: Utilização de subconsultas
SELECT *
FROM Tabela1
WHERE Coluna IN (SELECT Coluna FROM Tabela2);

-- Consulta 7: Utilização de expressões condicionais (CASE)
SELECT Coluna,
       CASE
           WHEN Coluna = valor THEN 'Condição 1'
           WHEN Coluna = outro_valor THEN 'Condição 2'
           ELSE 'Condição padrão'
       END AS Resultado
FROM Tabela;

-- Consulta 8: Uso de cláusulas GROUP BY e HAVING
SELECT Coluna, COUNT(*) AS Total
FROM Tabela
GROUP BY Coluna
HAVING COUNT(*) > 10;

-- Consulta 9: Utilização de junções externas (LEFT JOIN, RIGHT JOIN)
SELECT *
FROM Tabela1
LEFT JOIN Tabela2 ON Tabela1.Chave = Tabela2.Chave;

-- Consulta 10: Utilização de operadores de conjunto (UNION, INTERSECT, EXCEPT)
SELECT Coluna
FROM Tabela1
UNION
SELECT Coluna
FROM Tabela2;

-- Consulta 11: Uso de cláusula LIMIT para limitar o número de resultados
SELECT *
FROM Tabela
LIMIT 10;

-- Consulta 12: Utilização de funções de data e hora
SELECT *
FROM Tabela
WHERE data_coluna BETWEEN '2023-01-01' AND '2023-12-31';

-- Consulta 13: Utilização de cláusula DISTINCT para retornar valores únicos
SELECT DISTINCT Coluna
FROM Tabela;

-- Consulta 14: Uso de expressões de string (CONCAT, SUBSTRING, LENGTH, etc.)
SELECT CONCAT(FirstName, ' ', LastName) AS FullName
FROM Tabela;

-- Consulta 15: Utilização de cláusula WHERE com múltiplas condições
SELECT *
FROM Tabela
WHERE Coluna1 = valor1 AND Coluna2 = valor2;

-- Consulta 16: Utilização de operadores lógicos (AND, OR, NOT)
SELECT *
FROM Tabela
WHERE Coluna1 = valor1 OR (Coluna2 = valor2 AND Coluna3 = valor3);
