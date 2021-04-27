from Bio.Data import CodonTable
from Bio.Seq import Seq
#finding codon table by name
standard_table =CodonTable.unambiguous_dna_by_name["Standard"]
print(standard_table)

# or we can use id 
standard_table = CodonTable.unambiguous_dna_by_id[1]
print(standard_table)

#codon table of condylostoma
condylostoma_codon_table=CodonTable.unambiguous_dna_by_id[28]
print(condylostoma_codon_table)


#transaltion
dna_seq=Seq("ATGCTGAGATGGTGGGGGGGGGGGGGGTATAGATAGATAGAGATAG")
ATGCTGAGATGGTGGGGGGGGGGGGGGTATAGATAGATAGAGATAG

yeast_codon_table=CodonTable.unambiguous_dna_by_id[3]
protein=dna_seq.translate(table=yeast_codon_table)
print(protein)

print("MTRWWGGGGYR-MEM")

