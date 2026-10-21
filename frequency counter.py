n=25444687999958231
freq=[0]*10
while n>0:
    digit=n%10
    freq[digit]+=1
    n=n//10
for i in range(0,10):
    if (freq[i]>2):
        print(f"freq {i} is {freq[i]}" )
