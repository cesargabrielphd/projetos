################################################################################
## exemplo:
# > full_join(data1, data2, by = "ID")
################################################################################
## juntarpor uma coluna que nas duas bases tem nomes diferentes
# > dplyr::full_join(x = BASE, y = base, by = c("coluna_x" = "coluna_y"))
################################################################################
# referencias:
# - https://www.youtube.com/watch?v=xnUo25VRH70
# - https://statisticsglobe.com/r-dplyr-join-inner-left-right-full-semi-anti
################################################################################

# SET UP PACKAGES ----
use("dplyr", c("full_join"))

# CARREGAR BASES ----
source("src/r/read/read_base_mcti.R")
source("src/r/read/read_request.R")

# JUNTAR BASES ----
base_mcti_request <- dplyr::full_join(
  x = base_mcti,
  y = base_request,
  by = "cnpj"
)

# SALVANDO BASE COMPLETA ----
write.csv(
  x = base_mcti_request,
  file = "data/processed/base_mcti_request.csv",
  row.names = FALSE
)
