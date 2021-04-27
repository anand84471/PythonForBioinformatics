from Bio  import SeqIO
path=r"genbank_file_example.gb"

#reading the file
seq_info=SeqIO.read(path,"genbank")
#print(seq_info)
seq_obj=seq_info.seq
id_info=seq_info.id
desc_info=seq_info.description



#transcribe
rna=seq_obj.transcribe()
print(rna)
protein=seq_obj.translate()
print(protein)