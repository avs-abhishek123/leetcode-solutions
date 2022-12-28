# s = "babad"
s = "cbbd"
n = len(s)
if n<2:
    print(n)
if n>1 and n<1000:
    init = 0
    max_len = 1
    for i in range(n):
        lower_index =i-1
        higher_index =i+1
        while higher_index<n and s[higher_index] == s[i]:
            higher_index+=1
        while lower_index >=0 and s[lower_index] == s[i]:
            lower_index-=1
        while lower_index>=0 and higher_index <n and s[lower_index] == s[higher_index]:
            lower_index-=1
            higher_index += 1
        l = higher_index-lower_index-1
        if max_len<l:
            max_len = l
            init = lower_index+1
    print(s[init:init+max_len])