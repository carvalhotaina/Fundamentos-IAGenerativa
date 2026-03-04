import json; import re;
def validate_json(text):
    try:
        text_cleaned = re.sub(r"```json|```", "", text).strip()
        data = json.loads(text_cleaned, strict=False)
        if isinstance(data, dict) and "resposta" in data:
            return True, data
        return False, "O JSON nao contem a chave resposta."
    except Exception as e:
        raise ValueError(f"Erro ao decodificar JSON: {e}")
