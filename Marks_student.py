n=input("Enter the name:")
a=int(input("Enter the English marks:"))
b=int(input("Enter the Maths marks:"))
c=int(input("Enter the Pyschology marks:"))
avg=(a+b+c)/3
print("The Average is:",avg)
if(avg>100 and avg<90):
    print("Grade A",n,"Congratulaions!!")
elif(avg>90 and avg<70):
    print("Grade B")
elif(avg>20 and avg<70):
    print("Grade C")
else:
    print(n,"has Failed the examination!!!")
