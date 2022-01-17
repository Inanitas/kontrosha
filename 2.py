try:
    f= open('mat_dv.txt','r')
except FileNotFoundError:
    f= open('D:\test\zada\mat_dv.txt','r') 
info=list()
max_geometry=list()
max_algebry=list()
max_geometry.append(int(0))
max_algebry.append(int(0))
for i in f:
    i=i.split()
    if not( i[2] in info): 
        info.append(0)
        info.append('name?')
        info.append(i[2])
    if int(i[3])+int(i[4])>info[0]:
        info[info.index(i[2])-2]=int(i[3])+int(i[4])
        info[info.index(i[2])-1]= i[1]+' '+i[0]
    if int(i[4])>int(max_geometry[0]):
        max_geometry.clear()
        max_geometry.append(i[4])
        max_geometry.append(i[1]+' '+i[0])
        max_geometry.append(i[2])
    if int(i[3])>int(max_algebry[0]):
        max_algebry.clear()
        max_algebry.append(i[3])
        max_algebry.append(i[1]+' '+i[0])
        max_algebry.append(i[2])  
    if  i[3] in max_algebry and not (max_algebry[1]== i[1]+' '+i[0]):
        max_algebry.append(i[3])
        max_algebry.append(i[1]+' '+i[0])
        max_algebry.append(i[2]) 
    if  i[4] in max_geometry and not (max_geometry[1]== i[1]+' '+i[0]): 
        max_geometry.append(i[1]+' '+i[0])
        max_geometry.append(i[2])
print(max_algebry)
print(max_geometry)
print(info)

        

    
        
     