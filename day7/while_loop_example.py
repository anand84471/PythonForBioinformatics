# while <condition>: 
#    #while body


x=2 #initilization
while x<6: #condition
    print(x)
    x+=1 #updation





# seq=["AAAAA","GGGG","AGC","AGA","GGA","CCCA"]
# we are dividng the seq as 
# Type        Gc percentage range
# A           30-40
# B           40-65
# C           65-85
# find out which sequence are present in A, B and C categories.

count=0
seq=["AAAAA","GGGG","AGC","AGA","GGA","CCCA"]
#      0       1     2       3   4     5
len_seq=len(seq)
while count<len_seq:
    current_seq=seq[count]
    gc_value=100*(current_seq.count("G")+current_seq.count("C"))/len(current_seq)
    if gc_value>30 and gc_value<40:
        print("seq{}:gc{} Type====>A".format(current_seq,gc_value))
    elif gc_value>40 and gc_value<65:
        print("seq{}:gc{} Type====>B".format(current_seq,gc_value))
    elif gc_value>65 and gc_value<85:
        print("seq{}:gc{} Type====>C".format(current_seq,gc_value))
    count+=1
    

seq=["AAAAA","GGGG","AGC","AGA","GGA","CCCA"]
x=2
while x<len(seq):
    print(seq[x])
    x+=1

gc_values=[30,40,25,68,96]
#filter all the gc values having value>60

x=0
while x<len(gc_values):
    if gc_values[x]>90:
        print(gc_values[x])
    x+=1