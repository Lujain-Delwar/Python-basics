#Ans to qn 1
a=int(input("Enter a number:"))
if a%2==0:
    print("The number is even")
elif a%2!=0:
    print("The number is odd")
else:
    print("The number is zero")

# Ans to qn 2
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
o=input("Enter the operator:")
if o=="+":
    print("The sum is:",n1+n2)
elif o=="-":
    print("The difference is:",n1-n2)
elif o=="*":
    print("The product is:",n1*n2)
elif o=="/":
    if n2!=0:
        print("The result is:",n1/n2)
    else:
        print("Error")
else:
    print("Invalid operator")

# Ans to qn 3
sum=0
for i in range(1,101):
    if i%2==0:
        sum=sum+i
print("The sum of even numbers from 1 to 100 is:",sum)