#!/usr/bin/sh

## Protein files
wget ftp://ftp.wormbase.org/pub/wormbase//species/c_elegans/sequence/protein/c_elegans.PRJNA13758.WS255.protein.fa.gz
wget ftp://ftp.wormbase.org/pub/wormbase//species/c_briggsae/sequence/protein/c_briggsae.PRJNA10731.WS255.protein.fa.gz
wget ftp://ftp.wormbase.org/pub/wormbase//parasite/releases/WBPS8/species/strongyloides_ratti/PRJEB125/strongyloides_ratti.PRJEB125.WBPS8.protein.fa.gz
wget ftp://ftp.wormbase.org/pub/wormbase//parasite/releases/WBPS8/species/strongyloides_stercoralis/PRJEB528/strongyloides_stercoralis.PRJEB528.WBPS8.protein.fa.gz
gunzip *.gz
mv strongyloides_ratti.PRJEB125.WBPS8.protein.fa s_ratti.PRJEB125.WBPS8.protein.fa
mv strongyloides_stercoralis.PRJEB528.WBPS8.protein.fa s_stercoralis.PRJEB528.WBPS8.protein.fa
## Protein with only longest isoforms
python ../../bin/longest.py c_elegans.PRJNA13758.WS255.protein.fa
python ../../bin/longest.py c_briggsae.PRJNA10731.WS255.protein.fa
python ../../bin/longest.py s_ratti.PRJEB125.WBPS8.protein.fa
python ../../bin/longest.py s_stercoralis.PRJEB528.WBPS8.protein.fa
