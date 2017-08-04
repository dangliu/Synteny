#!/usr/bin/python
# input: gff
# output: gff sorted by Chr then Start

usage = """
Sort the gff.
usage:

python gff_sorting.py gff

Written by Dang, Academia sinica, Feb 09, 2017.


"""


import sys, re

if __name__ == "__main__":
        if len(sys.argv) < 2:
                print usage
                sys.exit( 0 )

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

# two dit, dit1 for input gff info saving, dit2 for sorted info saving
dit = {}
dit2 = {}

check_n = 0 # deal with case that there is gene with same start

line = f.readline()
while(line):
        line_s = re.split(r'\s+', line)
        scf = line_s[0]
        source = line_s[1]
        feature = line_s[2]
        start = line_s[3]
        end = line_s[4]
        score = line_s[5]
        orient = line_s[6]
        frame = line_s[7]
        info = line_s[8]
        if (scf not in dit):
                dit[scf] = {}
                dit[scf][start] = []
                dit[scf][start].append(end)
                dit[scf][start].append(orient)
                dit[scf][start].append(info)
                dit[scf][start].append(source)
                dit[scf][start].append(feature)
                dit[scf][start].append(score)
                dit[scf][start].append(frame)
        else:
                if (start in dit[scf]): # deal with case that there is gene with same start # if use int to add, you will encount a sort probelm when check_n getting bigger
                        check_n += 1
                        dit[scf][start+'.'+str(check_n)] = []
                        dit[scf][start+'.'+str(check_n)].append(end)
                        dit[scf][start+'.'+str(check_n)].append(orient)
                        dit[scf][start+'.'+str(check_n)].append(info + ';check_n=' + str(check_n))
                        dit[scf][start+'.'+str(check_n)].append(source)
                        dit[scf][start+'.'+str(check_n)].append(feature)
                        dit[scf][start+'.'+str(check_n)].append(score)
                        dit[scf][start+'.'+str(check_n)].append(frame)   
                else:   
                        dit[scf][start] = []
                        dit[scf][start].append(end)
                        dit[scf][start].append(orient)
                        dit[scf][start].append(info)
                        dit[scf][start].append(source)
                        dit[scf][start].append(feature)
                        dit[scf][start].append(score)
                        dit[scf][start].append(frame)
        line = f.readline()

for x in dit:
        sort = sorted(dit[x], key=natural_keys)
        dit2[x] = sort

#print dit2
#CE_chr_l = ['I', 'II', 'III', 'IV', 'V', 'X']
sort_chr_l = sorted(dit2, key=natural_keys)

# output
#for x in CE_chr_l:
#       for i in dit2[x]:
#               print x+'\tDAGchainer\tblock\t'+i+'\t'+dit[x][i][0]+'\t.\t'+dit[x][i][1]+'\t.\t'+dit[x][i][2]
for x in sort_chr_l:
        for i in dit2[x]:
                if (re.search(r'check_n', dit[x][i][2])): # deal with case that there is gene with same start
                        print x+'\t'+dit[x][i][3]+'\t'+dit[x][i][4]+'\t'+i.replace('.' + dit[x][i][2].split(';')[-1].replace('check_n=',''), '')+'\t'+dit[x][i][0]+'\t'+dit[x][i][5]+'\t'+dit[x][i][1]+'\t'+dit[x][i][6]+'\t'+dit[x][i][2]
                else:
                        print x+'\t'+dit[x][i][3]+'\t'+dit[x][i][4]+'\t'+i+'\t'+dit[x][i][0]+'\t'+dit[x][i][5]+'\t'+dit[x][i][1]+'\t'+dit[x][i][6]+'\t'+dit[x][i][2]


f.close()
# last_v20170209
# deal with highly repetitive gff
