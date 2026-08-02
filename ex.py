n = int(input("Height : "))
for i in range(1,n + 1):
    s = 0
    for j in range(n):
        if s == (n - i):
            print("*", end="")
        else:
            print(" ", end="")
            s = s + 1
    print("") 
print("Super cool !")
    

