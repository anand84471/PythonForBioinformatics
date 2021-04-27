from Bio import SeqIO
handler=SeqIO.parse(r"ls orchid.fasta","fasta")
count=0
for sequences in handler:
    count+=1
print(count)
    
