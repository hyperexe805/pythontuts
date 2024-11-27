def nums(n):
    
    num1 = n[0]
    num2 = n[1]
    n0 = 0

    while n0 < n[1]: 
        n0 += 1
        num1 += n[0]
        print(n0, num1, num2)

    print(n)
    return num1
    
    

total = nums([4,3])

print(total)