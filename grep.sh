#copying headers from fasta file containing ">" but NOT "Eukaryota" to a text file
grep ">" SILVA_123_SSUParc_tax_silva.fasta | grep -v "Eukaryota" > ../Aline_results/bowtie_silva/header_silva.txt

#counting
grep -c "x"
