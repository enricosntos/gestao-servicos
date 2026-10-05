import json
from pathlib import Path

DATA_FILE = Path("data/dados.json")

def carregar_dados():
    if not DATA_FILE.exists():
        return {"clientes": [], "servicos": [],
                "proximo_id_clientes": 1, "proximo_id_servico": 1}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)