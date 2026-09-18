student={
    "name" : "Anjali Kumari",
    "subjects" :{
        "phy" : 97,
        "chem" :89,
        "maths" :99,
    }
}
print(student.keys())  #return all keys -> dict.keys()
print(len(student)) 

print(student.values())  #return all values-> dict.values()

print(student.items())  # return all pairs as tuple -> dict.items()

print(student.get("name"))   #return key A/C to value -> dict.get("key")

new_dict=({"city":"Delhi" ,"name" : "Lucky kumari"}) #insert the specified items to the dict -> dict.update(newDict)
student.update(new_dict)
print(student)