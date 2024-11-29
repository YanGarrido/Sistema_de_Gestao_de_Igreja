def validate_login_data(data):
    # Verifica se os campos estão presentes
    if (not isinstance(data["usuario"], str) or not data["usuario"].strip()) and (not isinstance(data["senha"], str) or not data["senha"].strip()):
        return False, "Os campos 'Email' e 'Senha' são obrigatórios."

    # Verifica se o username é uma string não vazia
    if not isinstance(data["usuario"], str) or not data["usuario"].strip():
        return False, "O campo 'Email' não pode estar vazio."

    # Verifica se a senha atende a um critério básico (ex: pelo menos 6 caracteres)
    if not isinstance(data["senha"], str) or len(data["senha"]) < 6:
        return False, "O campo 'Senha' deve ter pelo menos 6 caracteres."

    # Se todas as verificações passarem, retorna True
    return True, ""