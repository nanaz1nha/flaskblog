-- Apaga o banco de dados caso exista
-- PERIGO!!! Não execute este comando em produção
DROP DATABASE IF EXISTS flaskblog;

-- Cria o banco de dados
-- PERIGO!!! Não execute este comando em produção
CREATE DATABASE flaskblog 
	-- Define a tabela de caracteres UTF-8 para acentuação
	CHARACTER SET utf8mb4 
    -- As pesquisas são em UTF-8 e case-insensitive
    COLLATE utf8mb4_general_ci;
 
-- Seleciona o banco de dados criado
USE flaskblog; 