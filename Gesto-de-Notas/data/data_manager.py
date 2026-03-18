import json
from pathlib import Path

CAMINHO = Path(__file__).parent / "data.json"

def carregar_dados():
    if not CAMINHO.exists():
        return {"escola":[], "faculdade":[]}
    with CAMINHO.open("r", encoding="utf-8") as f:
        return json.load(f)



def salvar_dados(dados):
    CAMINHO.parent.mkdir(parents=True, exist_ok=True)
    with CAMINHO.open("w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)