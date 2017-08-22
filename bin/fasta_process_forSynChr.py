#!/usr/bin/python

# a script for transforming gff and fasta file for SynChro ConvertFasta.py 
# format:
#[A_scf]<tab>[block_strat_gene]<tab>[gene_start]<tab>[gene_end]<tab>[block_end_gene]<tab>[gene_start]<tab>[gene_end]<tab>[+]<tab>[block_length]
#+
#[B_scf]<tab>[block_strat_gene]<tab>[gene_start]<tab>[gene_end]<tab>[block_end_gene]<tab>[gene_start]<tab>[gene_end]<tab>[+/-]<tab>[block_length]
# input argv[1]: gene.gff
# input argv[2]: gene.fasta

# output1: ForSynChr.SP.fasta


usage = """
Arrange gff and fasta for SynChro input converting,
usage:

python fasta_process_forSynChr.py gene.gff gene.fasta tag


Written by Dang, Academia sinica, Jan 16, 2017.


"""


import sys, re

if __name__ == "__main__":
	if len(sys.argv) < 4:
			print usage
			sys.exit( 0 ) 


gff = open(sys.argv[1], 'r')
fasta = open(sys.argv[2], 'r')
tag = sys.argv[3]

out_f = open('ForSynChr.' + sys.argv[2], 'w')


# make a dit to collect gene and their scf coordinate in gff
dit = {}

line = gff.readline()

while(line):
	line_s = re.split(r'\s+', line)
	gene = re.sub(r'[A-Za-z]*:', '', line_s[8].split(';')[0]).replace('ID=', '')
	scf = line_s[0]
	s = line_s[3]
	e = line_s[4]
	strand = line_s[6]
	dit[gene] = []
	dit[gene].append(scf)
	dit[gene].append(s)
	dit[gene].append(e)
	dit[gene].append(strand)	
	line = gff.readline()

print 'gff info is saved ! \n'
gff.close()

check_n = 0
line = fasta.readline()

while(line):
	if ('>' in line):
		NAME = line.split('|')[0].replace('>', '')
		g_ID = line.split('|')[1]
		if (g_ID in dit):
			out_f.write('>' + tag + g_ID + ' ' + NAME + ' ' + tag + dit[g_ID][0] + ' ' + dit[g_ID][1] + ' ' + dit[g_ID][2] + ' ' + dit[g_ID][3] + '\n')
			check_n = 1
	else:
		if (check_n == 1):
			out_f.write(line)
			check_n = 0
	line = fasta.readline()

print 'fasta info is saved ! \n'
fasta.close()


out_f.close()


print 'All done!\n'

# last_v20170116
