from Bio import Entrez
Entrez.email="akr.cpibtc@gmail.com"
handler=Entrez.esearch(db="nucleotide",term="BRCA",retmax="100",idtype="acc")
#print(Entrez.read(handler))
#count
result=Entrez.read(handler)
# print(result["Count"])
# print(result["IdList"])
for ids in result["IdList"]:
    hanler=Entrez.efetch(db="nucleotide",id=ids,rettype="gb",retmode="text")
    print(hanler.readline())