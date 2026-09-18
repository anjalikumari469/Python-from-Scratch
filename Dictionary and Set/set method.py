collection = set()
collection.add(1) #set.add() add an element
collection.add(2)
collection.add("apna college")
collection.remove(1) #set.remove() remove an element
print(collection)

collection.clear() # set.clear() empty the set
print(len(collection))

collection={"hello","apnacollege","world","coding","python"}
print(collection.pop())  #set.pop() removes a random value

set1={1,2,3,4}    #set.union(set2) combines both set values and return new
set2={2,3,4}
print(set1.union(set2))

print(set1.intersection(set2))  #set.intersection(set2) combines common values and return new