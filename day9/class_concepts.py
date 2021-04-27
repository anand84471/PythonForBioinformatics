# class DNA:
#     pass


class DNA:
    #atrributes 
    seq="ATGCTAGTAGAGATA"
    length=len(seq)
    gc_value=50
    pass

dna=DNA()
print(type(dna))
print(dna.seq)
print(dna.length)
print(dna.gc_value)

#state 
print(dna.seq)
dna.seq="TTTTTTTTTTTTTTTTT"
print(dna.seq)


