# MELHORAR ESTRUTURA E DESENVOLVER ALGUMAS FUNÇÕES
# FUNÇÕES:
#   1. read_cnpj: ler a base e importar os cnpj, sem repetições de cnpj
#   2. cnpj_save: verificar se o cjp já está salvo no arquivo desejado.
#   3. save_lista: salvar dados de cnpjs
#   3. request_cnpj: salvar dados da API do cnpj

import pandas
import os
import requests
import json
import time


def read_cnpj(caminho: str = None, namecol: str = None, repetir:bool=False):
  #   1. read_cnpj: ler a base e importar os cnpj, sem repetições de cnpj
    namecol = namecol.lower().strip()
    base = pandas.read_excel(caminho, dtype=str)
    for col in base.columns:
        if col.strip().lower() == namecol:
            return base[col].astype(str).str.zfill(14).tolist()
    raise ValueError(f"Coluna '{namecol}' não encontrada no arquivo.")

def is_save(cnpj: int, lista: list):
    #   2. is_save: verificar se o cjp já está salvo no arquivo desejado.
    if cnpj in lista:
      return True
    else:
      return False

def request_cnpj(url, cnpj, savein=None, retries=3, delay=5):
    cnpj_nao_encontrado = []
    url_completa = url + cnpj

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url_completa, timeout=10)
            if response.status_code == 200:
                dados = response.json()
                break
            else:
                print(
                    f"Tentativa {attempt}/{retries}: {cnpj} não encontrado ou erro na requisição.")
                if attempt == retries:
                    cnpj_nao_encontrado.append(cnpj)
                    return f"Lista de CNPJs NÃO ENCONTRADOS", cnpj_nao_encontrado
        except requests.exceptions.RequestException as e:
            print(f"Tentativa {attempt}/{retries} falhou: {e}")
            if attempt == retries:
                cnpj_nao_encontrado.append(cnpj)
                return f"Lista de CNPJs NÃO ENCONTRADOS", cnpj_nao_encontrado
        time.sleep(delay)  # Aguarda antes de tentar novamente

    data = {
        cnpj: dados
    }
    return data

def save_lista(save_in: str = None, dados: list = None, namefile="cnpjs_request"):
    if not save_in or not dados:
        raise ValueError("Os parâmetros 'save_in' e 'dados' são obrigatórios.")

    os.makedirs(save_in, exist_ok=True)
    path = os.path.join(save_in, f"{namefile}.json")

    # Carregar dados existentes, se o arquivo já existir
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as arquivo:
            try:
                dados_existentes = json.load(arquivo)
                if not isinstance(dados_existentes, dict):
                    dados_existentes = {}
            except json.JSONDecodeError:
                dados_existentes = {}
    else:
        dados_existentes = {}

    # Atualizar os dados existentes com os novos
    for cnpj, info in dados.items():
        if cnpj not in dados_existentes:
            dados_existentes[cnpj] = info

    # Salvar os dados atualizados no arquivo
    with open(path, "w", encoding="utf-8") as arquivo:
        json.dump(dados_existentes, arquivo, ensure_ascii=False, indent=4)
    print(f"Dados salvos em {path}.")

if __name__ == "__main__":
    # LISTA DE CNPJs
    BASE_CAMINHO = "./data/processed/base_cnpjs.xlsx"
    COLUNA_CNPJ = "CNPJ Dispêndio"
    LISTA_CNPJ = read_cnpj(caminho=BASE_CAMINHO, namecol=COLUNA_CNPJ)
    print(f"Total de CNPJs carregados: {len(LISTA_CNPJ)}")

    # SETUP API
    URL = "https://minhareceita.org/"
    SAVE_DADOS_IN = "./data/processed/"
    NAMEFILE = "cnpjs_request"

    # Verificar e salvar dados
    cnpjs_salvos = {}
    for cnpj in LISTA_CNPJ:
        if not is_save(cnpj, cnpjs_salvos):
            print(f"Requisitando dados para o CNPJ: {cnpj}")
            dados = request_cnpj(URL, cnpj)
            if isinstance(dados, dict):  # Verifica se a resposta é válida
                cnpjs_salvos.update(dados)
            else:
                print(f"Erro ao requisitar dados para o CNPJ: {cnpj}")

    # Salvar os dados coletados
    save_lista(save_in=SAVE_DADOS_IN, dados=cnpjs_salvos, namefile=NAMEFILE)
    print("Processo concluído.")
