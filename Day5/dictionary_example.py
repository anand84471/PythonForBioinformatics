mortality_count={
    "1982":75,
    "1983":101,
    "1984":108
}

cancer_type_mortality_count={
    "Acute lymphoblastic leukaemia (ALL)":100,
    "Acute myeloid leukaemia (AML)":500,
    "Anal cancer":700
}
#Accessing the data from the dict
#dict_name[key_name]
print(mortality_count["1982"])
print(cancer_type_mortality_count["Anal cancer"])
print(mortality_count["1983"])



#Adding the data to the dict
#dict_name[kay_name]=value
mortality_count["1985"]=180
mortality_count["1986"]=188
print(mortality_count)


#modify the value in the dict
#dict_name[key_name]=updated_value
mortality_count["1986"]=200


#adding two dict
mortality_count1={
    "1982":500,
    "1983":800
}
mortality_count2={
    "1984":900,
    "1985":1000
}
print(mortality_count1)
mortality_count1.update(mortality_count2)
print(mortality_count1)




#keys()==>returns the keys present in the dict

mortality_count={
    "1982":75,
    "1983":101,
    "1984":108
}

years=mortality_count.keys()
print(years)

#values()==> returns the values present in the dict
print(mortality_count.values())

#clear()==>removes all the items from dict


mortality_count={
    "1982":75,
    "1983":101,
    "1984":108
}
print(mortality_count)
mortality_count.clear()
print(mortality_count)



mortality_report={
    "1982":100,
    "1983":200
}
mortality_count["1982"]=300
print(mortality_count)

mortality_report.update(mortality_count)
print(mortality_report)


