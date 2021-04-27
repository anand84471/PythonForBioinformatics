def filter_seq(seq,length_cuttoff=10,gc_value_cutoff=50):
    length=len(seq)
    def get_gc_percent(seq):
        return 100*(seq.count("G")+seq.count("C"))/len(seq)
    gc_value=get_gc_percent(seq)
    if length>length_cuttoff and gc_value<gc_value_cutoff:
        print("This is an ideal seq with length= {} and gc value= {}".format(length,gc_value))
    else:
        print("This is not an ideal seq with length= {} and gc value= {}".format(length,gc_value))
        


filter_seq("ATGTCGATAGATAAGT",10,90) #length and gc value we passing
filter_seq("ATGTCGATAGATAAGT",100)  #gc_value_cutoff=50 ,length_cutoff=100
filter_seq("ATGTCGATAGATAAGT")  #gc_value_cutoff=50 ,length_cutoff=10