seq="ATGCTAGATTA"
len_seq=len(seq)  #11
gc_value=100*(seq.count("G")+seq.count("C"))/len(seq) #27
print(len_seq)
print(gc_value)

#identify the seq having length >5 and gc percentage>50

if len_seq>5:
    print("Seq length is okay")
    if gc_value>50:
        print("GC value is good")
    else:
        print("GC Value is not in the desired range")
else:
    print("Seq is too short")