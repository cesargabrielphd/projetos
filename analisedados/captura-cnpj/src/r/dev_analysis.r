# Analisar os dados de cnpjs que indicam que houve parcerias com:
# ANALISE CNPJs DESEJADOS
# filtrar CNPJs que tem indicios de desenvolvimento de projetos de P,D&I com:
# - Universidades Publicas e ICT
# variaveis da Base:
# - [34] "Universidades"
# - [35] "Instituições de Pesquisa"
# - [36] "Inventor Independente Contratado"
# - [37] "Relação dos Serviços de Terceiros - Contratados"
# - [38] "MicroEmpresas"
# - [39] "Empresas de Pequeno Porte"
# - [40] "Inventor Independente Valores Transferidos"
# CAMINHO DA BASE NA REDE DO MCTI (movido para `/data/raw/`)
# - "P:\CGIA\OSTENSIVO\CGIT\03_COIAI\Lei do Bem\APRESENTACOES\EVENTOS\SLIDES_GRAFICOS_BRASIL\Base AB 2023.xlsx"

# SETUP LIBRARY R 4.5 ----
# use(pacote, c(fun1,fun2))


# SETUP IMPORT BASES ----
# install.packages("writexl")
# install.packages("janitor")
# install.packages(c("dplyr", "ggplot2", "readr"), repos = "https://cran-r.c3sl.ufpr.br/")
# install.packages("tidyverse", repos = "https://cran-r.c3sl.ufpr.br/")
library(package="dplyr")
library(package="ggplot2")
library(package="readr")
library(package="readxl")
library(package="janitor")

# SETUP IMPORT BASE ----

BASE <- readxl::read_xlsx("data/raw/Base AB 2023.xlsx", sheet="Export")

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
