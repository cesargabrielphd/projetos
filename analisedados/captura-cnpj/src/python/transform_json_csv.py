import json
import pandas as pd

# Carrega o arquivo JSON
with open("./data/processed/cnpjs_request.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Cria uma lista para armazenar os dados formatados
rows = []

# Itera sobre os CNPJs e extrai as informações relevantes
for cnpj, info in data.items():
    rows.append({
        "CNPJ": cnpj,
        "UF": info.get("uf"),
        "Porte": info.get("porte"),
        "Capital Social": info.get("capital_social"),
        "CNAE Fiscal": info.get("cnae_fiscal"),
        "Descrição CNAE Fiscal": info.get("cnae_fiscal_descricao"),
        "Natureza Jurídica": info.get("natureza_juridica"),
        "Data Início Atividade": info.get("data_inicio_atividade"),
    })

# Cria o DataFrame
df = pd.DataFrame(rows)

# Exibe o DataFrame
print(df)

# Salva o DataFrame em um arquivo CSV (opcional)
df.to_csv("./data/processed/cnpjs_data.csv", index=False, encoding="utf-8")