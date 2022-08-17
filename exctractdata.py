##a=open(r'C:\Users\jayaram\OneDrive\Desktop\pythonaiml\cars.csv','r')
##b=a.readlines()
##c=[]
##for i in b:
##    c.append(i.split(','))
#print(c)
##a.close()

#count=0
#print how many origins
#for i in c:
#    if (i[8][:-1]=="US" and i[2]=='8'):
#        print(i[0])
#        count+=1
#print(count)

#weights
#w=[]
#for i in c[1:]:
#    w.append(i[5])
#print(w)
#average car weight and weight of car names
#avg=sum(w)//len(w)
#print(avg)
#for i in c[1:]:
#    if (int(i[5])>avg):
#        print(i[0])

#creating new csvfile
#x=[]
#for i in c[:10]:
#    x.append(i)
#n=open(r'C:\Users\jayaram\OneDrive\Desktop\pythonaiml\newcars.csv','w')
#for i in x:
#    n.write(','.join(i))
#n.close()
#print(x)

#creating new csv having 10 maximum weight
#weights
#j=[]
#for i in c[1:]:
#    j.append(i[5])
#j.sort(reverse=True)
#j=j[:10]

#p=[]
#for i in c[1:]:
#    if i[5] in j:
#        p.append(i)


#creating new csv having 10 maximum weights
##n=open(r'C:\Users\jayaram\OneDrive\Desktop\pythonaiml\maxweightcars.csv','w')
##for i in p:
##    n.write(','.join(i))
##n.close()
##print(p)

#unique elements in cylinder
##u=[]
##for i in c[1:]:
##    if i[2] not in u:
##        u.append(i[2])
##for i in c[1:]:
##    u.append(i[2])
####print(u)
##s=set(u)
##for i in s:
##    print(i,u.count(i))'

##m=[]
##for i in c[1:]:
##    if int(i[7])>=73:
##        m.append(i)
#print(m)
##
##n=open(r'C:\Users\jayaram\OneDrive\Desktop\pythonaiml\newmodel.csv','w')
##n.write(','.join(c[0]))
##for i in m:
##    n.write(','.join(i))
##n.close()

##with open(r'C:\Users\jayaram\OneDrive\Desktop\pythonaiml\newmodel.csv','w') as n:
##    n.write(','.join(c[0]))
##    for i in m:
##        n.write(','.join(i))
##    n.close()

import matplotlib.pyplot as plt
x=[9,3,4,2,5,7,9,0]
y=[3,5,3,6,3,7,4,8]
plt.plot(x,y,c='green')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('graph between x and y')

plt.savefig(r'C:\Users\jayaram\OneDrive\Desktop\pythonaiml\xygraph.png')

plt.show()


