-- SCRIPT DE PESQUISAR MEMBRO POR NOME

DELIMITER //
CREATE PROCEDURE PesquisarMembrosPorNome(IN nome_busca VARCHAR(100))
BEGIN
    SELECT * 
    FROM Membros 
    WHERE nome LIKE CONCAT('%', nome_busca, '%');
END //
DELIMITER ;
CALL PesquisarMembrosPorNome('luis');
