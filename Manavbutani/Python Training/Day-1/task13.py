k=0
l=[]
def manav(t, boat_capacity, no_of_boats, weight):
    
    global k,l
    r=no_of_boats*boat_capacity
    a=max(weight)
    
    k+=1
    if r>=a:
        l.append("Yes")
    else:
        l.append("No")

    if k==t:
        for i in l:
            print(i)
            
    
    

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        trips, boat_capacity, no_of_boats = map(int,input().rstrip().split())
        weight = map(int,input().rstrip().split())
        manav(t, boat_capacity, no_of_boats, weight)