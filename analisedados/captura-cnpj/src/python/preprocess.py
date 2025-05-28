import pandas
import os
import requests
import json
import time

def request_cnpj(url, cnpj, savein=None, namefile="cnpjs_request"):
    cnpj_nao_encontrado = []
    url_completa = url + cnpj
    response = requests.get(url_completa)
    if response.status_code == 200:
        dados = response.json()
    else:
      cnpj_nao_encontrado = cnpj_nao_encontrado.append(cnpj)
      print(f"{cnpj} não encontrado ou erro na requisição.")
      return f"Lista de CNPJs NÃO ENCONTRADOS", cnpj_nao_encontrado

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
      request_cnpj(url=URL, cnpj=cnpj, savein=SAVE_DADOS_IN,
                  namefile="cnpjs_request")
      print(f"Processado {idx} de {total}.")
    #   if idx % 10 == 0:
    #       print("Aguardando 1 minuto para evitar sobrecarga na API (processados 5 CNPJs).")
    #       time.sleep(60)

  print("Fim")