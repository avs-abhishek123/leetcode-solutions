array = [-1,0,1,2,-1,-4]
# array=[]
# array=[0]

res_list = []
a_list =[]
n = len(array)

flag = False

array.sort()

for i in range(0, n-1):
    left=i+1
    right=n-1
    x=array[i]
    while (left<right):
        if (x+array[left]+array[right]==0):
            a_list = [x,array[left],array[right]]
            left+=1
            right-=1
            flag = True
            res_list.append(a_list)
        elif (x+array[left]+array[right]<0): left+=1
        else: right-=1

if array ==0:
    res_list =[]
    print(res_list)
elif flag == False: print(res_list)
else: print([i for n, i in enumerate(res_list) if i not in res_list[:n]])
#  list comprehension to remove the duplicates