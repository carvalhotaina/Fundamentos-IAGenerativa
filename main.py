from llm_client import LLMClient
from retriever import load_conhecimento, simple_retriever
from validator import validate_json
from prompt import build_system_prompt

def main():
    provider = input("Escolha o provedor (openai/groq): ").strip().lower()
    client = LLMClient(provider=provider)
    conhecimento = load_conhecimento()

    print("\n--- Sistema de Atendimento Seguro Iniciado ---")

    while True:
        query = input("\nDigite sua pergunta (ou 'sair' para encerrar): ").strip()
        if query.lower() == "sair":
            break
        
        # 🛡️ PROTEÇÃO CONTRA PROMPT INJECTION (O Firewall)
        palavras_proibidas = ["system prompt", "ignore", "esqueça", "instruções", "regras", "desconsidere"]
        if any(palavra in query.lower() for palavra in palavras_proibidas):
            print("❌ ERRO DE SEGURANÇA: Tentativa de manipulação de prompt detectada. Acesso bloqueado.")
            continue # Interrompe aqui e não deixa a IA ver a mensagem
        
        # Se passou pelo firewall, continua o fluxo normal
        contexto = simple_retriever(query, conhecimento)
        system_prompt = build_system_prompt()

        response_text = client.generate_text(system_prompt, contexto)

        try:
            is_valid, data = validate_json(response_text)
            if is_valid:
                print(f"✅ Resposta: {data['resposta']}")
        except ValueError as e:
            print(f"⚠️ Erro de validação: {e}")

if __name__ == "__main__":
    main()