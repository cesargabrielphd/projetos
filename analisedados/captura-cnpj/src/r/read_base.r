# SETUP IMPORT BASE ----
use("readxl")

BASE <- readxl::read_xlsx("./data/processed/base_cnpjs.xlsx", sheet="Export")

# verificar se Há algum NA nas colunas desejadas

# # LIMPNDO OS NOMES COM JANITOR
BASE <-
BASE  |>
janitor::clean_names()

print(x=BASE, n=10)
# # [34] "universidades"
# # [35] "instituicoes_de_pesquisa"
# # [36] "inventor_independente_contratado"
# # [37] "relacao_dos_servicos_de_terceiros_contratados"
# # [38] "micro_empresas"
# # [39] "empresas_de_pequeno_porte"
# # [40] "inventor_independente_valores_transferidos"

CONDICAO_BASE <-
BASE  |>
  dplyr::mutate(
    univer_condicao = dplyr::case_when(
      # Por hipotese, pode ter menos empresas com condição
      universidades == 0 ~ "sim",
      TRUE ~ "nao"
    ),
    instipesq_condicao = dplyr::case_when(
      instituicoes_de_pesquisa == 0 ~ "sim",
      TRUE ~ "nao"
    )
  )  |>
  dplyr::filter(
    univer_condicao == "sim" |
    instipesq_condicao == "sim"
  )  |>
  dplyr::select(
    cnpj,
    universidades,
    instituicoes_de_pesquisa
  )


# SALVANDO BASE DE DADOS COM OS CNPJS QUE ATENDEM AS CONDIÇÕES
writexl::write_xlsx(CONDICAO_BASE, "data/processed/CONDICAO_BASE.xlsx")
