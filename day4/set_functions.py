# add() :Adds an element to the set
# clear(): Removes all the elements from the set
# copy(): Returns a copy of the set
# difference(): Returns a set containing the difference between two or more sets
# difference_update(): Removes the items in this set that are also included in another, specified set
# discard(): Remove the specified item
# intersection(): Returns a set, that is the intersection of two other sets
# intersection_update(): Removes the items in this set that are not present in other, specified set(s)


set_example={"AAA"}

# add() :Adds an element to the set

set_example={"AAA"}
set_example.add("TT")
print(set_example)

# clear(): Removes all the elements from the set


set_example={"AAA","AAA"}
set_example.clear()
print(set_example)


set_example={"AAA","AA","AA"}
print(set_example)



set_example={"AAA","AA","AA"}
set_example.clear()
set_example.add("AA")
set_example.add("AA")
print(set_example)


# copy(): Returns a copy of the set

set1={"AA","TT"}
copy_set1=set1
copy_set1.add("GC")
print(set1)



set1={"AA","TT"}
copy_set1=set1.copy()
copy_set1.add("GC")
print(set1)


