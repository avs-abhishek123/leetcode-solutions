l1 = [2,4,3]
l2 = [5,6,4]

# adding the reveresed list 
res_list = [l1[::-1][i]+l2[::-1][i] for i in range(len(l1))]

for i in range(len(res_list)):
    if res_list[i]>9:
        res_list[i]=res_list[i]-10
        if i+1<len(res_list): res_list[i+1] =res_list[i+1]+1
        else: break
    else: continue
print(res_list)