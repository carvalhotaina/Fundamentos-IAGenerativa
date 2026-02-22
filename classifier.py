from llm_client import gerar_resposta

# Categorias corretas 
CATEGORIAS = ["Suporte", "Vendas", "Financeiro", "Geral"]

def classificar_mensagem(texto, temperature=0.0):
    prompt = f"""
Classifique a mensagem abaixo em uma das seguintes categorias: {', '.join(CATEGORIAS)}.
Retorne apenas um JSON no formato:
{{"categoria":"nome_categoria"}}

Mensagem:
{texto}
"""
    return gerar_resposta(prompt, temperature)