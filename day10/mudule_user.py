#from module_name import name_to_import


from module_example import E_VALUE_CUTTOFF
from module_example import get_length
from module_example import RNA
from constants import GC_VALUE_CUTOFF

print(E_VALUE_CUTTOFF)

dna_seq="TAGTCGATAGGAATTAGAA"
print(get_length(dna_seq))

rna_obj=RNA("UAGCAUAUAG")
print(rna_obj)
