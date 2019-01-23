matriz = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]



        
# recebe numero linhas
N = int(raw_input())
# recebe numero colunas
M = int(raw_input())


# recebe entrada da matriz
mat = []
for i in range(N):
    mat.append(map(int, raw_input().split()))
# monta matriz para visitados inicializado com -1
visitado = []
for i in range (N):
    v = []
    for j in range (M):
        v.append(-1)
    visitado.append(v)

# profundidade, recursivo
def prof(i, j, mat, visit, c):
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]): return
    if mat[i][j] == 0: return
    if visit[i][j] != -1: return
    visit[i][j] = c
    for d in matriz:
        prof(i+d[0], j+d[1], mat, visit, c)


c = 0
for i in range(N):
    for j in range(M):
        prof(i, j, mat, visitado, c)
        c += 1

count = [0]*(N*M)
for i in range(N):
    for j in range(M):
        if visitado[i][j] != -1:
            count[visitado[i][j]] += 1
            
print max(count)
