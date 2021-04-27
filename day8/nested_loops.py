# records={
#     "2765651":{
#         "file_name":"file1", "is_blast_done":True
#     },
#     "2765650":{
#         "file_name":"file2","is_blast_done":False
#     },
#     "2765656":{
#         "file_name":"file3","is_blast_done":True
#     }
# }


# for keys in records.keys():
#     print(keys)
    


# sequeces=["ATAGATAGATA","ATAGATGATA","ATAGATAGTC","ATGCTAGTA","ATGCTAGAT"]

# for seq in sequeces:
#     for bases in seq:
#         print(bases,end=" ")
#     print()



HITS_TO_SEARCH="Hit7"
blast_results={
    "file1":["Hit1","Hit2","Hit3"],
    "file2":["Hit5","Hit7","Hit9"],
    "file3":["Hit12","Hit11","Hit10"]
}

for files in blast_results.keys():
    for hits in blast_results.get(files):
        if hits==HITS_TO_SEARCH:
            print("Found in the file",files)
        


list_seq1=["ATGC","ATGCA","ATCGAA","AA"]
list_seq2=["ATA","GCC","CCC","CCCC","AA"]

#ATGC  ["ATA","GCC","CCC","CCCC","AA"]
#ATGCA ["ATA","GCC","CCC","CCCC","AA"]
#ATCGAA ["ATA","GCC","CCC","CCCC","AA"]

for every_seq_1 in list_seq1:
    for every_seq_2 in list_seq2:
        if every_seq_1==every_seq_2:
            print(every_seq_1)
            



print("--------------------------------------")
seq=["ATGC","ATGCA","ATCGAA","AA","ATGC","ATGCA","ATCGAA","AA"]

for sequences in seq:
    if sequences=="ATCGAA":
        print("Found")
        break
    print(sequences)
    

