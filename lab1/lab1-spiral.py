def matricespirala(mat, i, j, m, n):
    if(i>=m or j>=n):
        return;
    
    for x in range(i, n):
        print(mat[i][x], end='')
    for x in range(i+1, m):
        print(mat[x][n-1],  end='')

    if ((m - 1) != i):
        for x in range(n - 2, j - 1, -1):
            print(mat[m - 1][x],  end='')
    if ((n - 1) != j):
        for x in range(m - 2, i, -1):
            print(mat[x][j],  end='')
 
    matricespirala(mat, i + 1, j + 1, m - 1, n - 1)

mat = [['f', 'i', 'r', 's'],
        ['n', '_', 'l', 't'],
        ['o', 'b', 'a', '_'],
        ['h', 't', 'y', 'p']]

matricespirala(mat, 0, 0, 4, 4)