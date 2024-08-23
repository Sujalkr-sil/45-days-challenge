number=int(input("enter number: "))
sum=0
temp=number
while number !=0:
    temp=number%10
    sum=sum+temp
    number=number//10
print(sum)
