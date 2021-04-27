#1 upper: converts the seq in upper case

seq="ATATATATATATaatT"
cureated_seq=seq.upper()
print(cureated_seq)



#2: lower function : converts the seq in lower case

cureated_seq=seq.lower()
print(cureated_seq)



seq1="ATATTATAGAT"
seq2="ATGCTAGATTA"
result=seq1+seq2+"AAA"
print(result)


seq1="ATaT"
seq2="Tg"
result=seq2.upper()+seq1.lower()
print(result)
print(seq1.upper()[0:2])  #seq1.upper()==ATAT[0:2]  ==> 
#                                        012

print(seq1.lower()[:3]) #seq1.lower()==>atat[:3]
#find function




#find function =>Index of first occurence of character specifies
seq="ATGCTAGTAGATATTAAG"
#    0123456789
print(seq.find("A"))
print(seq.find("U"))
print(seq.find("AGATA"))
print(seq.find("AT"))
print(seq.find("G",10))


#split function
seq="ATCGTAGATAGATTTTTGATGAATAT"
print(seq.split("T"))
print(seq.split("A*T"))

info=">gi|2765620|emb|Z78495.1|PEZ78495 45 NO_OF_ADENOSINE"
print(info.split("|")[1])



['>gi', '2765620', 'emb', 'Z78495.1', 'PEZ78495 45 NO_OF_ADENOSINE']
#  0      1          2          3       4           5



line1="PREDICTED: Carica papaya cold-regulated 413 plasma membrane...    Carica papaya   papaya          3649       268    268   47%   4e-67 76.21  1009       XM_022049453.1   "
line2="PREDICTED: Carica papaya cold-regulated 413 plasma membrane...    Carica papaya   papaya          3649       268    268   47%   4e-67 76.21  1009       XM_022049453.1   "
line3="PREDICTED: Citrus sinensis cold-regulated 413 plasma membrane...  Citrus sinensis sweet orange    2711       254    254   53%   1e-62 74.71  880        XM_006466626.3  "
print(line1.split()[-4])
print(line2.split()[-4])
print(line3.split()[-4])



print(line1.split()[-1])
print(line2.split()[-1])
print(line3.split()[-1])


#reverse the seq
seq="TAGATAGATTATAAAGATAG"
print(seq[::-1])


#relace function
seq="ATAGATAGAT*AGATAGATTAGACTAGAGT"
print(seq.replace("*",""))
print(seq.replace("*","-------"))


seq="ATAGATAGAT*AGATA*GATTAGACTAGAGT"
print(seq.replace("*",""))
print(seq.replace("*","-------"))
print(seq)


#Mutation
seq="TAGATA" #TANATA
seq=seq[0:2]+"N"+seq[3:]
print(seq)




# from Bio.Seq import Seq
# seq=Seq("TAGATTAAA")
# mutable_seq=seq.tomutable()
# mutable_seq[2]="N"
# print(mutable_seq)







