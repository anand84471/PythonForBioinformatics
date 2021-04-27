from Bio.Seq import Seq
from Bio.SeqUtils import GC

dna_seq=Seq("ATGCTAGATAGTAGAATTG")

#Count Bases

no_of_a=dna_seq.count("A")
no_of_t=dna_seq.count("T")
no_of_g=dna_seq.count("G")
no_of_c=dna_seq.count("C")
print(no_of_a)
print(no_of_g)
print(no_of_t)
print(no_of_c)






dna_seq=Seq("AGCGAATAGTAAGTAGATATAT")

if dna_seq.count("A")+dna_seq.count("T")+dna_seq.count("G")+dna_seq.count("C")==len(dna_seq):
    print("This sequence is a valid seq")
else:
    print("This seq in not a valid seq")
    


#finding the complement of sequence


dna_seq=Seq("AGCGAATAGTAAGTAGATATAT")
com_dna_seq=dna_seq.complement()
print(dna_seq)
print(com_dna_seq)

#transcription
dna_seq=Seq("AGCGAATAGTAAGTAGATATAT")
rna=dna_seq.transcribe()
print(rna)



#finding gc percentage
dna_seq=Seq("AGCGAATAGTAAGTAGATATAT")
gc_value=GC(dna_seq)
print(gc_value)



#back transcribe
rna=Seq("AGCGAAUAGUAAGUAGAUAUAU")
back_transcribed_product=rna.back_transcribe()
print(back_transcribed_product)

#reverse complement of DNA

dna_seq=Seq("AGCGAATAGTAAGTAGATATAT")
reverse_complement=dna_seq.reverse_complement()


#reverse complement RNA
reverse_complement_rna=rna.reverse_complement_rna()
print(reverse_complement_rna)

#Mutation
dna_seq=Seq("AGCGAATAGTAAGTAGATATAT")
mutable_seq=dna_seq.tomutable()
mutable_seq[3]="T"
print(mutable_seq)


#Translation
dna_seq=Seq("AGCGAATAGTAAGTAGATATAT")
protein=dna_seq.translate()
print(protein)



