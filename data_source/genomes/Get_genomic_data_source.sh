#!/usr/bin/sh

## Genome files
wget ftp://ftp.wormbase.org/pub/wormbase//species/c_elegans/sequence/genomic/c_elegans.PRJNA13758.WS255.genomic.fa.gz
wget ftp://ftp.wormbase.org/pub/wormbase//species/c_briggsae/sequence/genomic/c_briggsae.PRJNA10731.WS255.genomic.fa.gz
wget ftp://ftp.wormbase.org/pub/wormbase//parasite/releases/WBPS8/species/strongyloides_ratti/PRJEB125/strongyloides_ratti.PRJEB125.WBPS8.genomic.fa.gz
wget ftp://ftp.wormbase.org/pub/wormbase//parasite/releases/WBPS8/species/strongyloides_stercoralis/PRJEB528/strongyloides_stercoralis.PRJEB528.WBPS8.genomic.fa.gz
gunzip *.gz
## Genome length files
python ../../bin/fasta_length.py c_elegans.PRJNA13758.WS255.genomic.fa > CE.ref.fa.len.txt
python ../../bin/fasta_length.py c_briggsae.PRJNA10731.WS255.genomic.fa > CBG.ref.fa.len.txt
python ../../bin/fasta_length.py strongyloides_ratti.PRJEB125.WBPS8.genomic.fa > SR.ref.fa.len.txt
python ../../bin/fasta_length.py strongyloides_stercoralis.PRJEB528.WBPS8.genomic.fa > SS.ref.fa.len.txt
