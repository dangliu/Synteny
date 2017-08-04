#!/usr/bin/python

usage = """
Match gff of two species with  their blast file by gene order in scafffold,
usage:

python match.py spA.gene.gff spB.gene.gff out_blast.file

output:
out_blast.file.match_file

Written by Dang, Academia sinica, Jan 06, 2017.


"""

import sys, re

gff1 = open(sys.argv[1], 'r')
gff2 = open(sys.argv[2], 'r')

blast = open(sys.argv[3], 'r')

out_f = open(sys.argv[3] + '.match_file', 'w')



dit = {}
scf_l = []

line = gff1.readline()

while(line):
	line_s = re.split(r'\s+', line)
	scf = 'A.'+ line_s[0]
	gene = 'A.'+ re.sub(r'[A-Za-z]*:', '', line_s[8].split(';')[0]).replace('ID=', '')
	#print gene
	#print scf
	if (scf not in scf_l):
		scf_l.append(scf)
		n = 1
		dit[gene] = []
		dit[gene].append(scf)
		dit[gene].append(n)
	else:	
		n += 1
                dit[gene] = []
                dit[gene].append(scf)
                dit[gene].append(n)
	line = gff1.readline()

gff1.close()

#print dit


scf_l2 = []

line2 = gff2.readline()

while(line2):
	line2_s = re.split(r'\s+', line2)
	scf = 'B.'+ line2_s[0]
        gene = 'B.'+ re.sub(r'[A-Za-z]*:', '', line2_s[8].split(';')[0]).replace('ID=', '')
	#print gene
	#print scf
        if (scf not in scf_l2):
                scf_l2.append(scf)
                n = 1
                dit[gene] = []
                dit[gene].append(scf)
                dit[gene].append(n)
        else:
		n += 1
                dit[gene] = []
                dit[gene].append(scf)
                dit[gene].append(n)
	line2 = gff2.readline()

gff2.close()

#print dit

line3 = blast.readline()
while(line3):
	line3_s = re.split(r'\s+', line3)
	#print 'A.'+line3_s[0]
	#print 'B.'+line3_s[1]
	if ('A.'+line3_s[0] in dit and 'B.'+line3_s[1] in dit):
		out_f.write(dit['A.'+line3_s[0]][0] + '\tA.' + line3_s[0] + '\t' + str(dit['A.'+line3_s[0]][1]) + '\t' + str(dit['A.'+line3_s[0]][1]) + '\t' + dit['B.'+line3_s[1]][0] + '\tB.' + line3_s[1] + '\t' + str(dit['B.'+line3_s[1]][1]) + '\t' + str(dit['B.'+line3_s[1]][1]) + '\t' + str(line3_s[2]) + '\n')
	line3 = blast.readline()

blast.close()
out_f.close()

# last_v20170106
		


