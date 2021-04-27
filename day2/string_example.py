seq="ATGCTAGATGATATTA"
#len function
length=len(seq)
print(length)


#count function
count_g=seq.count("G")
print(count_g)

count_a=seq.count("A")
print(count_a)


gc_percentage=100*(count_g+seq.count("C"))/length
print(gc_percentage)




seq="ATGCTAGATGATATTA"
#    0123456789
print(seq[2])
print(seq[5])
print(seq[8])
print(seq[5])
print(seq[11])

seq="ATGCTAGATGATATTA"
#                 -2-1
print(seq[-1])
print(seq[-3])



#slicing
seq="ATGCTAGATGATATTA"
print(seq[2:6])

#seq_name[start:stop] ==>start -stop-1

print(seq[3:5]) #===3 4


#slicing
seq="atcggcc"
print(seq[3:])
print(seq[:5])
print(seq[:])


#stepping
seq="atgcta"
print(seq[::2])
print(seq[1::2])
