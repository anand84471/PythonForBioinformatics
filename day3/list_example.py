list_example=[1,2,3,4]
print(list_example)

sequences=["ATAGATA","ATGCTAGA","ATGTAA"]
print(sequences)


list_example=[1,2,3,4]
#             0 1 2 3 
sequences=["ATAGATA","ATGCTAGA","ATGTAA"]
#             0         1           2
print(list_example[1])
print(sequences[2])

list_example=["ATAGATA",1,True,[1,2,3]]
print(list_example)



sequences=["ATAGATA","ATGCTAGA","ATGTAA"]
print(type(sequences))


#check the length of list
print(len(sequences))

list_example=[1,2,3,4]
print(len(list_example))
print(len(list_example)+len(sequences))


#slicing

sequences=["AGCTAA","ATCGTAGA","ATGCTAGAGAT","ATGCTAGA","ATCGATGAAT"]
#               0       1           2           3           4
#           -5      -4                -3            -2            -1

print(sequences[1:4]) # 1-3
print(sequences[3:4]) # 3 
print(len(sequences[1:4]))




#reverse seq
sequences.reverse()
print(sequences)

#sort the seq
sequences=["A","G","TT","AT","GC"]
sequences.sort()
print(sequences)


gc_values=[12,25,65,2,5,23]
gc_values.sort()
gc_values.reverse()
print(gc_values)