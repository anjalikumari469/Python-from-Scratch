# wap to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dict and add one by one.use subject name as key and marks as value.

marks = {}
x = int(input("Enter phy:"))
marks.update({"phy ": x})

x = int(input("Enter maths:"))
marks.update({"maths": x})

x = int(input("Enter chem:"))
marks.update({"chem": x})

print(marks)