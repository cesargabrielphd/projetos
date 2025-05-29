import json

with open("./data/processed/cnpjs_request.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Exibe as chaves principais do JSON
print("Chaves principais:", data.keys())

# Exemplo de inspeção detalhada
for cnpj, info in data.items():
    print(f"CNPJ: {cnpj}")
    print("Informações:", info)
    break  # Remove este 'break' para exibir todas as entradas

# DADOS
# Estado(UF): uf
# Classificação e Porte:
#   - Porte da Empresa: porte
#   - Capital Social: capital_social

# Atividade Econômica:
# - CNAE Fiscal: cnae_fiscal
# - Descrição do CNAE Fiscal: cnae_fiscal_descricao

# informações Adicionais:
# - Natureza Jurídica: natureza_juridica
# - Data de Início de Atividade: data_inicio_atividade

# cnpj ; uf ; porte; capital_social; cnae_fiscal ; cnae_fiscal_descricao ; natureza_juridica ; data_inicio_atividade