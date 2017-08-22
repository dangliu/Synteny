#!/usr/bin/sh

## Make sure preparing protein files before doing these.

## GFFs
wget ftp://ftp.wormbase.org/pub/wormbase//species/c_elegans/gff/c_elegans.PRJNA13758.WS255.annotations.gff3.gz
wget ftp://ftp.wormbase.org/pub/wormbase//species/c_briggsae/gff/c_briggsae.PRJNA10731.WS255.annotations.gff3.gz
wget ftp://ftp.wormbase.org/pub/wormbase//parasite/releases/WBPS8/species/strongyloides_ratti/PRJEB125/strongyloides_ratti.PRJEB125.WBPS8.annotations.gff3.gz
wget ftp://ftp.wormbase.org/pub/wormbase//parasite/releases/WBPS8/species/strongyloides_stercoralis/PRJEB528/strongyloides_stercoralis.PRJEB528.WBPS8.annotations.gff3.gz
gunzip *.gz
## Coding gene GFFs
# C.elegans
cat c_elegans.PRJNA13758.WS255.annotations.gff3 | grep WormBase | grep -v WormBase_transposon | awk '$3 == "gene"' > c_elegans.gene.gff 
cat ../proteins/c_elegans.fasta | grep \> > c_elegans.protein.list
python ../../bin/noncoding_gene_filter.py c_elegans.protein.list c_elegans.gene.gff > c_elegans.coding_gene.gff
# C.briggsae
cat c_briggsae.PRJNA10731.WS255.annotations.gff3 | grep WormBase | grep -v WormBase_transposon | awk '$3 == "gene"' > c_briggsae.gene.gff 
cat ../proteins/c_briggsae.fasta | grep \> > c_briggsae.protein.list
python ../../bin/noncoding_gene_filter.py c_briggsae.protein.list c_briggsae.gene.gff > c_briggsae.coding_gene.gff
# S.ratti
cat strongyloides_ratti.PRJEB125.WBPS8.annotations.gff3 | grep WormBase | grep -v WormBase_transposon | awk '$3 == "gene"' > s_ratti.gene.gff 
cat ../proteins/s_ratti.fasta | grep \> > s_ratti.protein.list
python ../../bin/noncoding_gene_filter.py s_ratti.protein.list s_ratti.gene.gff > s_ratti.coding_gene.gff
# S.stercoralis
cat strongyloides_stercoralis.PRJEB528.WBPS8.annotations.gff3 | grep WormBase | grep -v WormBase_transposon | awk '$3 == "gene"' > s_stercoralis.gene.gff 
cat ../proteins/s_stercoralis.fasta | grep \> > s_stercoralis.protein.list
python ../../bin/noncoding_gene_filter.py s_stercoralis.protein.list s_stercoralis.gene.gff > s_stercoralis.coding_gene.gff
