#open the file for reading
# path=r"C:\D\ReadMyCourseLiveClasses\Python for Bioinfromatics batch 3\Day5\blast_result.txt"
# #opening
# file_handler=open(path)
# #reading
# print(file_handler.read())
# #closing
# file_handler.close()




# read()  ⇒ Returns message in the file as string object

# readline() ⇒ reads file line by line (single line)
path=r"C:\D\ReadMyCourseLiveClasses\Python for Bioinfromatics batch 3\Day5\blast_result.txt"
file_handler=open(path)
# print(file_handler.readline())
# print(file_handler.readline())
file_handler.close()
# readlines() ⇒ Returns list of lines in the file

file_handler=open(path)
lines=file_handler.readlines()
#print(lines)
print(lines[1])
print(lines[19].split("_"))
print(lines[20].split("#"))
file_handler.close()

