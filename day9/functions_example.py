
def get_length(seq):
    return len(seq)


sequence="ATGCTAGTATGA"
print(get_length(sequence)) #get_length(sequence) calling the function







def get_sequence():
    return "ATGCTAGTAGAAAAAAAAATGATAGATGATATAA"

def get_gc_value_cutoff():
    return 0.0001

seq=get_sequence()
print(seq)


cutoff=get_gc_value_cutoff()
print(cutoff)









# def get_length(seq):
#     return len(seq)

def get_gc_percent(seq):
    return 100*(seq.count("G")+seq.count("C"))/len(seq)

#default parameters
# def is_desired_seq(seq,gc_value):
#     if get_gc_percent(seq)<gc_value:
#         return "This is an ideal seq"
#     else:
#         return "This is not an ideal seq"


def is_desired_seq(seq,gc_value=60):
    if get_gc_percent(seq)<gc_value:
        return "This is an ideal seq"
    else:
        return "This is not an ideal seq"


print(is_desired_seq("ATGC",55))
print(is_desired_seq("ATGC"))









#FILTER SEQ IF LENGTH >specified length AND GC_VALUE<SPECIFIED GC VALUE

# def filter_seq(seq,length_cuttoff,gc_value_cutoff):
#     length=len(seq)
#     gc_value=get_gc_percent(seq)
#     if length>length_cuttoff and gc_value<gc_value_cutoff:
#         print("This is an ideal seq with length= {} and gc value= {}".format(length,gc_value))
#     else:
#         print("This is not an ideal seq with length= {} and gc value= {}".format(length,gc_value))


def filter_seq(seq,length_cuttoff=10,gc_value_cutoff=50):
    length=len(seq)
    gc_value=get_gc_percent(seq)
    if length>length_cuttoff and gc_value<gc_value_cutoff:
        print("This is an ideal seq with length= {} and gc value= {}".format(length,gc_value))
    else:
        print("This is not an ideal seq with length= {} and gc value= {}".format(length,gc_value))


filter_seq("ATGTCGATAGATAAGT",10,90) #length and gc value we passing
filter_seq("ATGTCGATAGATAAGT",100)  #gc_value_cutoff=50 ,length_cutoff=100
filter_seq("ATGTCGATAGATAAGT")  #gc_value_cutoff=50 ,length_cutoff=10














