#reading the genbank file with the help of SeqIO
from Bio import SeqIO
# seqrecord=SeqIO.read(r"sample_genbank_file.gb","genbank")
path=r"sample_genbank_file.gb"
seqrecord=SeqIO.read(path,"genbank")
#print(seqrecord)

#id
#print(seqrecord.id)
#name
#print(seqrecord.name)
#description
#print(seqrecord.description)
#seq
#print(seqrecord.seq)


#features
#getting no of features
print(len(seqrecord.features))

for fatures in seqrecord.features:
    print("---------Feature starting---------------")
    if "translation" in fatures.qualifiers.keys():  
        print(fatures.qualifiers["translation"])
    print("---------Feature End--------------------")
    
# for fatures in seqrecord.features:
#     if fatures.type=="CDS":
#         print("---------Feature starting---------------")
#         #find the regions reposible for All CDS features
#         print(seqrecord.seq[fatures.location.start:fatures.location.end])
#         print("---------Feature End--------------------")