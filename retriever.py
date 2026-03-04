def load_conhecimento():
    # Ajuste o caminho do arquivo se necessário
    with open("conhecimento/conhecimento.txt", "r", encoding="utf-8") as f:
        return f.read()

def simple_retriever(query, conhecimento):
    # Quebra o texto da empresa em blocos menores
    sections = conhecimento.split("\n\n")
    
    # Limpa a pergunta e separa as palavras
    palavras_pergunta = set(query.lower().split())
    
    melhor_trecho = ""
    maior_pontuacao = 0
    
    # Simulação de Busca por Similaridade (Overlapping)
    for section in sections:
        if not section.strip():
            continue
            
        palavras_secao = set(section.lower().split())
        
        # Conta quantas palavras da pergunta existem neste bloco
        pontuacao = len(palavras_pergunta.intersection(palavras_secao))
        
        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_trecho = section
            
    if maior_pontuacao > 0:
        print(f"\n🔍 [RAG Simulado] Trecho recuperado: {melhor_trecho[:80]}...")
        return melhor_trecho
    else:
        return "Desculpe, não encontrei informações relevantes."
