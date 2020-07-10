#HackerRank longest common subsequence Dynamic Programming top down solution

n,m = [int(i) for i in input().strip().split()]
a = [int(x) for x in input().strip().split()]
b = [int(y) for y in input().strip().split()]
'''
Recursive solution
def longestCommon(n,m):
    if (n<0 or m<0):
        return []
    
    elif (a[n] == b[m]):
        return  longestCommon(n-1,m-1) + [a[n]]
    else: 
        if len(longestCommon(n-1,m)) > len(longestCommon(n,m-1)):
            return (longestCommon(n-1,m))
        else:
            return (longestCommon(n,m-1))
    
        
'''
def main():
    # Memoization
    solution = [[' ' for i in range (m+1)]for j in range (n+1)]
    for i in range(len(solution)):
        for j in range(len(solution[i])):
            if (i==0 or j==0):
                solution[i][j] = ' '
            elif (a[i-1] == b[j-1]):
                solution[i][j] =  solution[i-1][j-1] + str(a[i-1])+ " "
            else:
                if len(solution[i-1][j]) > len(solution[i][j-1]):
                    solution[i][j] = solution[i-1][j]
                else:
                    solution[i][j] = solution[i][j-1]
    print (solution[n][m][1:])
                
    
    
main()
