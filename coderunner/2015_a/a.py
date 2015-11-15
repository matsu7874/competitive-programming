import random
PS=[(1,0,1),(2,99,1),(4,0,7),(8,0,2),(16,10,1)]
for i in range(2,min(4,500)):
    for j in range(3):
        ps=random.sample(PS,i)
        qu = ','.join([str(ps[k][0])+','+str(ps[k][1]) for k in range(i)])
        print(qu)
