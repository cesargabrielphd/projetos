# SETUP IMPORT BASE ----
library(readxl)

BASE <-
  readxl::read_xlsx(
    path = "C:/Users/cesar.oliveira/github/projetos/analisedados/captura-cnpj/data/processed/base_cnpjs.xlsx",
    sheet = "Export",
    col_types = "text"
  )

# verificar se Há algum NA nas colunas desejadas

# # LIMPNDO OS NOMES COM JANITOR
BASE <-
  BASE |>
  janitor::clean_names()

#  [1] "ano_base"                        "cnpj"
#  [3] "razao_social"                    "codigo_atividade_economica_ibge"
#  [5] "uf"                              "numero_projeto"
#  [7] "projeto"                         "setor"
#  [9] "tipo_dispendio"                  "cnpj_dispendio"
# [11] "razao_social_dispendio"          "servico"
# [13] "valor"
