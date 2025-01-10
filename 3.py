# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
# na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open("./dados.json") as f:
    faturamento = json.load(f)

valor_faturamento = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

menor_faturamento = min(valor_faturamento)
maior_faturamento = max(valor_faturamento)

media_faturamento = sum(valor_faturamento) / len(valor_faturamento)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(
    f"A media de faturamento é de {media_faturamento} e o número de dias com faturamento superior à média: {len([dia for dia in valor_faturamento if dia > media_faturamento])}"
)
