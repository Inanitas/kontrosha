f=open('Perepis.txt', 'r')
sum=int()

for i in f:
    srez=i[:i.rfind('.'):-1]
    if int(srez[::-1])<=int(1978) :
        print(i)

        sum+=1
        #[::-1]
print(sum)