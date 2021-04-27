from Bio.Seq import Seq


dna_seq=Seq("ATGCTAGTAGAGAATT")
#transcription
print(dna_seq.transcribe())
#getting the complement
print(dna_seq.complement())
print(dna_seq.count("A"))
print(dna_seq.count("G"))

rna_seq=dna_seq.transcribe()

print(rna_seq.back_transcribe())



rna_seq=Seq("AUGCUAGUAGAGAAUU")
print(rna_seq.back_transcribe())
