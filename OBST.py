"""

Optimal Binary Search Tree

"""

BST_TREE_NUMS = [0.2,0.3,0.35,0.15]


def Optimal_Bst(p):

    arrayLength = len(p) + 1

    e = [[0] * arrayLength for i in range(arrayLength)]

    w = [[0] * arrayLength for i in range(arrayLength)]

    root = [[0] * arrayLength for i in range(arrayLength)]

    for l in range(0, arrayLength):
        for i in range(0, arrayLength - l - 1):
            j = i + l + 1
            e[i][j] = 1000000
            w[i][j] = w[i][j-1] + p[j - 1]

            for r in range(i,j):
                t = e[i][r] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    PrintMatrix(w)
    PrintMatrix(e)
    PrintMatrix(root)

def PrintMatrix(twoDArray):
    for i in twoDArray:
        print i

    print "\n\n"

Optimal_Bst(BST_TREE_NUMS)

