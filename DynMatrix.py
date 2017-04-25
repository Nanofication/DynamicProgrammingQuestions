"""

Dynamic Matrix

"""



def MemorizedMatrixOrder(p):
    n = len(p) - 1

    m = [[0] * n for i in range(n)]

    s = [[0] * n for i in range(n)]

    for l in range(1,n):
        for i in range(0, n - l):
            j = i + l
            m[i][j] = 100000000

            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    for i in m:
        print i

    print s


p = [10, 5, 2, 20, 12, 4, 60]

MemorizedMatrixOrder(p)