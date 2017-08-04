#!/usr/bin/python

usage = """
Parse scf-sorted gff for i-ADHoRe input.
usage:

python gff_parse_foriAD.py gene.gff tag

output:
scf#.lst scf#.lst scf#.lst ...... (depends on how many scaffolds)
scf_list.txt

Written by Dang, Academia sinica, Jan 13, 2017.


"""

import sys, re
import os 


if __name__ == "__main__":
        if len(sys.argv) < 3:
                print usage
                sys.exit( 0 ) 

gff = open(sys.argv[1], 'r')
out_list = open(sys.argv[1] + '.scf_list.txt', 'w')
dir_path = os.path.dirname(os.path.realpath(__file__)) 
tag = sys.argv[2]

first = 0

line = gff.readline()

while(line):
        line_s = re.split(r'\s+', line)
        scf = line_s[0]
        gene = tag + re.sub(r'[A-Za-z]*:', '', line_s[8].split(';')[0]).replace('ID=', '')
        strand = line_s[6]
        #print gene
        #print scf
        if (first == 0):
                out_list.write(tag + scf + ' ' + dir_path + '/' + tag + scf + '.lst' + '\n')
                out_f = open(tag + scf + '.lst', 'w')
                out_f.write(gene + strand + '\n')
                last_scf = scf
                first = 1
        elif (scf != last_scf):
                out_list.write(tag + scf + ' ' + dir_path + '/' + tag + scf + '.lst' + '\n')
                out_f.close()
                out_f = open(tag + scf + '.lst', 'w')
                out_f.write(gene + strand + '\n')
                last_scf = scf
        else:
                out_f.write(gene + strand + '\n')
        line = gff.readline()

gff.close()
out_f.close()
out_list.close()

# last_v20170113
