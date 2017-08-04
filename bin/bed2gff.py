# input:  bed file
# output: gff

import sys, re

# human sorting
# sort numbers in string
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

f = open(sys.argv[1], 'r')
out_f = open(sys.argv[1] + '.gff', 'w')

dit = {}
dit2 = {}

line = f.readline()

while(line):
        line_s = re.split(r'\s+', line)
        scf = line_s[0]
        start = str(int(line_s[1])+1)
        end = line_s[2]
        if (scf not in dit):
                dit[scf] = {}
                dit[scf][start] = []
                dit[scf][start].append(end)
        else:
                dit[scf][start] = []
                dit[scf][start].append(end)
        line = f.readline()

for x in dit:
        sort = sorted(dit[x], key=int)
        dit2[x] = sort

#print dit2

sort_chr_l = sorted(dit2, key=natural_keys)

# output
for x in sort_chr_l:
        for i in dit2[x]:
                out_f.write(x+'\tbed\tregion\t'+i+'\t'+dit[x][i][0]+'\t.\t+\t.\t'+'ID=NA;Derives_from=bedtools'+'\n')


f.close()
out_f.close()

# last_v20161221
