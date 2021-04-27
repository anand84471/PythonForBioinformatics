b_cell_eiptopes={"AAATGT","CGGA","AHCA","CCVAA","CHGAS"} #5
t_cell_eiptopes={"AAATGT","CGGA","AHCA","AGC"} #4
 

#union
#find all the epitopes

epitopes=b_cell_eiptopes|t_cell_eiptopes
print(epitopes)
print(len(epitopes))

#intersection
#find epitopes which are both tcell and bcell epitopes
result=b_cell_eiptopes&t_cell_eiptopes
print(result)

#difference
#find all the bcell epitopes only
only_b_cell_epitopes=b_cell_eiptopes-t_cell_eiptopes
print(only_b_cell_epitopes)

#find all the t cell epitopes only
only_t_cell_epitopes=t_cell_eiptopes-b_cell_eiptopes
print(only_t_cell_epitopes)


#sym diff
#find epitopes that are present in either b cell or t cell but not in both
result=b_cell_eiptopes^t_cell_eiptopes
print(result)




b_cell_eiptopes={"AAATGT","CGGA","AHCA","CCVAA","CHGAS"} #5
t_cell_eiptopes={"AAATGT","CGGA","AHCA","AGC"} #4
x_epitopes={"AHCA","AGC","AA"} 


print(t_cell_eiptopes&x_epitopes)
print(b_cell_eiptopes&t_cell_eiptopes&x_epitopes)

print(b_cell_eiptopes|t_cell_eiptopes|x_epitopes)
print(b_cell_eiptopes|t_cell_eiptopes-x_epitopes)
