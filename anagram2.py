def anangram(n1,n2):
    freq=[0]*10
    while (n1 !=0):
        last_digit=n1%10
        freq[last_digit]+=1
        n1//=10
    while (n2 !=0):
        last_digit=n2%10
        freq[last_digit]-=1
        n2//=10

    for i in freq:
        if (i != 0):
            return False

    return True
n1=12334
n2=43211
res=(anangram(n1,n2))
print (res)