USE jogadores;
CREATE TABLE jogadores (nome string, idade int, CPF int);
INSERT INTO jogadores (nome, idade, CPF) VALUES ("josicreuson", 1900, 00000000011);
SELECT * FROM jogadores;
SELECT nome, idade FROM jogadores;
SELECT * FROM jogadores ORDER BY nome;
SELECT * FROM jogadores WHERE idade > 9023;
UPDATE jogadores SET nome = "josicreuson" WHERE nome = "victor";
DELETE FROM jogadores WHERE nome = "amarildo";TRUNCATE TABLE jogadores;