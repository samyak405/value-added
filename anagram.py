def digit_freq(n):
    freq = [0] * 10
    while n > 0:
        digit = n % 10
        freq[digit] += 1
        n = n // 10
    return freq

n1 = 1234
n2 = 3421

freq1 = digit_freq(n1)
freq2 = digit_freq(n2)

#for i in range(0, 10):
 #   print(f"digit {i}: n1 = {freq1[i]}, n2 = {freq2[i]}")

if freq1 == freq2:
    print(n1,"and",n2,"are an Anagram")
else:
    print(n1,"and",n2,"are not an Anagram")