def Superpower(x,y):
    ans = 1
    i = 0
    while(i < y):
        ans = ans * x
        i = i + 1
    return(ans)

print(Superpower(3,4))
