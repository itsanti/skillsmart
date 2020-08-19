# https://skillsmart.ru/algo/lvl1/d83i.html

# void MatrixTurn(string Matrix[], int M, int N, int T)


def MatrixTurn(Matrix, M, N, T):
    mat = [list(row) for row in Matrix]
    for t in range(T):
        turn(mat)
    for r in range(M):
        Matrix[r] = ''.join(mat[r])
    return None


def turn(mat):
    top = 0
    bottom = len(mat)-1
    left = 0
    right = len(mat[0])-1
  
    while left < right and top < bottom: 
        prev = mat[top+1][left] 

        for i in range(left, right+1): 
            curr = mat[top][i] 
            mat[top][i] = prev 
            prev = curr 
  
        top += 1
  
        for i in range(top, bottom+1): 
            curr = mat[i][right] 
            mat[i][right] = prev 
            prev = curr 
  
        right -= 1

        for i in range(right, left-1, -1): 
            curr = mat[bottom][i] 
            mat[bottom][i] = prev 
            prev = curr 
  
        bottom -= 1
  
        for i in range(bottom, top-1, -1): 
            curr = mat[i][left] 
            mat[i][left] = prev 
            prev = curr 
  
        left += 1
