step = int(input("Enter number of steps:")) 
for i in range(1, step+1): 
    for j in range(1, i+1): 
        print(i*j, end=" ") 
    print() 
for i in range(step-1, 0, -1): 
    for j in range(1, i+1): 
        print(i*j, end=" ") 
    print()
