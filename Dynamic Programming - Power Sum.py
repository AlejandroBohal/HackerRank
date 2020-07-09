dictBottomUp = {}
def powerSum(num,X,N):
  if ((num,X) not in dictBottomUp.keys()):
    if (num**N < X):
      dictBottomUp[(num,X)] = powerSum(num+1,X,N) + powerSum(num+1,X-num**N,N)
      return dictBottomUp[(num,X)]
    elif(num**N == X):
      dictBottomUp[(num,X)] = 1
      return 1
    else:
      dictBottomUp[(num,X)] = 0
      return 0
  else:
    return dictBottomUp[(num,X)]

def main():
  X = int(input())
  N = int(input())
  print(powerSum(1,X,N))
  

main()
