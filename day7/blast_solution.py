# results={
#     "gi|2765658|emb|Z78533.1|CIZ78533":["KJ939539.1","FR720328.1"],
#     "gi|2765657|emb|Z78532.1|CCZ78532":["JN018070.1","JN018079.1"]
# }


# result={
    
# }

# result={
#     "gi|2765658|emb|Z78533.1|CIZ78533":[].append(JF796914.1)
# }
#gi|2765649|emb|Z78524.1|CFZ78524	JF796914.1	85.048	729	89	13	1	713	1	725	0.0	726
file_handler=open("blast_output.txt")
dict_result={}


E_VALUE_CUTOFF=5.22e-130
SCORE_CUTTOFF=90
for lines in file_handler.readlines():
    if not lines.startswith("#"):
        if float(lines.split()[-2])<E_VALUE_CUTOFF and float(lines.split()[2])>SCORE_CUTTOFF:
            acc_id=lines.split()[0]
            hit=lines.split()[1]
            if acc_id in dict_result.keys():
                dict_result[acc_id].append(hit)
            else:
                dict_result[acc_id]=[hit]

for key in dict_result.keys():
    print(key)
    print(dict_result[key])
    print("------------------------------")

file_handler.close()
         