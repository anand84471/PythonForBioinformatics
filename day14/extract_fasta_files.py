#first 10 sequences having greater length
from Bio import SeqIO
handler=SeqIO.parse("ls orchid.fasta","fasta")

fasta_sequences_lengths={}
for sequenes in handler:
    fasta_sequences_lengths[sequenes.id]=len(sequenes.seq)

#sorting the dictionary based on values
lengths=list(fasta_sequences_lengths.values())
lengths.sort()
lengths.reverse()
print(lengths)
handler=SeqIO.parse("ls orchid.fasta","fasta")

result_file=open("result.fasta","w")
for sequenes in handler:
    if len(sequenes.seq)>=lengths[9]:
        result_file.write(sequenes.id)
        result_file.write("\n")
        result_file.write(str(sequenes.seq))
        result_file.write("\n")
result_file.close()
    
    

