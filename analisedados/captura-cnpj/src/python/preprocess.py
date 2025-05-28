# MELHORAR ESTRUTURA E DESENVOLVER ALGUMAS FUNÇÕES
# FUNÇÕES:
#   1. read_cnpj: ler a base e importar os cnpj, sem repetições de cnpj
#   2. is_save: verificar se o cjp já está salvo no arquivo desejado.
#   3. save_lista: salvar dados de cnpjs
#   3. request_cnpj: salvar dados da API do cnpj

import pandas
import os
import requests
import json
import time

def request_cnpj(url, cnpj, savein=None, namefile="cnpjs_request", retries=3, delay=5):
    cnpj_nao_encontrado = []
    url_completa = url + cnpj

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url_completa, timeout=10)
            if response.status_code == 200:
                dados = response.json()
                break
            else:
                print(f"Tentativa {attempt}/{retries}: {cnpj} não encontrado ou erro na requisição.")
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

    if savein:
        os.makedirs(savein, exist_ok=True)
        path = os.path.join(savein, f"{namefile}.json")
        salvar_cnpj_no_json(path, cnpj, dados)

    return data

def salvar_cnpj_no_json(path, cnpj, dados_novo):
    # Se o arquivo existe, carrega o dicionário
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as arquivo:
            try:
                dados = json.load(arquivo)
                if not isinstance(dados, dict):
                    dados = {}
            except json.JSONDecodeError:
                dados = {}
    else:
        dados = {}

    # Só adiciona se o CNPJ não existir
    if cnpj not in dados:
        # Adiciona ao topo: recria o dicionário com o novo CNPJ primeiro
        dados = {cnpj: dados_novo, **dados}
        with open(path, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print(f'CNPJ {cnpj} salvo em {path}.')
    else:
        print(f'CNPJ {cnpj} já existe em {path}.')


def read_cnpj(caminho: str = None, namecol: str = None):
    namecol = namecol.lower().strip()
    base = pandas.read_excel(caminho, dtype=str)
    for col in base.columns:
        if col.strip().lower() == namecol:
            return base[col].astype(str).str.zfill(14).tolist()
    raise ValueError(f"Coluna '{namecol}' não encontrada no arquivo.")

if __name__ == "__main__":
  # LISTA DE CNPJs
  BASE_CAMINHO = "./data/processed/base_cnpjs.xlsx"
  LISTA_CNPJ = read_cnpj(caminho=BASE_CAMINHO, namecol="CNPJ Dispêndio")

  # SETUP ....
  URL = "https://minhareceita.org/"
  SAVE_DADOS_IN = "./data/processed/"


    # SALVAR INFORMAÇÕES DOS CNPJs
    # Para evitar sobrecarregar a API, processaremos 5 CNPJs por vez com um intervalo de 4 minutos entre os lotes.
  total = len(LISTA_CNPJ)
  for idx, cnpj in enumerate(LISTA_CNPJ, start=1):
      try:
          request_cnpj(url=URL, cnpj=cnpj, savein=SAVE_DADOS_IN,
                      namefile="cnpjs_request")
          print(f"Processado {idx} de {total}.")
      except Exception as e:
          print(f"Erro ao processar o CNPJ {cnpj}: {e}")
      if idx % 50 == 0:
        print("Aguardando 15 seg para evitar sobrecarga na API (processados 5 CNPJs).")
        time.sleep(15)
  print("Fim")