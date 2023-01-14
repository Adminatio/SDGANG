n=int(input("Enter the no->"))
fact=1
sum=0
for i in range(1,n+1):
    fact*=i
    print("The fact of",n,"is:",fact)
    sum+=fact
    print("The Sum of Factorial is->",sum)
