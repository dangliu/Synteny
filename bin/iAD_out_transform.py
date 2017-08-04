#!/usr/bin/python

# a script for transforming i-ADHoRe output to a more informative form
# format:
#[A_scf]<tab>[block_strat_gene]<tab>[gene_start]<tab>[gene_end]<tab>[block_end_gene]<tab>[gene_start]<tab>[gene_end]<tab>[+]<tab>[block_length]
#+
#[B_scf]<tab>[block_strat_gene]<tab>[gene_start]<tab>[gene_end]<tab>[block_end_gene]<tab>[gene_start]<tab>[gene_end]<tab>[+/-]<tab>[block_length]
# input argv[1]: A.gene.gff
# input argv[2]: B.gene.gff
# input argv[3]: iADout (segment.txt)
# output1: transformed.MCS_out
# output2: the gene pairs


usage = """
Arrange i-ADHoRe output including gff information,
usage:

python iAD_out_transform.py gff1 gff2 segment.txt


Written by Dang, Academia sinica, Jan 16, 2017.


"""


import sys, re

if __name__ == "__main__":
	if len(sys.argv) < 3:
			print usage
			sys.exit( 0 ) 


def re_AB(i):
   re_AB_i = re.sub(r'[AB]\.', '', i) 
   return re_AB_i


gff1 = open(sys.argv[1], 'r')
gff2 = open(sys.argv[2], 'r')

iAD = open(sys.argv[3], 'r')

out_f = open('transformed.' + sys.argv[3], 'w')
#out_f2 = open('gene_pair.' + sys.argv[3], 'w')


# make a dit to collect A gene and B gene and their scf coordinate in gff
dit = {}

line = gff1.readline()

while(line):
	line_s = re.split(r'\s+', line)
	gene = 'A.' + re.sub(r'[A-Za-z]*:', '', line_s[8].split(';')[0]).replace('ID=', '')
	dit[gene] = []
	dit[gene].append(line_s[3])
	dit[gene].append(line_s[4])
	line = gff1.readline()

print 'gff1 info is saved ! \n'
gff1.close()


line = gff2.readline()

while(line):
	line_s = re.split(r'\s+', line)
	gene = 'B.' + re.sub(r'[A-Za-z]*:', '', line_s[8].split(';')[0]).replace('ID=', '')
	dit[gene] = []
	dit[gene].append(line_s[3])
	dit[gene].append(line_s[4])
	line = gff2.readline()

print 'gff2 info is saved ! \n'
gff2.close()

# get the block info from ## line
# set a n for alinment pair count. if "n == the pair number" then we know it's reading the last alignment pair in one block, so can write the info of this block to output file.
# Need to notify if "reverse" in the ## line
# Need to notify that in some block the A and B will switch their site (qry <> ref). So use if 'A' in qry scf site to test
# if switch, then the reverse one in A and B need to be chenged so that the format can be consistent

# make a dit to collect gene pair, and a dit for e-value collect
#g_dit = {}
#e_dit = {}

line = iAD.readline()
line = iAD.readline() # remove header

while(line):
	line_s = re.split(r'\s+', line)
	g_s = line_s[4]
	g_e = line_s[5]
	order = line_s[6]
	if (str(order) == '0'):
		if ('A.' in line):
			A_scf = line_s[3]
			if (int(dit[g_s][0]) < int(dit[g_e][0])):
				A_start_gene = g_s
				A_end_gene = g_e
				A_strand = '+'
			else:
				A_start_gene = g_e
				A_end_gene = g_s
				A_strand = '-'
		else:
			B_scf = line_s[3]
			if (int(dit[g_s][0]) < int(dit[g_e][0])):
				B_start_gene = g_s
				B_end_gene = g_e
				B_strand = '+'
			else:
				B_start_gene = g_s
				B_end_gene = g_e
				B_strand = '-'

	else:
		if ('A.' in line):
			A_scf = line_s[3]
			if (int(dit[g_s][0]) < int(dit[g_e][0])):
				A_start_gene = g_s
				A_end_gene = g_e
				A_strand = '+'
			else:
				A_start_gene = g_e
				A_end_gene = g_s
				A_strand = '-'
		else:
			B_scf = line_s[3]
			if (int(dit[g_s][0]) < int(dit[g_e][0])):
				B_start_gene = g_s
				B_end_gene = g_e
				B_strand = '+'
			else:
				B_start_gene = g_s
				B_end_gene = g_e
				B_strand = '-'
		if (A_strand == B_strand):
			B_orientation = '+'
		else:
			B_orientation = '-'
		out_f.write(re_AB(A_scf)+'\t'+re_AB(A_start_gene)+'\t'+dit[A_start_gene][0]+'\t'+dit[A_start_gene][1]+'\t'+re_AB(A_end_gene)+'\t'+dit[A_end_gene][0]+'\t'+dit[A_end_gene][1]+'\t+\t'+str(abs(int(dit[A_start_gene][0])-int(dit[A_end_gene][1])))+'\t')
		out_f.write(re_AB(B_scf)+'\t'+re_AB(B_start_gene)+'\t'+dit[B_start_gene][0]+'\t'+dit[B_start_gene][1]+'\t'+re_AB(B_end_gene)+'\t'+dit[B_end_gene][0]+'\t'+dit[B_end_gene][1]+'\t'+B_orientation+'\t'+str(abs(int(dit[B_start_gene][0])-int(dit[B_end_gene][1])))+'\n')
	line = iAD.readline()
print 'tranformed.segment.txt is output!\n'

iAD.close()
out_f.close()

# output gene pair
#for g in g_dit:
#        out_f2.write(g + '\t' + g_dit[g] + '\n')

#print 'gene pair is output!\n'
#out_f2.close()
print 'All done!\n'

# last_v20170116
