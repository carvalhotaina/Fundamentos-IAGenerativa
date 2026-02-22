import json
import logging
from typing import Dict, Any

# Categorias permitidas
ALLOWED_CATEGORIES = [
    "suporte",
    "vendas",
    "financeiro",
    "geral"
]

FALLBACK_CATEGORY = "não_classificado"

# Configuração de log estruturado
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(message)s"
)

def log_event(event: dict):
    logging.info(json.dumps(event, ensure_ascii=False))


#  Parser JSON
def parse_json_response(response: str) -> Dict[str, Any]:
    try:
        return json.loads(response)
    except json.JSONDecodeError as e:
        log_event({
            "status": "erro",
            "tipo": "json_invalido",
            "mensagem": str(e)
        })
        raise


#  Normalização
def normalize_category(category: str) -> str:
    return category.strip().lower()


# Validação contra lista permitida
def validate_allowed_category(category: str) -> bool:
    return category in ALLOWED_CATEGORIES


# Fallback seguro
def fallback_response(error_type: str) -> Dict[str, Any]:
    result = {
        "categoria": FALLBACK_CATEGORY,
        "confidence": 0.0,
        "erro": error_type
    }

    log_event(result)
    return result


# Pipeline completo
def safe_classification(response: str) -> Dict[str, Any]:

    try:
        parsed = parse_json_response(response)

        category = parsed.get("categoria")
        confidence = parsed.get("confidence", 0.5)

        if not category:
            return fallback_response("categoria_ausente")

        category = normalize_category(category)

        if not validate_allowed_category(category):
            return fallback_response("categoria_invalida")

        result = {
            "categoria": category,
            "confidence": confidence
        }

        log_event({
            "status": "sucesso",
            "categoria": category,
            "confidence": confidence
        })

        return result

    except json.JSONDecodeError:
        return fallback_response("json_invalido")

    except Exception as e:
        log_event({
            "status": "erro",
            "tipo": "erro_inesperado",
            "mensagem": str(e)
        })
        return fallback_response("erro_inesperado")