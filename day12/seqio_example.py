from Bio import SeqIO
path=r"single_seq.fasta"
file_hanler=SeqIO.read(path,"fasta")
#file_hanler ==> SeqRecord object
print(file_hanler)


#get the sequence 
sequence=file_hanler.seq  #seq object
#get the id
id_info=file_hanler.id
#get the description
description_info=file_hanler.description
print(sequence,id_info,description_info)

