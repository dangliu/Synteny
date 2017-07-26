#!/usr/bin/python
# A script to calculate fasta file scaffolds/proteins length

usage = """

A script to calculate fasta file scaffolds/proteins length,
usage:

python fasta_length.py fasta 


Written by Dang, Academia sinica, June 28, 2017.


"""

import sys, re

scaffold = open(sys.argv[1], 'r')


s_dit = {}

n = 0

line_s = scaffold.readline()

while(line_s):
		line_r = line_s.replace('\n', '')
		if ('>' in line_s):
				n += 1
				scf_id = line_r.replace('>', '')
				s_dit[n] = []
				s_dit[n].append(scf_id)
				s_dit[n].append(0)
		else:
				s_dit[n][1] += len(line_r)
		line_s = scaffold.readline()

scaffold.close()


for n in s_dit:
	print s_dit[n][0] + "\t" + str(s_dit[n][1])

# last_v20170628
