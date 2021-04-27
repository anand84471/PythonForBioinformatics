file_handler=open(r"result.txt","w")
file_handler.write("Welcome to ReadMyCourse\n")
file_handler.write("Hi Everyone")
file_handler.close()



list_years=["1982","1983","1984"]
list_acc=["TsM_101\n","TsM_102\n"]
#writelines
file_handler=open(r"result_1.txt","w")
file_handler.writelines("Welcome to ReadMyCourse\n")
file_handler.writelines("Hi Everyone\n")
#additional functionality
file_handler.writelines(list_years)
file_handler.writelines("\n")
file_handler.writelines(list_acc)
file_handler.close()



file_handler=open(r"result_2.txt","a")
file_handler.writelines("Welcome to facebook\n")
file_handler.writelines("Hi Everyone\n")
file_handler.close()