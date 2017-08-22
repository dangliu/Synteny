import sys, re



## protein_list
f1 = open(sys.argv[1], 'r')

g_list = []

line1 = f1.readline()

while(line1):
	line1_s = line1.split('|')
	gene = line1_s[1]
	g_list.append(gene)
	line1 = f1.readline()

f1.close()

## gff
f2 = open(sys.argv[2], 'r')

line2 = f2.readline()

while(line2):
	line2_s = re.split(r'\s+', line2)
	gene = re.sub(r'[A-Za-z]*:', '', line2_s[8].split(';')[0]).replace('ID=', '')
	if (gene in g_list):
		print line2.replace('\n', '')
	line2 = f2.readline()

f2.close()


# last_v20161216

