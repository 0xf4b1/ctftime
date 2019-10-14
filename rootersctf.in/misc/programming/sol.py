def lcs(s1, s2):
    matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + s1[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)

    cs = matrix[-1][-1]

    return cs

print(lcs(")$kzro5fotRe)lFrjs_t{s0OmT=33gLtiJm`|et-mxssdE_U~,oI_t/@>h^>J@1;~B?v`Z!m3n<",
    "S8*r~x`o-#x:]o0RAteY5Lr-sQ9Mk.{4sj0|^C1mwtwP3poj}t{yz6i*e&mevv4bgsQ_]5xUt-_mh.&;@vQ64gp3W-8"))