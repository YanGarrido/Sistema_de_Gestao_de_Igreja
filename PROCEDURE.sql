DELIMITER $$

CREATE PROCEDURE ListarEventos()
BEGIN
    SELECT 
        e.nome AS evento_nome,
        e.descricao AS evento_descricao,
        e.tipo AS evento_tipo,
        l.nome AS local_nome,
        e.data_inicio AS evento_data_inicio,
        e.numero_participantes AS evento_capacidade
    FROM eventos e
    LEFT JOIN locais l ON e.id_local = l.id_local;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE ListarMinisterios()
BEGIN
    SELECT 
        m.nome AS ministerio_nome,
        m.descricao AS ministerio_descricao,
        m.lider AS ministerio_lider
    FROM ministerio m;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE ListarReunioesPorMinisterio(IN membro_id INT)
BEGIN
    SELECT 
        r.nome AS reuniao_nome,
        r.data_inicio AS reuniao_data_inicio,
        l.nome AS local_nome
    FROM reunioes r
    JOIN membro_ministerio mm ON r.id_ministerio = mm.id_ministerio
    JOIN locais l ON r.id_local = l.id_local
    WHERE mm.id_membro = membro_id;
END$$

DELIMITER ;

--Script de listar eventos
DELIMITER //
CREATE PROCEDURE ListarEventosPorLocal(IN id_local INT)
BEGIN
    SELECT E.id_evento, E.nome, E.descricao, E.tipo, E.data_inicio, E.data_fim
    FROM Eventos E
    WHERE E.id_local = id_local;
END //
DELIMITER ;




