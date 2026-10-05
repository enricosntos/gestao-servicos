from storage import carregar_dados, salvar_dados 

def criar_clientes(nome, telefone, email):
    dados  = carregar_dados()
    
    clientes = { 
        "id": dados ["proximo_id_clientes"],
        "nome": nome,
        "email": email,
        "telefone": telefone
        }
    dados ["clientes"] .append(clientes)
    dados ["proximo_id_clientes"] += 1 
    salvar_dados(dados)
    return clientes 

def listar_clientes():
    dados = carregar_dados()
    return dados["clientes"]
