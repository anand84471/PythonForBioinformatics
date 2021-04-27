#variables
E_VALUE_CUTTOFF=0.0001
seq="ATGCTAGATAGATAAGTAA"
gc_value=54

#function
def get_length(sequence):
    return len(sequence)



#class

class RNA:
    seq=None
    def __init__(self,seq_parm):
        self.seq=seq_parm
        
        
        
    