import sys, re
fh = open(sys.argv[1], 'r')
line = fh.readline()

#make species name
input_name_split = sys.argv[1].split(".")
species_name = input_name_split[0]

#be careful not to rewrite the input
out_fh = open(species_name + ".fasta", 'w')

# adress first line
# split to get the gene name
split_line = re.split(r'\s+', line.replace('>', ''))
#print split_line
#print ">" + split_line[1] + "\n"
lastgene = split_line[2]
CDS = split_line[2] + "|" + split_line[0]
# set some start value
seq = ''
seq_length = 0
dit_seq = {}
dit_length ={}
dit_id = {}
line = fh.readline()
# while loop to read line
# use if to seperate genes
while(line):
	if (">" in line):
		clean_seq = seq.replace('\n', '')
		if (lastgene in dit_length):
			if (dit_length[lastgene] < seq_length):      # get the longest one in the same gene key 
				dit_seq[lastgene] = clean_seq
				dit_length[lastgene] = seq_length
				dit_id[lastgene] = CDS
		else:
			dit_seq[lastgene] = clean_seq
			dit_length[lastgene] = seq_length
			dit_id[lastgene] = CDS

		#print clean_seq + '\n'
		#print str(seq_length) + '\n' 
		split_line = re.split(r'\s+', line.replace('>', ''))
		#print ">" + split_line[1] + "\n"
		lastgene = split_line[2]
		CDS = split_line[2] + "|" + split_line[0]
		seq = ''
		seq_length = 0
	else:
		line_length = len(line.replace('\n', ''))
		seq_length += line_length
		seq += line
	line = fh.readline()
clean_seq = seq.replace('\n', '')
if (lastgene in dit_length):
	if (dit_length[lastgene] < seq_length):      # get the longest one in the same gene key 
		dit_seq[lastgene] = clean_seq
		dit_length[lastgene] = seq_length
		dit_id[lastgene] = CDS
else:
	dit_seq[lastgene] = clean_seq
	dit_length[lastgene] = seq_length
	dit_id[lastgene] = CDS
#print clean_seq + '\n'
#print str(seq_length) + '\n' 


#print dit_seq
#print dit_length
#print dit_length['g64']
#print dit_length['g75']
count = 0
for char in dit_seq:
	count += 1
	#print ">" + char + "\n"
	out_fh.write(">" + species_name + "|" + dit_id[char] + "\n")
	#print dit_seq[char] + "\n"
	out_fh.write(dit_seq[char] + "\n")

#print len(dit_seq)
#print count
#print dit_seq['g64']
#print dit_seq['g75']

fh.close()
out_fh.close()

# last_v20160418
