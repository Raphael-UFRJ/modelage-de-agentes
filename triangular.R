if (!requireNamespace("triangle", quietly = TRUE)) {
  install.packages("triangle")
}

library(triangle)

# Definir parâmetros da distribuição triangular
min_val <- 0.1
max_val <- 10.8
mode <- 10.8
initial_size <- 10

# Função para gerar números aleatórios usando rtriangle
random_triangular_r <- function(initial_size, min_val, max_val, mode) {
  rtriangle(initial_size, min_val, max_val, mode)
}

# Gerar números aleatórios usando rtriangle
random_numbers_r <- random_triangular_r(initial_size, min_val, max_val, mode)

# Exibir os resultados de R
cat("R Triangular:", random_numbers_r, "\n")
