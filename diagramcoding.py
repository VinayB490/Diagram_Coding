print('****** DIAGRAM CODING ******')
d=[]
dicta={}
print('Enter the element and code in dictionary')
while(True):
    k=input('Enter Element : ')
    d.append(k)
    dicta[k]=input('Enter Code : ')
    j=input('To add more element in dictionary (y/n):')
    if(j=='n' or j=='N'):
        break
print(dicta)
while(True):
    a=input('Enter the String : ')
    m=''
    p=len(a)*-1
    for i in range(len(a)-1):
        s=a[i]
        if p-i>=0:
            continue
        if s not in d:
            print(s,' not found in dictionary')
            break
        else:
            n=dicta[s]
        for j in range(i+1,len(a)):
            s=s+a[j]
            if s in d:
                n=dicta[s]
                p=j
        m=m+n
    if p!=i+1:
        m=m+dicta[a[-1]]
    print(m)
    k=input('Try another String (y/n)')
    if(k=='n' or k=='N'):
        break
        
    
