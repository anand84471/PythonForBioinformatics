#To write a program to count how many sequences in the fasta file has length>5000
from Bio import SeqIO
handler=SeqIO.parse(r"ls orchid.fasta","fasta")
result_file=open("sequences_700.fasta","w")
count=0
for sequences in handler:
    if len(sequences.seq)>700:
        result_file.write(">"+sequences.id)
        result_file.write("\n")
        result_file.write(str(sequences.seq))
        result_file.write("\n")
        count+=1
result_file.close()
print(count)