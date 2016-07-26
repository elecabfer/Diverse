### looking for a pattern in a proteome
import re
db=open('../152K_uniprot-homo+sapiens.fasta', 'r').read().split('>')
output=open('../motif_protein_152K_uniprot.fa', 'w')
motif=r'GQL\w\wP'
for i in db:
    sequence=i.replace('\n', '')
    match=re.search(motif, sequence)
    if match:
        #print match
        output.write('>'+i)
