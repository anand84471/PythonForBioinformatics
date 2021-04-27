from Bio import SeqIO
handler=SeqIO.parse(r"gbcon218.seq","genbank")
count=0

# for sequences in handler:
#     count+=1
#     print(sequences.id)
    
    
for sequences in handler:
    print(sequences.id,"===>",len(sequences.features))
print(count)