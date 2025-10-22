def are_we_ana(word1,word2):
    w1=sorted(list(word1))
    w2=sorted(list(word2))
    return w1==w2

print(are_we_ana('silent','listen'))
