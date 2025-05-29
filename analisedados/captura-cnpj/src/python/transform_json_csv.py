import pandas as pd

# Ler o JSON da base de dados
BASE = pd.read_json("./data/processed/cnpjs_request.json")

# Transformar JSON em lista de dicionários para o DataFrame
rows = []
for cnpj, info in BASE.items():
    row = {
        "CNPJ": cnpj,
        "UF": info.get("uf"),
        "CEP": info.get("cep"),
        "Logradouro": info.get("logradouro"),
        "Número": info.get("numero"),
        "Bairro": info.get("bairro"),
        "Município": info.get("municipio"),
        "Porte": info.get("porte"),
        "Razão Social": info.get("razao_social"),
        "Nome Fantasia": info.get("nome_fantasia"),
        "Capital Social": info.get("capital_social"),
        "DDD Telefone 1": info.get("ddd_telefone_1"),
        "DDD Telefone 2": info.get("ddd_telefone_2"),
        "DDD Fax": info.get("ddd_fax"),
        "Complemento": info.get("complemento"),
        "CNAE Fiscal": info.get("cnae_fiscal"),
        "CNAE Fiscal Descrição": info.get("cnae_fiscal_descricao"),
        "CNAEs Secundários": "; ".join(
            [f"{cnae.get('codigo', '')} - {cnae.get('descricao', '')}"
             for cnae in info.get("cnaes_secundarios", [])]
        ),
        "Natureza Jurídica": info.get("natureza_juridica"),
        "Regime Tributário": info.get("regime_tributario"),
        "Situação Especial": info.get("situacao_especial"),
        "Opção pelo Simples": info.get("opcao_pelo_simples"),
        "Opção pelo MEI": info.get("opcao_pelo_mei"),
        "Situação Cadastral": info.get("situacao_cadastral"),
        "Data Início Atividade": info.get("data_inicio_atividade"),
        "Data Situação Cadastral": info.get("data_situacao_cadastral"),
        "Data Opção pelo Simples": info.get("data_opcao_pelo_simples"),
        "Data Exclusão do Simples": info.get("data_exclusao_do_simples"),
        "Data Situação Especial": info.get("data_situacao_especial"),
        "Código Município IBGE": info.get("codigo_municipio_ibge"),
        "Código Município": info.get("codigo_municipio"),
        "Código Natureza Jurídica": info.get("codigo_natureza_juridica"),
        "Código Porte": info.get("codigo_porte"),
        "Motivo Situação Cadastral": info.get("motivo_situacao_cadastral"),
        "Descrição Situação Cadastral": info.get("descricao_situacao_cadastral"),
        "Descrição Tipo de Logradouro": info.get("descricao_tipo_de_logradouro"),
        "Descrição Motivo Situação Cadastral": info.get("descricao_motivo_situacao_cadastral"),
        "Descrição Identificador Matriz/Filial": info.get("descricao_identificador_matriz_filial"),
        "Identificador Matriz/Filial": info.get("identificador_matriz_filial"),
        "Qualificação do Responsável": info.get("qualificacao_do_responsavel"),
        "Ente Federativo Responsável": info.get("ente_federativo_responsavel"),
        "Nome Cidade no Exterior": info.get("nome_cidade_no_exterior"),
        "QSA": "; ".join(
            [f"{socio.get('nome_socio', '')} ({socio.get('qualificacao_socio', '')}, {socio.get('faixa_etaria', '')})"
             for socio in info.get("qsa", [])]
        )
    }
    rows.append(row)

# Criar DataFrame
df = pd.DataFrame(rows)

# Salvar em CSV
df.to_csv("./data/processed/cnpjs_request.csv", index=False, sep="|")

print("Arquivo CSV gerado com sucesso!")
