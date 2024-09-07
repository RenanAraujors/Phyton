import json


dados_faturamento = '''
{
    "faturamento": [1000, 2000, 0, 1500, 0, 0, 3000, 2500, 5000, 4000]
}
'''

dados = json.loads(dados_faturamento)
faturamento_diario = [valor for valor in dados['faturamento'] if valor > 0]

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Contagem de dias acima da média
dias_acima_da_media = len([dia for dia in faturamento_diario if dia > media_mensal])

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
