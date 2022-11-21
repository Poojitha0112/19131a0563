str1,str2=[x for x in input().split(',')]
hmap={}
k=str2[-1]
for i in str1:
    if i in hmap:
        hmap[i]+=1
    else:
        hmap[i]=1
print(hmap[k])