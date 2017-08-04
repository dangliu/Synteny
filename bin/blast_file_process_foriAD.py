#!/usr/bin/python

import sys, re

SeqID = open(sys.argv[1], 'r')
blast = open(sys.argv[2], 'r')

out_f = open("out_" + sys.argv[2], 'w')



ID_dit = {}
line = SeqID.readline()

while(line):
        ID = line.split(':')[0]
        gene = line.split('|')[1]
        sp = re.split(r'\s+', line)[1].split('|')[0]
        ID_dit[ID] = gene
        line = SeqID.readline()
SeqID.close()

first = 0
check_n = 1
line2 = blast.readline()
while(line2):
        line2_s = re.split(r'\s+', line2)
        if (first == 0):
                last_g = line2_s[0]
                first = 1
        elif (line2_s[0] != last_g):
                last_g = line2_s[0]
                check_n = 1
        else:
                ''
        if (check_n <= 1):
                out_f.write('A.' + ID_dit[line2_s[0]] + '\t' + 'B.'+ ID_dit[line2_s[1]] + '\n')
                check_n += 1
        line2 = blast.readline()

blast.close()
out_f.close()

#last_v20170111
