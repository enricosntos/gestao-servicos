from storage import carregar_dados, salvar_dados


def criar_cliente(nome, telefone, email):
    dados = carregar_dados()

    cliente = {
        "id": dados["proximo_id_cliente"],
        "nome": nome,
        "telefone": telefone,
        "email": email,
    }

    dados["clientes"].append(cliente)
    dados["proximo_id_cliente"] += 1
    salvar_dados(dados)
    return cliente


def listar_clientes():
    dados = carregar_dados()
    return dados["clientes"]


def buscar_cliente(id_cliente):
    dados = carregar_dados()

    for cliente in dados["clientes"]:
        if cliente["id"] == id_cliente:
            return cliente

    return None


def deletar_cliente(id_cliente):
    dados = carregar_dados()

    for cliente in dados["clientes"]:
        if cliente["id"] == id_cliente:
            dados["clientes"].remove(cliente)
            salvar_dados(dados)
            return True

    return False