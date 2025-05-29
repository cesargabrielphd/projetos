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


def read_cnpj(caminho: str = None, namecol: str = None):
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

def save_lista(save_in: str = None, dados: list = None, namefile="cnpjs_request", ):
    if save_in:
        os.makedirs(save_in, exist_ok=True)
        path = os.path.join(save_in, f"{namefile}.json")
        # salvar dados

    return ...

if __name__ == "__main__":
  # LISTA DE CNPJs
  BASE_CAMINHO = "./data/processed/base_cnpjs.xlsx"
  LISTA_CNPJ = read_cnpj(caminho=BASE_CAMINHO, namecol="CNPJ Dispêndio")

  # SETUP ....
  URL = "https://minhareceita.org/"
  SAVE_DADOS_IN = "./data/processed/"
