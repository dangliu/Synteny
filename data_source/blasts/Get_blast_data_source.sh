#!/usr/bin/sh

## Prepare input for orthofinder
mkdir fastas
cp -s ../proteins/*.fasta ./fastas/
../../bin/filter_seq fastas/ 40 20
## Run orthofinder
../../bin/OrthoFinder_assistant -thread_n 32 -fasta_folder fastas.filtered/ -orthofinder_path ../../bin/OrthoFinder-1.1.2/orthofinder
## Get blast files
#0: c_briggsae.fasta
#1: c_elegans.fasta
#2: s_ratti.fasta
#3: s_stercoralis.fasta
cp -s ./fastas.filtered/Results*/WorkingDirectory/Blast1_1.txt CEvsCE.txt
cp -s ./fastas.filtered/Results*/WorkingDirectory/Blast0_1.txt CEvsCBG.txt
cp -s ./fastas.filtered/Results*/WorkingDirectory/Blast2_2.txt SRvsSR.txt
cp -s ./fastas.filtered/Results*/WorkingDirectory/Blast3_2.txt SRvsSS.txt
