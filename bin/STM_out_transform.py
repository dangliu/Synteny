#!/usr/bin/python

# a script for transforming sastuma output to a my synteny output form
# format:
#[A_scf]<tab>[block_strat_gene]<tab>[gene_start]<tab>[gene_end]<tab>[block_end_gene]<tab>[gene_start]<tab>[gene_end]<tab>[+]<tab>[block_length]
#+
#[B_scf]<tab>[block_strat_gene]<tab>[gene_start]<tab>[gene_end]<tab>[block_end_gene]<tab>[gene_start]<tab>[gene_end]<tab>[+/-]<tab>[block_length]
# input argv[1]: satsuma_summary.chained.out
# output1: transformed.STM_out



usage = """
Arrange satsuma output to my synteny output format,
usage:

python STM_out_transform.py satsuma_summary.chained.out


Written by Dang, Academia sinica, Oct 22, 2017.


"""


import sys, re

if __name__ == "__main__":
        if len(sys.argv) < 2:
                print usage
                sys.exit( 0 ) 


STM = open(sys.argv[1], 'r')

out_f = open('transformed.' + sys.argv[1], 'w')



line = STM.readline()

while(line):
        line_s = re.split(r'\s+', line)
        A_scf = line_s[3]
        B_scf = line_s[0]
        orientation = line_s[7].replace('\n', '')
        A_start_gene = 'A_start_site'
        A_end_gene = 'A_end_site'
        B_start_gene = 'B_start_site'
        B_end_gene = 'B_end_site'
        A_start = line_s[4]
        # modify for start site for bedtools
        if (int(A_start) == 0):
            A_start = '1'
        A_end = line_s[5]
        B_start = line_s[1]
        if (int(B_start) == 0):
            B_start = '1'
        B_end = line_s[2]                        
        out_f.write(A_scf+'\t'+A_start_gene+'\t'+A_start+'\t'+A_start+'\t'+A_end_gene+'\t'+A_end+'\t'+A_end+'\t+\t'+str(abs(int(A_start)-int(A_end)))+'\t')
        out_f.write(B_scf+'\t'+B_start_gene+'\t'+B_start+'\t'+B_start+'\t'+B_end_gene+'\t'+B_end+'\t'+B_end+'\t'+orientation+'\t'+str(abs(int(B_start)-int(B_end)))+'\n')
        line = STM.readline()
print 'tranformed.STM is output!\n'

STM.close()
out_f.close()


print 'All done!\n'

# last_v20171022
