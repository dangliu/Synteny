#!/usr/bin/python

# a script for transforming MCScanX output to a more informative form
# format:
#[A_scf]<tab>[block_strat_gene]<tab>[gene_start]<tab>[gene_end]<tab>[block_end_gene]<tab>[gene_start]<tab>[gene_end]<tab>[+]<tab>[block_length]
#+
#[B_scf]<tab>[block_strat_gene]<tab>[gene_start]<tab>[gene_end]<tab>[block_end_gene]<tab>[gene_start]<tab>[gene_end]<tab>[+/-]<tab>[block_length]
# input argv[1]: A.gene.gff
# input argv[2]: B.gene.gff
# output1: transformed.MCS_out
# output2: the gene pairs


usage = """
Arrange MCScanX output including gff information,
usage:

python MCS_out_transform.py gff1 gff2 MCSout


Written by Dang, Academia sinica, Jan 11, 2017.


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

MCS = open(sys.argv[3], 'r')

out_f = open('transformed.' + sys.argv[3], 'w')
out_f2 = open('gene_pair.' + sys.argv[3], 'w')


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

n = 0
check_n = 0
# make a dit to collect gene pair, and a dit for e-value collect
g_dit = {}
e_dit = {}

line = MCS.readline()

while(line):
        line_s = re.split(r'\s+', line)
        #print line_s
        if ('## Alignment' in line):
                check_n = 1
                A_scf = line_s[6].split('&')[0]
                B_scf = line_s[6].split('&')[1]
                pair = line_s[5].replace('N=', '')
                if ('minus' not in line):
                        B_orientation = '+'
                else:
                        B_orientation = '-'
                n = 0
        else:
        		if (check_n == 1):
		                if (re.search(r'A\.[A-Za-z0-9]*', line).group(0) in g_dit):
		                        if (float(line_s[-2]) < float(e_dit[re.search(r'A\.[A-Za-z0-9]*', line).group(0)])):
		                                g_dit[re.search(r'A\.[A-Za-z0-9]*', line).group(0)] = re.search(r'B\.[A-Za-z0-9]*', line).group(0)
		                                e_dit[re.search(r'A\.[A-Za-z0-9]*', line).group(0)] = line_s[-2]
		                else:
		                        g_dit[re.search(r'A\.[A-Za-z0-9]*', line).group(0)] = re.search(r'B\.[A-Za-z0-9]*', line).group(0)
		                        e_dit[re.search(r'A\.[A-Za-z0-9]*', line).group(0)] = line_s[-2]
		                n += 1
		                if (n == 1):
		                        A_start_gene = re.search(r'A\.[A-Za-z0-9]*', line).group(0)
		                        #print A_start_gene
		                        if (B_orientation == '+'):
		                                B_start_gene = re.search(r'B\.[A-Za-z0-9]*', line).group(0)
		                                #print B_start_gene
		                        else:
		                                B_end_gene = re.search(r'B\.[A-Za-z0-9]*', line).group(0)
		                                #print B_end_gene
		                if (n == int(pair)):
		                        A_end_gene = re.search(r'A\.[A-Za-z0-9]*', line).group(0)
		                        if (B_orientation == '+'):
		                                B_end_gene = re.search(r'B\.[A-Za-z0-9]*', line).group(0)
		                                #print B_end_gene
		                        else:
		                                B_start_gene = re.search(r'B\.[A-Za-z0-9]*', line).group(0)
		                                #print B_start_gene
		                        out_f.write(re_AB(A_scf)+'\t'+re_AB(A_start_gene)+'\t'+dit[A_start_gene][0]+'\t'+dit[A_start_gene][1]+'\t'+re_AB(A_end_gene)+'\t'+dit[A_end_gene][0]+'\t'+dit[A_end_gene][1]+'\t+\t'+str(abs(int(dit[A_start_gene][0])-int(dit[A_end_gene][1])))+'\t')
		                        out_f.write(re_AB(B_scf)+'\t'+re_AB(B_start_gene)+'\t'+dit[B_start_gene][0]+'\t'+dit[B_start_gene][1]+'\t'+re_AB(B_end_gene)+'\t'+dit[B_end_gene][0]+'\t'+dit[B_end_gene][1]+'\t'+B_orientation+'\t'+str(abs(int(dit[B_start_gene][0])-int(dit[B_end_gene][1])))+'\n')

        line = MCS.readline()
print 'tranformed.MCS is output!\n'

MCS.close()
out_f.close()

# output gene pair
for g in g_dit:
        out_f2.write(g + '\t' + g_dit[g] + '\n')

print 'gene pair is output!\n'
out_f2.close()
print 'All done!\n'

# last_v20170111
