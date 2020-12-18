from Bio.Seq import Seq
from Bio.SeqUtils import GC
"""Sequnce object"""
#sequnce objects are used to get the information of DNA Sequnce
#Creating a sequnce object
my_seq=Seq("ATGCTATC")
#getting the no of adenosine and no of thymine
no_of_adenosine=my_seq.count("A")
no_of_thymine=my_seq.count("T")
print(no_of_adenosine,no_of_thymine)

"""calculating the GC percentage"""
#Bio.SeqUtils has a dunction GC to calculate the GC percentage
gc_percentage=GC(my_seq)
print(gc_percentage)

"""Concatination of the sequnce"""
my_seq1=Seq("ATGC")
my_seq2=Seq("ATGCTA")
concatinated_sequence=my_seq1+my_seq2
print(concatinated_sequence)
#string can also be joined using join method
spacer=Seq("NNN"*3)
print(spacer.join([my_seq1,my_seq2]))

"""changing the cases"""
my_seq=Seq("ATgc")
print(my_seq.upper())
print(my_seq.lower())

"""Nucleotide sequnce and reverse complment"""
# valid complement sequnce https://www.mathworks.com/help/bioinfo/ref/baselookup.html 
my_seq=Seq("AGTCATA")
print(my_seq.complement())
print(my_seq.reverse_complement())

"""Removing spaces"""
my_seq=Seq("ATGCTTT AT")
my_seq=str(my_seq).replace(" ","")
print(my_seq)

"""Transcription"""
my_seq=Seq("ATTTTGCTA")
# print(my_seq.transcribe())
#true transcription
#dna->reverse_complement_dna->{T==>U}->messenger_rna
messenger_rna=my_seq.reverse_complement().transcribe()
print(messenger_rna)

"""Back transcribe"""
print(messenger_rna.back_transcribe())

"""Trnsalation"""
protein=messenger_rna.translate()
print(protein)
#By default, translation will use the standard genetic code (NCBI table id 1)
#We need to tell the translation function to use the relevant geneticcode instead:
protein=messenger_rna.translate(table="Vertebrate Mitochondrial")
print(protein)
# You can also specify the table using the NCBI table number which is shorter, and often included in the
# feature annotation of GenBank files:

"""Transalational tables"""
#internally biopython usages   codon table objects derived from
# the NCBI information at ftp://ftp.ncbi.nlm.nih.gov/entrez/misc/data/gc.prt , also shown on 
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi in a much more readable layout.

# Standard translation table
from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
# or we can use id standard_table = CodonTable.unambiguous_dna_by_id[1]
print(standard_table)
# similarly mitochondrial table
mitocondria_table=CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
print(mitocondria_table)

"""Comparing Sequnce"""
# seq1==seq2==>True if both the sequnce are same 
# seq1==seq2==>False if both the sequnce are not same

"""Mutable Sequnce"""
#as sequnec
seq1=Seq("ATGCTTATATAT")
mutable_seq=seq1.tomutable()