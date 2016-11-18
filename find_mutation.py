import re
dir="/scratch/cluster/monthly/ecabello/Wareed/"
inputfiles=["gDNA5_S1", "gDNA-T75_S2" , "gDNA-TQ5_S3","Telo5_S4","Telo-T75_S5","Telo-TQ5_S6", "Telo-EV40_S7", "Telo-T740_S8", "Telo-TQ40_S9"]
#output = open("/scratch/cluster/monthly/ecabello/Wareed/new_sequencing/output_mutatio
strand="f"#raw_input("Strand? f/rev: ") #or "rev"
readlist=[]
####################################################
if strand != "rev":
    print "FORWARD"
    motivo6=r'T\wA[GT]{3,}.'
    motivos=[r'T\wAGGG',r'T\wATGG',r'T\wAGTG',r'T\wAGGT', r'T\wATTG', r'T\wAGTT', r'T\wATTT']
    output = open(dir+"/new_sequencing/output_mutations6x.xls" , 'w')
else:
    print "REVERSE"
    motivo6=r'[CA]{3}T\wA'
    motivos=[r'CCCT\wA',r'CCAT\wA',r'CACT\wA',r'ACCT\wA', r'CAAT\wA', r'AACT\wA', r'AAAT\wA']
    output = open(dir+"/new_sequencing/output_mutations_rev6x.xls" , 'w') #REVERSE

def findmotif(motifinput, motif6, fichier, salida): #motiflist y fichier son listas con los motivos y los archivos
    for f in fichier:
        R1=open(dir+"/new_sequencing/"+f+"_R1_001.fastq", "r").read().split("@NB500883")
        salida.write(f+"\nMotif:\tNumber of hits:\tProportion:\tReads matching the motif, x times:")
        a=0
        t=0
        g=0
        c=0
        r6=[]
        R1=R1[1:]
        motif6count=0
        for entry in R1:
            read2=entry.split("\n")
            read=read2[1]
            match6=re.findall(motif6,read)
            if len(match6)>6:
                r6.append(read)
        motif6count = len(r6)
        for l in motifinput:
            #print f,l
            motiflist=[]
            cuenta=[]
            countmatch=0
            countread=0
            readlist=[]
            usedmotif=[]
            for r in r6:
                match=re.findall(l,r) #motivo
                cuenta.append(len(match))
                a+=r.count("A")
                t+=r.count("T")
                c+=r.count("C")
                g+=r.count("G")
                cuenta.append(len(match))
                if len(match)>0: #or len(match6)>0 :
                    countread+=len(match)
#                    print match, len(match)
                    for m in match:
                        motiflist.append(m)
                        if m not in usedmotif:
                            usedmotif.append(m)
            permillion=int((100.0/(motif6count+1))*countread) #replace count6read by len(R1)
            salida.write("\n"+l+"\t"+str(countread)+"\t"+str(permillion)+" per 100")
            if max(cuenta)>4:  #in a tab
                for n in range(4,max(cuenta)):
                    salida.write("\t"+str(n)+"x: "+str(cuenta.count(n)+1))
        sum_nt=float(a+t+c+g)
        ratioa=(a/sum_nt)*10
        ratiot=(t/sum_nt)*10
        ratiog=(g/sum_nt)*10
        ratioc=(c/sum_nt)*10
        salida.write("\nTotal number of reads: "+str(len(R1)+1))
        salida.write('\nTotal number of reads with 6x motif: '+str(motif6count+1))
        salida.write("\nComposition   A: "+(str(ratioa))[:4]+"; T: "+ (str(ratiot))[:4]+ "; G: "+ (str(ratiog))[:4]+ "; C: "+ (str(ratioc))[:4])
        salida.write("\n\n")
        #print "\nComposition (%) A: "+str(ratioa)+"; T: "+ str(ratiot)+ "; G: "+ str(ratiog)+ "; C: "+ str(ratioc)
findmotif(motivos, motivo6,  inputfiles, output)
print "FINI!!!"
#######################################
