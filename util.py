import re

def extrair_uf(texto):
    match = re.search(r'\b([A-Z]{2})\b', texto.upper())
    return match.group(1) if match else None
