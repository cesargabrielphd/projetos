# install.packages("tidyverse")

library(tidyverse)
base <- read_csv(
  file = "C:/Users/cesar.oliveira/github/projetos/analisedados/captura-cnpj/data/processed/cnpjs_data.csv",
  sep = ";",
  col_types = list(col_character())
)