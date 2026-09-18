#figure out a way to store 9 and 9.0 as separate values in the set.

#values = {9,"9.0"}
#print(values)

#2nd method
values ={
    ("float",9.0),("int",9)
}
print(values)