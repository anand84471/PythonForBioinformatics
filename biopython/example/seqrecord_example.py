"""
*If you are only going to be working with simple data like FASTA files, you can probably skip this chapter
*for now. If on the other hand you are going to be using richly annotated sequence data, say from GenBank
*or EMBL files, this information is quite important
1. The SeqRecord (Sequence Record) class is defined in the Bio.SeqRecord module. 
2. This class allows higher level features such as identifiers and features to be associated with a sequence.

It has the following informating related to sequnce
.seq –          The sequence itself, typically a Seq object.

.id –           The primary ID used to identify the sequence – a string. In most cases this is something like an
accession number.

.name –         A “common” name/id for the sequence – a string. In some cases this will be the same as the
accession number, but it could also be a clone name. I think of this as being analogous to the LOCUS
id in a GenBank record.

.description –  A human readable description or expressive name for the sequence – a string.

.letter annotations – Holds per-letter-annotations using a (restricted) dictionary of additional information
about the letters in the sequence. The keys are the name of the information, and the information is
contained in the value as a Python sequence (i.e. a list, tuple or string) with the same length as
the sequence itself. This is often used for quality scores (e.g. Section 20.1.6) or secondary structure
information (e.g. from Stockholm/PFAM alignment files).
31
.annotations – A dictionary of additional information about the sequence. The keys are the name of

the information, and the information is contained in the value. This allows the addition of more
“unstructured” information to the sequence.

.features – A list of SeqFeature objects with more structured information about the features on a sequence
(e.g. position of genes on a genome, or domains on a protein sequence). The structure of sequence
features is described below in Section 4.3.

.dbxrefs - A list of database cross-references as strings

"""

"""Creating a sequence object"""
# from Bio.Seq import Seq
# simple_seq=Seq("ATGCA")
# from Bio.SeqRecord import SeqRecord
# seqrecord_example_seq=SeqRecord(simple_seq)
# * we can also pass following infromation manually
# * SeqRecord(seq, id="<unknown id>", name="<unknown name>", 
# *   description="<unknown description>", dbxrefs=None, 
# *   features=None, annotations=None, letter_annotations=None)
#print(seqrecord_example_seq)
# *will print this
#     ID: <unknown id>
#     Name: <unknown name>
#     Description: <unknown description>
#     Number of features: 0
#     Seq('ATGCA')

#* we can manually set the values
# seqrecord_example_seq.id="AC125"
# seqrecord_example_seq.description="This sequnce is a sample seq"
# seqrecord_example_seq.annotations["evidence"] = "None. I just made it up."
# seqrecord_example_seq.annotations["date"] = "Identified on 12 Dec, 2020"
# print(seqrecord_example_seq)
#* now the result should look like this
# Seq('ATGCA')
# ID: AC125
# Name: <unknown name>
# Description: This sequnce is a sample seq
# Number of features: 0
# /evidence=None. I just made it up.
# /date=Identified on 12 Dec, 2020
# Seq('ATGCA')

"""Reading SeqRecord from fasta file"""
from Bio import SeqIO
#fasta_file_sequnce_record=SeqIO.read(r"C:\\D\\ReadMyCourseLiveClasses\\Python for bioinformatics\\examples\\single_fasta_seq.fasta","fasta")
# *read method can only be used if the fasta file has only one sequnce
# print(fasta_file_sequnce_record)
# *suppose our example fasta file has following sequnce
# >gi|2765605|emb|Z78480.1|PGZ78480 P.gratrixianum 5.8S rRNA gene and ITS1 and ITS2 DNA
# CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGTTGAGATCACATAATAATTGATCGAGTT
# AATCTGGAGGATCAGTTTACTTTGGTCACCCATGGGCATTTGCTATTGCAGTGACCGAGATTTGCCATCG
# AGCCTCCTTGGGAGCTTTCTTGCTGGCGATCTAAACCCTAGCCCGGCGCAGTTTTGCGCCAAGTCATATG
# ACACATAATTGGCGAAGGGGGCGGCATGCTGCCTTGACCCTCCCCAAATTATTTTTTAACAACTCTCAGC
# AACGGATAGGCCATCAGGCTAAGGGCACGCCTGCCTGGGCATTGCGAGTCATATCTCTCCCTTCAATGAG
# GCTGTCCACACATACTGTTCAGCCGGTGCGGATGTGAGTTTGGCCCCTTGTTCATTGGTACGGGGGGTCT
# AAGAGCTGCGTGGGCTTTTGTTGGTACCTAAATACGGCAAGAGGTGGACGAACTATGCTACAACAAAAAT
# GTTGTGCGAATGCCCCGGGTTGTCGTATAGATGGGCCAGCATAATCTAAAGACCCTTTTGAACCCCATTG
# GAGGCCCATCAACCCATGATCAGTTGA
# *now the print outcome will be
# ID: gi|2765605|emb|Z78480.1|PGZ78480
# Name: gi|2765605|emb|Z78480.1|PGZ78480
# Description: gi|2765605|emb|Z78480.1|PGZ78480 P.gratrixianum 5.8S rRNA gene and ITS1 and ITS2 DNA
# Number of features: 0
# Seq('CGTAACAAGGTTTCCGTAGGTGAACCTGCGGAAGGATCATTGTTGAGATCACAT...TGA')
# *getting record data
# print(fasta_file_sequnce_record.id)
# print(fasta_file_sequnce_record.name)

"""SeqRecord objects from GenBank files"""
genbannk_record=SeqIO.read(r"C:\\D\\ReadMyCourseLiveClasses\\Python for bioinformatics\\examples\\genbank_file_example.gb","genbank")
print(genbannk_record)
# ID: NC_005816.1
# Name: NC_005816
# Description: Yersinia pestis biovar Microtus str. 91001 plasmid pPCP1, complete sequence
# Database cross-references: Project:58037
# Number of features: 41
# /molecule_type=DNA
# /topology=circular
# /data_file_division=BCT
# /date=21-JUL-2008
# /accessions=['NC_005816']
# /sequence_version=1
# /gi=45478711
# /keywords=['']
# /source=Yersinia pestis biovar Microtus str. 91001
# /organism=Yersinia pestis biovar Microtus str. 91001
# /taxonomy=['Bacteria', 'Proteobacteria', 'Gammaproteobacteria', 'Enterobacteriales', 'Enterobacteriaceae', 'Yersinia']
# /references=[Reference(title='Genetics of metabolic variations between Yersinia pestis biovars and the proposal of a new biovar, microtus', ...), Reference(title='Complete genome sequence of Yersinia pestis strain 91001, an isolate 
# avirulent to humans', ...), Reference(title='Direct Submission', ...), Reference(title='Direct Submission', ...)]   
# /comment=PROVISIONAL REFSEQ: This record has not yet been subject to final
# NCBI review. The reference sequence was derived from AE017046.
# COMPLETENESS: full length.
# Seq('TGTAACGAACGGTGCAATAGTGATCCACACCCAACGCCTGAAATCAGATCCAGG...CTG')
