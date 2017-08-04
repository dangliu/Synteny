# input1: transformed_DAGoutpt
# input2: A (for first species) or B (for second species)
# output: systeny.gff


import sys, re

f = open(sys.argv[1], 'r')
out_f = open(sys.argv[2] + '.' + sys.argv[1] + '.intra' + '.gff', 'w')
out_f2 = open(sys.argv[2] + '.' + sys.argv[1] + '.inter' + '.gff', 'w')

# add vs_start_gene (20161024)

if (sys.argv[2] == "A"):
        line = f.readline()
        while(line):
                line_s = re.split(r'\s+', line)
                scf = line_s[0]
                chromosome = line_s[0]
                vs_chr = line_s[9]
                orient = line_s[16]
                start = line_s[2]
                end = line_s[6]
                start_g = line_s[1]
                vs_start_g = line_s[10]
                end_g = line_s[4]
                if (chromosome == vs_chr):
                        out_f.write(scf+'\tDAGchainer\tblock\t'+start+'\t'+end+'\t.\t'+orient+'\t.\t'+'ID_s='+start_g+';ID_e='+end_g+';chr='+chromosome+';vs_s='+vs_start_g+';vs_chr='+vs_chr+'\n')
                else:
                        out_f2.write(scf+'\tDAGchainer\tblock\t'+start+'\t'+end+'\t.\t'+orient+'\t.\t'+'ID_s='+start_g+';ID_e='+end_g+';chr='+chromosome+';vs_s='+vs_start_g+';vs_chr='+vs_chr+'\n')
                line = f.readline()
else:
        line = f.readline()
        while(line):
                line_s = re.split(r'\s+', line)
                scf = line_s[9]
                chromosome = line_s[9]
                vs_chr = line_s[0]
                orient = line_s[16]
                start = line_s[11]
                end = line_s[15]
                start_g = line_s[10]
                vs_start_g = line_s[1]
                end_g = line_s[13]
                if (chromosome == vs_chr):
                        out_f.write(scf+'\tDAGchainer\tblock\t'+start+'\t'+end+'\t.\t'+orient+'\t.\t'+'ID_s='+start_g+';ID_e='+end_g+';chr='+chromosome+';vs_s='+vs_start_g+';vs_chr='+vs_chr+'\n')
                else:
                        out_f2.write(scf+'\tDAGchainer\tblock\t'+start+'\t'+end+'\t.\t'+orient+'\t.\t'+'ID_s='+start_g+';ID_e='+end_g+';chr='+chromosome+';vs_s='+vs_start_g+';vs_chr='+vs_chr+'\n')
                line = f.readline()
f.close()
out_f.close()
out_f2.close()
# last_v20161024
