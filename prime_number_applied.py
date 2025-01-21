def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i)==0:
            return False
    return True
number=int(input("Enter the number"))
for i in range(1,int((number)/2)+1):
    if prime(i) and prime(number-i):
        print(f'Prime number pair is {number-i} {i}')