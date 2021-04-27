def calculate_gc_percent(seq):
    gc_percent=100*(seq.count("G")+seq.count("C"))/len(seq)
    return gc_percent



seq1="TCGTAGATATAA"
seq2="GCGCGGCGGAAAA"

gc_percent1=calculate_gc_percent(seq1)
gc_percent2=calculate_gc_percent(seq2)
print(gc_percent1,gc_percent2)


lis_seq=["AAAA","CTAGTAA","AGCGGAA","ATCGATA"]
for sequences in lis_seq:
    print(calculate_gc_percent(sequences))
    



def calculate_area(length,width):
    area=length*width
    return area



print(calculate_area(4,5))






