a=open(r'C:\Users\jayaram\OneDrive\Desktop\pythonaiml\cars.csv','r')
b=a.readlines()
c=[]
for i in b:
    c.append(i.split(','))
#print(c)
a.close()

j=[]
for i in c[1:]:
    j.append(i[5])
j.sort(reverse=True)
j=j[:10]

p=[]
for i in c[1:]:
    if i[5] in j:
        p.append(i)


##n=open(r'C:\Users\jayaram\OneDrive\Desktop\pythonaiml\maxweightcars1.csv','w')
##for i in p:
##    n.write(','.join(i))
##n.close()
##print(p)
maxi=0
for i in range(1,len(c[1:])):
    if float(c[i][3])>maxi:
        maxi=float(c[i][3])
print(maxi)
    
