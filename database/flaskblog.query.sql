-- ----------------------------------- --
-- Testes de SELECT                    --
-- Dica: execute uma linha de cada vez --
-- ----------------------------------- --

-- Mostra todos os registros da tabela 'staff' --
SELECT * FROM staff;

-- Filtra staff pelo id
SELECT * FROM staff WHERE emp_id = '5';

-- Filtra staff pelo nome
SELECT * FROM staff WHERE emp_name = 'Maria Oliveira';

-- Ordena lista de staff pelo nome
-- Torque entre 'DESC' e 'ASC' para testar a ordem
SELECT * FROM staff ORDER BY emp_name DESC;

-- Somente campos específicos
-- Somente o tipo 'author'
-- Ordena pelo nome
SELECT emp_id, emp_name, emp_email 
	FROM staff 
    WHERE emp_type = 'author' 
    ORDER BY emp_name;

-- Mostra todos os registros da tabela 'article' --
SELECT * FROM article;

-- Mostra todos os registros da tabela 'comment' --
SELECT * FROM comment;
