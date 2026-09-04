#wap to find the greatest of 3 no entered by the user.
a = int(input("Enter the first no: "))
b = int(input("Enter the second no: "))
c = int(input("Enter the third no: "))
if(a>b and a>c):
    greatest ='a'
elif(b>a and b>c):
    greatest ='b'
else:
    greatest ='c'
print("Greatest number is:",greatest)   