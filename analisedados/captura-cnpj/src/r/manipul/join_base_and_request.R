################################################################################
## exemplo:
# > full_join(data1, data2, by = "ID")
################################################################################
## juntarpor uma coluna que nas duas bases tem nomes diferentes
# > dplyr::full_join(x = BASE, y = base, by = c("coluna_x" = "coluna_y"))
################################################################################
# referencias:
# - https://statisticsglobe.com/r-dplyr-join-inner-left-right-full-semi-anti
################################################################################

# SET UP PACKAGES ----
use("dplyr", c("full_join"))

# JUNTAR BASES ----
base_mcti_request <- dplyr::full_join(
  x = base_mcti,
  y = base_request,
  by = "cnpj"
)

view(bbase_mcti_request)