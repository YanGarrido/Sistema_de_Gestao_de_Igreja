CREATE DATABASE IF NOT EXISTS Igreja;
USE Igreja;

CREATE TABLE IF NOT EXISTS Membros (
id_membro INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nome VARCHAR(100),
email VARCHAR(100) UNIQUE,
telefone VARCHAR(20),
endereco TEXT,
data_nascimento DATE,
data_entrada DATE,
senha VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Ministerio (
id_ministerio INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nome VARCHAR(100) NOT NULL,
descricao TEXT,
lider VARCHAR(100)
);

-- Tabela Intermediária entre Membros e Ministérios
CREATE TABLE IF NOT EXISTS membro_ministerio (
    id_membro INT NOT NULL,
    id_ministerio INT NOT NULL,
    PRIMARY KEY (id_membro, id_ministerio),
    FOREIGN KEY (id_membro) REFERENCES membros(id_membro) ON DELETE CASCADE,
    FOREIGN KEY (id_ministerio) REFERENCES ministerio(id_ministerio) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS locais (	
    id_local INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco TEXT,
    capacidade INT,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS eventos (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    tipo VARCHAR(100),
    data_inicio DATETIME NOT NULL,
    data_fim DATETIME,
    id_local INT,
    numero_participantes INT,
    FOREIGN KEY (id_local) REFERENCES locais(id_local)
);

CREATE TABLE IF NOT EXISTS reunioes (
    id_reuniao INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    tipo VARCHAR(100),
    data_inicio DATETIME NOT NULL,
    data_fim DATETIME,
    id_ministerio INT,
    id_local INT,
    FOREIGN KEY (id_ministerio) REFERENCES ministerio(id_ministerio),
    FOREIGN KEY (id_local) REFERENCES locais(id_local)
);

CREATE TABLE IF NOT EXISTS log_membros (
    id_log INT AUTO_INCREMENT PRIMARY KEY,
    id_membro INT,
    nome VARCHAR(100),
    email VARCHAR(100),
    acao VARCHAR(50), -- INSERT, UPDATE ou DELETE
    data_alteracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
