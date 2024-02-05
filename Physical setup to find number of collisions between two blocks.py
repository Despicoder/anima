import timeit

def mass_ratio(n):
    v1,v2 = 1,0
    i = 0
    while v2>0 or v1>0 or abs(v2)>abs(v1):
        i+=1
        if i%2 == 0:
            v1,v2 = v1,-v2
        else:
            v1,v2 = (((n-1)*v1/(n+1))+(2*v2/(n+1))),((2*n*v1/(n+1))-((n-1)*v2/(n+1)))
    return i

n = float(input("mass ratio: "))  

r1 = timeit.timeit('mass_ratio(n)',globals=globals(),number=1)
print('''Two blocks of variable mass are kept on a frictionless surface.
There's a wall in front of one mass. All surfaces are perfectly elastic.\n'''  )
print("No. of collisions: ",mass_ratio(n),'\n')
print("Time for computation: ",r1,"seconds")
