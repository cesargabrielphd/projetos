# DESCRIÇÃO...

# SETUP R NO VSCODE ----
# install.packages("languageserver")
# - https://blog.curso-r.com/posts/2021-11-06-r-no-vscode/

# SETUP PROJECT ----

# Define diretório de trabalho
REMOTE_DIR <- "C:/Users/cesar.oliveira/github/portifolio/projetos/analisedados/captura-cnpj"
setwd(REMOTE_DIR)

# Opções globais
options(
  stringsAsFactors = FALSE,
  repos = c(CRAN = "https://cran.usp.br")
  )

# SETUP PACKAGES ----
# DEFININDO PACOTES ESSENCIAIS DA LINGUAGEM R PARA ANALISE DE DADOS
PACKAGES <- c("dplyr", "ggplot2", "readr")

# Define o caminho da biblioteca customizada
LIBS_R <- file.path(REMOTE_DIR, "config", "pacotesR")
if (!dir.exists(LIBS_R)) {
  dir.create(LIBS_R, recursive = TRUE)
  }

# Adiciona o caminho ao início do vetor de bibliotecas
.libPaths(LIBS_R)


for (pgk in PACKAGES) {
  if (!require(pgk, character.only = TRUE)) {
    install.packages(pgk, lib = LIBS_R, repos = "https://cran-r.c3sl.ufpr.br/")
    library(pgk, character.only = TRUE, lib.loc = LIBS_R)
  } else {
    library(pgk, character.only = TRUE, lib.loc = LIBS_R)
  }
}