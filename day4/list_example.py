# clear()   Removes all the elements from the list
# copy()    Returns a copy of the list
# count()   Returns the number of elements with the specified value
# extend()  Add the elements of a list (or any iterable), to the end of the current list
# index()   Returns the index of the first element with the specified value
# insert()  Adds an element at the specified position
# pop() Removes the last element
# remove()  Removes the first item with the specified value
# reverse() Reverses the order of the list
# sort()    Sorts the list




list_example=[1,2,3,4,4]
#             0 1 2 3 4
print(list_example)
print(list_example[2])
print(list_example[3])

list_example1=[1,2,3,4]
list_example2=[1,3,4,5]
print(list_example1+list_example2)


sequences1=["ATGCTAGA","ATCGATAGAT","ATCGATGAATAT"]
sequences2=["ATCGATA","ATCGATA","ATCGATA","ATCGATA","ATGTAGATAT"]
fianl_seq=sequences1+sequences2
print(fianl_seq)

print(len(fianl_seq))



# clear()   Removes all the elements from the list

sequences1=["ATGCTAGA","ATCGATAGAT","ATCGATGAATAT"]
sequences1.clear()
print(sequences1)


# copy()    Returns a copy of the list
#WHY WE NEED copy
sequences1=["ATCGTA","ATGCTA","ATGCTATA"]
#             0        1        2
copy_seq=sequences1
print(copy_seq)
copy_seq[1]="AAAAAAAAA"
copy_seq[2]="TTTTTTT"
print(copy_seq)
print(sequences1)



sequences1=["ATCGTA","ATGCTA","ATGCTATA"]
#             0        1        2
copy_seq=sequences1.copy()
print(copy_seq)
copy_seq[1]="AAAAAAAAA"
copy_seq[2]="TTTTTTT"
print(copy_seq)
print(sequences1)



# count()   Returns the number of elements with the specified value

sequences=["ATCGTA","AAA","ATATA","ATAGAT","ATAGA","AAA","TT"]
no_of_times=sequences.count("AAA")
no_of_times=sequences.count("AAA")+sequences.count("TT")
print(no_of_times)



# extend()  Add the elements of a list (or any iterable), to the end of the current list
sequences1=["ATGCTAGA","ATCGATAGAT","ATCGATGAATAT"]
sequences2=["ATCGATA","ATCGATA","ATCGATA","ATCGATA","ATGTAGATAT"]

sequences1.extend(sequences2)
print(sequences1)

seq1=["AAA"]
seq2=["TTT"]
seq1.extend(seq2) # seq1=["AAA","TTTT"]
seq1.extend(seq2) #["AAA","TTTT","TTT"]
print(seq1)


seq1=["AA"]
seq2=["TT"]
seq1.extend(seq2) 
seq1.extend(seq1)
print(seq1)



# index()   Returns the index of the first element with the specified value
sequences2=["ATCGATAA","ATCGATA","TT","ATCGATA","ATCGATA","ATGTAGATAT","TT","AAA","TTTTT","TT"]
seq_to_check="ATCGATAA"
result_index=sequences2.index(seq_to_check)

result_index=sequences2.index("TT")
print(result_index)

first_pos=sequences2.index("TT")
second_pos=sequences2.index("TT",first_pos+1)
third_pos=sequences2.index("TT",second_pos+1)
print(second_pos)
print(third_pos)

print(sequences2.count("TT"))
# insert()  Adds an element at the specified position

sequences2=["ATCGATAA","ATCGATA","TT","ATCGATA","ATCGATA","ATGTAGATAT","TT","AAA","TTTTT","TT"]
#sequences2=["ATCGATAA","ATCGATA","GCC",TT","ATCGATA","ATCGATA","ATGTAGATAT","TT","AAA","TTTTT","TT"]

sequences2.insert(2,"GCCC")
print(sequences2)


# pop() Removes the last element

sequences=["AAA","TTTT"]
sequences.pop()
print(sequences)


#sort

gc_values=[1.2,3,5,6,0.4,90,20,30]
gc_values.sort()
gc_values.reverse()
print(gc_values)

sequences=["ATCGTA","TTT","AAA","AA","AAAAG","GG"]
sequences.sort()
print(sequences)
# remove()  Removes the first item with the specified value

sequences=["ATCGTA","TTT","AAA","AA","AAAAG","GG","TTT"]
sequences.remove("TTT")
sequences.remove("TTT")
#sequences.remove("TTT")
print(sequences)
print("Hi")



seq1=["AA"]
seq2=["TT"]
seq1.extend(seq2)
seq1.remove("AA")
print(seq1)