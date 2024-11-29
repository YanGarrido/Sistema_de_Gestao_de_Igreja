-- foi
DELIMITER $$

CREATE TRIGGER before_ministerio_insert
BEFORE INSERT ON ministerio
FOR EACH ROW
BEGIN
    DECLARE count_lider INT;

    SELECT COUNT(*) INTO count_lider
    FROM ministerio
    WHERE lider = NEW.lider;

    IF count_lider > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Este membro já é líder de outro ministério.';
    END IF;
END$$

DELIMITER ;

-- foi
DELIMITER $$

CREATE TRIGGER before_evento_insert
BEFORE INSERT ON eventos
FOR EACH ROW
BEGIN
    DECLARE capacidade_local INT;
    
    SELECT capacidade INTO capacidade_local
    FROM locais
    WHERE id_local = NEW.id_local;

    IF NEW.numero_participantes > capacidade_local THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O número de participantes excede a capacidade do local.';
    END IF;
END$$

DELIMITER ;

-- foi
DELIMITER $$

CREATE TRIGGER after_membro_insert
AFTER INSERT ON membros
FOR EACH ROW
BEGIN
    INSERT INTO log_membros (id_membro, nome, email, acao)
    VALUES (NEW.id_membro, NEW.nome, NEW.email, 'INSERT');
END$$

DELIMITER ;
-- foi
DELIMITER $$

CREATE TRIGGER ImpedirEventoSemLocal
BEFORE INSERT ON eventos
FOR EACH ROW
BEGIN
    IF NEW.id_local IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O evento deve ser associado a um local.';
    END IF;
END$$

DELIMITER ;
-- foi
DELIMITER //

CREATE TRIGGER ImpedirReuniaoNoPassado
BEFORE INSERT ON reunioes
FOR EACH ROW
BEGIN
    IF NEW.data_inicio < NOW() THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A data de início da reunião não pode ser no passado.';
    END IF;
END //

DELIMITER ;

-- foi
DELIMITER //

CREATE TRIGGER VerificarDataFimEvento
BEFORE INSERT ON eventos
FOR EACH ROW
BEGIN
    IF NEW.data_fim < NEW.data_inicio THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A data de término não pode ser anterior à data de início.';
    END IF;
END //

DELIMITER ;

SHOW TRIGGERS FROM Igreja

--Script de verificar email duplicado
DELIMITER //

CREATE TRIGGER verificaremaildupli
BEFORE INSERT ON Membros
FOR EACH ROW
BEGIN
    -- Verifica se o e-mail já existe na tabela Membros
    IF EXISTS (SELECT 1 FROM Membros WHERE email = NEW.email) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'E-mail já está registrado!';
    END IF;
END //

DELIMITER ;
