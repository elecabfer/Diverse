#print
print "Hello world\n";

#open output
open(OUT,">$OUTFILE") or die $!;

#write output
print OUT "chr\tcoord\tCG\ttype\tA\tT\tC\tG\tTotal\tAgDNA\tTgDNA\tCgDNA\tGgDNA\tTotalgDNA\teditbasecount\tTotal\teditbaseGenomecount\tGenomeTot\n";
#script with options
my $USAGE = "find_rnaeditsites.pl -a annotation_file -t mysql_table -g gDNAtable -e experiment -o outfile\n";
my %option;
getopts( 'a:t:e:g:c:o:j:k:h', \%option );
if ( $option{a} && $option{t} && $option{g} && $option{e} && $option{o} && $option{j}) {
    $annotationfile = $option{a};
    $tablename = $option{t};
    $exp = $option{e};
    $gDNAtablename = $option{g};
    $OUTFILE = $option{o};
    $gexp = $option{j};
    if (exists $option{k}) {
	$gDNAtp =  $option{k};
    } else {
        die "value for gDNAtp is not being set";
       
##saving count of bases in variables "Acount, Zcount...)
my %gstrings = ("A"=>"g.Acount","T"=>"g.Tcount","C"=>"g.Ccount","G"=>"g.Gcount");
close OUT;
exit;
