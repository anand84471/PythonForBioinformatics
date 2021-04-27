def get_gc_percent(seq):
    return 100*(seq.count("G")+seq.count("C"))/len(seq)

class DNA:
    seq="ATGCTAGATAGAGT"
    length=10
    gc_value=20
    
    #constructors
    #special functions that get automaitically called while creatting the object of the class
    def __init__(self,seq):
        self.seq=seq

    def get_gc_percentage(self):
        self.gc_value=get_gc_percent(self.seq)
        return self.gc_value
    def get_length(self):
        self.length=len(self.seq)
        return self.length
    


seq="ATGCTGATAGATATATTA"
obj_dna=DNA(seq)
print(obj_dna.get_length())
print(obj_dna.get_gc_percentage())