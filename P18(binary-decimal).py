num=int(input("Enter binary digit"))
digits=len(str(num))
temp=num
result=0
while temp>0:
    for i in range(0,digits):
        digit=temp%10
        result+=digit*(2**i)
        temp//=10
print(f"The decimal value of {num} is {result}")