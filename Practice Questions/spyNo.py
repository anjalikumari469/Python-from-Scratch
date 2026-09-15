#spy number means:  A no is spy no ,if the sum of digits = product of digit.
# 1124=>1+1+2+4=8 = 1*1*2*4=8   sum==product

n=int(input("Enter any number:"))
sum=0
product=1
while(n>0):
    i=n%10
    sum=sum+i
    product=product*i
    n=n//10
if sum==product:
    print("Number is spy")
else:
    print("Number is not spy") 