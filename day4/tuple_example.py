seq1=["AAAA","ATATA","AATTA"] #list

#      0        1       2
seq2=("AAAA","ATATA","AATTA") #tuple

#         0     1       2

print(seq1[0])    #indexing is similiar in list and tuple
print(seq2[0])

seq1[0]="TT"
#seq2[0]="TT"    #tuple doesn't not allow assignmet


#count
seq2=("AAAA","ATATA","AATTA","AAAA") #tuple
print(seq2.count("AAAA"))


