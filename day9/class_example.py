def get_gc_percent(seq):
    return 100*(seq.count("G")+seq.count("C"))/len(seq)

class DNA:
    seq="ATGCTAGATAGAGT"
    length=10
    gc_value=20
    def get_gc_percentage(self):
        self.gc_value=get_gc_percent(self.seq)
        return self.gc_value
    def get_length(self):
        self.length=len(self.seq)
        return self.length
    

        





obj3_dna=DNA()
print(obj3_dna.get_length())
print(obj3_dna.length)
print(obj3_dna.get_gc_percentage())