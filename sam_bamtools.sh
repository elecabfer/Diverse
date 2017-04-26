module add UHTS/Analysis/samtools/1.3;
module add Emboss_package/EMBOSS/6.6.0;

#filter mapped reads in bowtie2
#to bam
samtools view -b -F 4 bwt2_fast/"$i"_bowtie2_hg19_fast.sam	> bwt2_fast/"$i"_bowtie2_hg19_fast_mapped.bam 
#to fasta
samtools fasta -F 4  bwt2_fast/"$i"_bowtie2_hg19_fast.sam  > bwt2_fast/"$i"_bowtie2_hg19_fast.fasta

#sam to bam
samtools view -Sb bwt2_fast/"$i"_bowtie2_hg19_fast.sam >  bwt2_fast/"$i"_bowtie2_hg19_fast.bam

#bam to fasta
samtools fasta  bwt2_fast/"$i"_bowtie2_hg19_fast.bam  > bwt2_fast/"$i"_bowtie2_hg19_fast.fasta
seqret -sequence bwt2_fast/"$i"_bowtie2_hg19_fast.bam -outseq bwt2_fast/"$i"_bowtie2_hg19_fast.fasta


