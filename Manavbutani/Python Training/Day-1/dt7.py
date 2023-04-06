z=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(len(z)-1):
    for j in range(len(z)-1):
        if z[j][1] >= z[j+1][1]:
            z[j],z[j+1]=z[j+1],z[j]
            
print(z)