def removeDuplicates(S):
    n = len(S)


    if (n < 2):
        return


    j = 0


    for i in range(n):


        if (S[j] != S[i]):
            j += 1
            S[j] = S[i]

             
    j += 1
    S = S[:j]
    return S