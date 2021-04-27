from Bio import Entrez
Entrez.email="akr.cpibtc@gmail.com"
handler=Entrez.efetch(db="nucleotide",id="AY851614",rettype="gb",
                      retmode="text")

#writing the resul to the file
result_file=open("entrez_result.gb","w")
result_file.write(handler.read())
result_file.close()
