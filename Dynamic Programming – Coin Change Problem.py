
def main():
  # C = I, N = J
  n,c = input().strip().split()
  n = int(n)
  c = int(c)
  coins = [int(x) for x in input().strip().split()]
  matrix = [[0 for i in range(n+1)] for j in range(c+1)] # se llena al revés columnas filas

  # I == Cantidad de denominacion de monedas disponible
  # j == Total al que se quiere llegar
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if (j ==0):
        matrix[i][j] = 1 
      elif (i==0 and j>0):
        matrix[i][j] = 0
      elif (coins[i-1] <= j):
        matrix[i][j] = matrix[i][j-coins[i-1]] + matrix[i-1][j] # Se decide entre tomar o no la denominacion
      else:
        matrix[i][j] = matrix[i-1][j] # No se utiliza la denominación si es mayor
  print (matrix[c][n])
main()
