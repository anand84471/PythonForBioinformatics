#+
print(2+2)
print(2-2)
print(2*2)
print(4/2)
print(4//3) #
print(8%3)
print(3**2) # 3*3
print(3**3) # 3*3*3 

#BODMAS Rule
print(3+2-4)
print(2+2/2)



#comparison operators
print(2<3)
print(2<=2)
print(2==2)
print(2!=2)


#Assignment operators
a=2
a+=2 #a=a+2
print(a)


a=2
a-=2 #a=a-2
print(a)

a=2
a*=2 #a=a*2
print(a)


a=2
a+=2 #a=a+2 #4
a*=2 #a=a*2 #4*2=8
print(a)

a=3
a=a+4 #7
a*=2 #7*2 =14
a-=2 #14-2 =12
print(a)




seq1="ATGCTAGATA"
seq2="AGCGAG"

len_seq1=len(seq1) 
len_seq2=len(seq2)

print(len_seq1) #10
print(len_seq2) #6

print(len_seq1<10 and len_seq2>14)
print(len_seq1<10 and len_seq2>10)
#       False

print(len_seq1<12 and len_seq2>5)

#     True            True


#or operator
seq1="ATGCTAGATA"
seq2="AGCGAG"

len_seq1=len(seq1)  #10
len_seq2=len(seq2) #6


print(len_seq1<11 or len_seq2>14)
#         True
print(len_seq1<10 or len_seq2>2)
#       False        True

print(len_seq1<12 or len_seq2>5)

#     True            True


#not operator
seq1="ATGCTAGATA"
len_seq1=len(seq1)  #10
print( len_seq1<12)
print(not len_seq1<12)

#TsM101
e_value=0.001
score=30
print(e_value<0.005 and score>50) 


#membership operators
#in
seq=["ATGAT","ATG"]

print("ATGA" in seq)
#not in
print("ATGA" not in seq)



