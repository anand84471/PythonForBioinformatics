from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

#creating a seqrecord object
#step1 : create a seq object
obj_seq=Seq("CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGATGAGACCGTGGAATAAACGATCGAGTG")
#step2: passing seq info or SeqRecord
obj_seqrecord=SeqRecord(obj_seq)

#step 3: Adding additiona information
obj_seqrecord.id="2765658"
obj_seqrecord.description=">gi|2765658|emb|Z78533.1|CIZ78533 C.irapeanum 5.8S rRNA gene and ITS1 and ITS2 DNA"
print(obj_seqrecord)


#Reading the seqrecord object

#get the seq information
seq_info=obj_seqrecord.seq #seq_info==>Seq object
#print(seq_info)
#translate 
#print(seq_info.translate())


#get the id
print(obj_seqrecord.id)
obj_seqrecord.id="New id"


#get the description
print(obj_seqrecord.description)
#setting the description
obj_seqrecord.description="New description"

obj_Se