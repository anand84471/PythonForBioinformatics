seq="ATGCTAGATAGATAGATGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
"""
we are dividng the seq as 
Type        Gc percentage range
A           0-40
C           40-100

find out which sequence are present in A, B and C categories.
"""
gc_per=100*(seq.count("G")+seq.count("C"))/len(seq)
print(gc_per)


if gc_per<40:
    #BLOCK OF IF
    print("Type A")
else:
    #BLOCK OF ELSE
    print("Type C")
    
seq="AGATTAAAAAAAAA"

if len(seq)>10:
    print("This is a big seq")
else:
    print("This is a small seq")
