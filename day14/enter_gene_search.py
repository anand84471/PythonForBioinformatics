from Bio import Entrez
Entrez.email="akr.cpibtc@gmail.com"
hanler=Entrez.efetch(db="gene",id="44819",rettype="gb",retmode="text")
print(hanler.read())