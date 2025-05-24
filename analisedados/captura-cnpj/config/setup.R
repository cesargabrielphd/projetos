# DESCRIÇÃO ----

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


# SETUP R NO VSCODE ----
# install.packages("languageserver")
# - https://blog.curso-r.com/posts/2021-11-06-r-no-vscode/

# SETUP PROJECT ----
options(
  stringsAsFactors = FALSE,
  repos = c(CRAN = "https://vps.fmvz.usp.br/CRAN/")
  )

# SETUP DIRETÓRIOS ----
# definindo diretório local
REMOTE_DIR <- "C:/Users/cesar.oliveira/github/portifolio/projetos/analisedados/captura-cnpj"
LOCAL_DIR <- "C:/Users/cesargabriel/github/portifolio/projetos/analisedados/captura-cnpj"

# Definindo o diretório de trabalho
setwd(LOCAL_DIR)
# setwd(REMOTE_DIR)
getwd()

# SETUP RENV ----
if(!require(renv)) install.packages("renv")
library(renv)

# iniciando e atiavando o RENV
Sys.setenv(
  RENV_PATHS_ROOT = file.path(LOCAL_DIR, "renv")
)

# renv::init(bare = TRUE)
# renv::activate()

# renv::deactivate()


# SETUP PACKAGES ----
# instalando pacotes

# .libPaths()

# DEFININDO PACOTES ESSENCIAIS DA LINGUAGEM R PARA ANALISE DE DADOS
PACKAGES <- c("dplyr", "ggplot2", "readr","readxl", "fs", "janitor", "renv", "purrr")

# instalando os pacotes
for (pgk in PACKAGES) {
  if (!require(pgk, character.only = TRUE, quietly = TRUE)) {
    install.packages(pgk)
    library(pgk, character.only = TRUE)
  } else {
    library(pgk, character.only = TRUE)
  }
}

# SETUP PACKAGES ----
# Carregando pacotes necessários
# use("writexl", c("write_xlsx"))
# use("janitor", c("clean_names"))
# use("dplyr", c("mutate", "case_when", "filter", "select"))
# use("ggplot2", c("ggplot", "aes", "geom_bar", "labs"))
# use("readr", c("read_csv"))
# use("readxl", c("read_xlsx"))
# use("fs", c("dir_create"))
# use("purrr", c("map"))

