# if (condition):
#     # Executes this block if
#     # condition1 is true
#     pass
# else:
#     # Executes this block if
#     # condition is false
#     pass




seq="ATGCTAGTAGAAT" 
len_seq=len(seq)

if len_seq<100:
    print("This is a big seq")
else:
    print("This is a small seq")    
    

seq="ATGCTAGATAA"
len_seq=len(seq)

if len_seq>10 and len_seq<100 and 'N' in seq:
    print("This is an ideal seq")
else:
    print("This is not an ideal seq")
    a=2
    a+=2
    print(a)





# if (condition1):
#     # Executes this block if
#     # condition1 is true
# elif (condition2):
#     # Executes this block if
#     # condition2 is true
# else:
#     # Executes this block if
#     # condition is false



condition1=False
condition2=False
condition3=False
condition4=False
if (condition1):
    print("Condition 1 block")
    # Executes this block if
    # condition1 is true
elif (condition2):
    print("Condition 2 block")
    # Executes this block if
    # condition2 is true
elif (condition3):
    print("Condition 3 block")
    # Executes this block if
    # condition2 is true
elif (condition4):
    print("Condition 4 block")
    # Executes this block if
    # condition2 is true
else:
    print("Else block")
    # Executes this block if
    # condition is false
    
