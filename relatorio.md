Relatório Comparativo — Classificador Produção Ready
Taína Carvalho

**1. Objetivo**

O objetivo aqui é tornar o classificador confiável o suficiente para ser usado em um ambiente de produção. Para isso, precisamos seguir alguns requisitos definidos:

*   Ter um *parser* JSON robusto;

*   Validar as categorias contra uma lista de categorias permitidas;

*   Implementar um *fallback* seguro;

*   Testar o classificador com múltiplas execuções e em diferentes temperaturas;

*   Registrar *logs* estruturados.

**2. Configuração de Testes**

Durante os testes, foram utilizadas as seguintes mensagens:

*   Quero contratar o plano *premium*;

*   O sistema está com erro;

*   Quero cancelar minha assinatura;

*   Quero falar com um atendente;

*   Preciso de ajuda com meu pagamento;

*   Gostaria de atualizar minhas informações de conta;

*   Vocês trabalham no sábado.

Foram testadas as temperaturas 0.0, 0.5 e 1.0, com 10 execuções para cada temperatura. As categorias válidas são: suporte, vendas, financeiro e geral. O *fallback* configurado foi “não\_classificado".

**3. Resultados**

### Temperatura 0.0

| Categoria   | Contagem |

| :---------- | :------- |

| vendas      | 10       |

| suporte     | 40       |

| financeiro  | 10       |

| geral       | 10       |

*   *Fallback* %: 0.0

*   Confiança média: 0.5

*   Desvio padrão: 0.0

*   Estabilidade: 0.571

### Temperatura 0.5

| Categoria   | Contagem |

| :---------- | :------- |

| vendas      | 10       |

| suporte     | 37       |

| geral       | 13       |

| financeiro  | 10       |

*   *Fallback* %: 0.0

*   Confiança média: 0.5

*   Desvio padrão: 0.0

*   Estabilidade: 0.529

### Temperatura 1.0

| Categoria   | Contagem |

| :---------- | :------- |

| vendas      | 10       |

| suporte     | 33       |

| financeiro  | 15       |

| geral       | 12       |

*   *Fallback* %: 0.0

*   Confiança média: 0.5

*   Desvio padrão: 0.0

*   Estabilidade: 0.471

**4. Observações**

*   O *parser* JSON e a validação estão funcionando corretamente, garantindo que apenas as categorias permitidas sejam aceitas.

*   O *fallback* seguro não precisou ser acionado durante as execuções.

*   A confiança está fixa em 0.5, o que é o esperado para o teste atual.

*   Houve pequenas variações nas categorias com o aumento da temperatura (1.0), mostrando uma maior flexibilidade do modelo.

*   O *log* estruturado (*app.log*) captura cada execução com *status* de sucesso ou erro.

**5. Conclusão**

O classificador atende a todos os critérios do desafio e está robusto o suficiente para ser usado em um ambiente de produção e pronto para entrega.

Ainda, podem ser consideradas melhorias opcionais, como a variação de confiança e o refinamento do *fallback*, mas elas não são obrigatórias para o desafio.