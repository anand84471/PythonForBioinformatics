seq=["AAAAA","GGGG","AGC","AGA","GGA","CCCA"]
set_seq={"AA","AGC","TTT"}
dict_seq={
    "Ass1":"ATAGAT",
    "Ass2":"TAGATAT",
    "Ass3":"ATAGAAT"
}
for sequences in seq:
    print(sequences)
    
for sequences in set_seq:
    print(sequences)
    
for ass_ids in dict_seq.keys():
    print(ass_ids)
    
for sequences in dict_seq.values():
    print(sequences)



print("-------------------------------------------------------------")
seq=["AAAAA","GGGG","AGC","AGA","GGA","CCCA"]
#     0        1      2

for sequences in seq[2:]:
    print(sequences)

for sequences in seq[1:4]:
    print(sequences)
    
    
seq=["AAAAA","GGGG","AGC","AGA","GGA","CCCA"]
for current_seq in seq:
    gc_value=100*(current_seq.count("G")+current_seq.count("C"))/len(current_seq)
    if gc_value>30 and gc_value<40:
        print("seq{}:gc{} Type====>A".format(current_seq,gc_value))
    elif gc_value>40 and gc_value<65:
        print("seq{}:gc{} Type====>B".format(current_seq,gc_value))
    elif gc_value>65 and gc_value<85:
        print("seq{}:gc{} Type====>C".format(current_seq,gc_value))
    