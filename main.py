import statistics
import csv
import matplotlib.pyplot as plt
from collections import Counter
from classifier import classificar_mensagem
from validator import safe_classification

# Configurações
TEMPERATURES = [0.0, 0.5, 1.0]

mensagens_cliente = [
    "Quero contratar o plano premium",
    "O sistema está com erro",
    "Quero cancelar minha assinatura",
    "Quero falar com um atendente",
    "Preciso de ajuda com meu pagamento",
    "Gostaria de atualizar minhas informações de conta",
    "Vocês trabalham no sábado"
]

def calcular_estabilidade(distribuicao):
    total = sum(distribuicao.values())
    mais_frequente = distribuicao.most_common(1)[0][1]
    return mais_frequente / total

def run_tests():
    final_report = {}

    for temp in TEMPERATURES:
        print(f"\n===== Testando temperatura {temp} =====")

        categorias = []
        confidences = []
        erros = 0

        for mensagem in mensagens_cliente:
            for i in range(10):
                raw = classificar_mensagem(mensagem, temperature=temp)
                validated = safe_classification(raw)

                print(f"Mensagem: {mensagem} | Execução {i+1}: {validated}")

                categorias.append(validated["categoria"])
                confidences.append(validated.get("confidence", 0))

                if validated["categoria"] == "não_classificado":
                    erros += 1

        distribuicao = Counter(categorias)

        final_report[temp] = {
            "distribuicao": dict(distribuicao),
            "taxa_fallback": erros / (len(mensagens_cliente) * 10),
            "confidence_media": statistics.mean(confidences),
            "confidence_std": statistics.stdev(confidences) if len(confidences) > 1 else 0,
            "estabilidade": calcular_estabilidade(distribuicao)
        }

    return final_report

def export_csv(report):
    with open("resultados.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Temperatura",
            "Fallback %",
            "Confiança Média",
            "Desvio Padrão",
            "Estabilidade"
        ])

        for temp, data in report.items():
            writer.writerow([
                temp,
                data["taxa_fallback"],
                data["confidence_media"],
                data["confidence_std"],
                data["estabilidade"]
            ])

def plot_results(report):
    temps = []
    fallback_rates = []

    for temp, data in report.items():
        temps.append(temp)
        fallback_rates.append(data["taxa_fallback"])

    plt.figure()
    plt.plot(temps, fallback_rates, marker='o')
    plt.xlabel("Temperatura")
    plt.ylabel("Taxa de Fallback")
    plt.title("Impacto da Temperatura na Taxa de Fallback")
    plt.savefig("grafico_fallback.png")
    plt.close()

if __name__ == "__main__":
    report = run_tests()
    export_csv(report)
    plot_results(report)

    print("\n===== RELATÓRIO FINAL =====")
    for temp, data in report.items():
        print(f"Temperatura {temp}: {data}")