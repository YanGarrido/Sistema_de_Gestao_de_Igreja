-- SCRIPT DE PESQUISAS

-- Membros e os seus ministerios
SELECT m.nome, mi.nome
FROM membros m
INNER JOIN ministerio mi ON  mi.id_membro = m.id_membro
WHERE mi.id_membro = m.id_membro;

-- Todos os membros em um determinado ministerio
SELECT m.nome, mi.nome
FROM membros m
INNER JOIN ministerio mi ON  mi.id_membro = m.id_membro
WHERE mi.nome ="Ministério de Adoração";
