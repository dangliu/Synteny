#!/usr/bin/python

# script to run one time for computing synteny coverage between Genome and N50 = n kb fragmented genome

usage = """

Run one time for computing synteny coverage between ref Genome and N50 = n kb fragmented qry genome,
usage:

python Run_one_SyC.py k n ref qry


Written by Dang, Academia sinica, Aug 27, 2017.


"""

import sys, re
import os
import subprocess
import time

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print usage
		sys.exit( 0 ) 


# script path
dir_path = os.path.dirname(os.path.realpath(__file__))

# start time
startTime = time.time()

#k = sys.argv[1]
#n = sys.argv[2]
ref = sys.argv[1]
qry = sys.argv[2]
sp_list = ['CE', 'CBG', 'SR', 'SS']
sp_dict = {'CE':'c_elegans', 'CBG':'c_briggsae', 'SR':'s_ratti', 'SS':'s_stercoralis'}
if (ref not in sp_list or qry not in sp_list):
	print "please choose CE, CBG, SR or SS as species input"
	sys.exit( 0 )
ref_genome_len = subprocess.check_output("awk '{print $2}' ./data_source/genomes/" + ref + ".ref.fa.len.txt | paste -sd+ | bc", shell=True)
qry_genome_len = subprocess.check_output("awk '{print $2}' ./data_source/genomes/" + qry + ".ref.fa.len.txt | paste -sd+ | bc", shell=True)
run = 1
out_f = open(dir_path + '/SynCov/SynCov_SyC.' + str(n) + 'kb.' + ref + 'vs' + qry + '.txt', 'a')
out_f.write('run\tref\tqry\tN50\n')

subprocess.call('cp -rs ' + dir_path + '/bin/CHROnicle/ ' + dir_path + '/raw_process/SyC/', shell=True)

for i in range(int(k)):
	# reomve intermediate
	subprocess.call('rm -r ' + dir_path + '/raw_process/SyC/CHROnicle/' + ref + 'vs' + qry + '_' + str(n) + 'kb/01Genomes/A_*', shell=True)
	subprocess.call('rm -r ' + dir_path + '/raw_process/SyC/CHROnicle/' + ref + 'vs' + qry + '_' + str(n) + 'kb/10RBH', shell=True)
	subprocess.call('rm -r ' + dir_path + '/raw_process/SyC/CHROnicle/' + ref + 'vs' + qry + '_' + str(n) + 'kb/11Blocks', shell=True)
	print 'Run ' + str(run) + ' is running...'
	# to directory Genome
	#os.chdir(dir_path + '/frag_assemblies/' + ref + 'vs' + qry + '/For_SyC')
	# Fragment Genome and make gene gff
	#subprocess.call('cp -s ' + dir_path + '/data_source/genomes/' + qry + '.ref.fa.len.txt ./', shell=True)
	#subprocess.call('python ' + dir_path + '/bin/Genome_cut.py ' + qry + '.ref.fa.len.txt ' + str(n) + '> cut.log', shell=True)
	#subprocess.call('../bin/bedtools2/bin/fastaFromBed -fi ../data_source/genomes/' + qry + '.genome.fa -bed ' + qry + '.ref.fa.len.txt.CutInto' + str(n) + 'kb.gff -fo ' + qry + '.CutInto' + str(n) + 'kb.fromGff.fa -name', shell=True)
	#subprocess.call('python ../bin/fasta_length.py ' + qry + '.CutInto' + str(n) + 'kb.fromGff.fa > ' + qry + '.CutInto' + str(n) + 'kb.fromGff.fa.len.txt', shell=True)	
	#subprocess.call('python ' + dir_path + '/bin/GeneIntoFrag.py ' + qry + '.ref.fa.len.txt.CutInto' + str(n) + 'kb.gff ' + dir_path + '/data_source/gffs/' + qry + '.coding_gene.gff > ' + qry + '.' + str(n) + 'kb.coding_gene.gff', shell=True)
	# to sub directory in CHROnicle/
	os.chdir(dir_path + '/raw_process/SyC/CHROnicle')
	subprocess.call('mkdir ' + ref + 'vs' + qry + '_' + str(n) + 'kb', shell=True)
	os.chdir(dir_path + '/raw_process/SyC/CHROnicle/' + ref + 'vs' + qry + '_' + str(n) + 'kb')
	subprocess.call('mkdir 00rawGenom', shell=True)
	os.chdir(dir_path + '/raw_process/SyC/CHROnicle/' + ref + 'vs' + qry + '_' + str(n) + 'kb/00rawGenom')
	subprocess.call('mkdir A_' + qry, shell=True)
	subprocess.call('mkdir B_' + ref, shell=True)
	os.chdir(dir_path + '/raw_process/SyC/CHROnicle/' + ref + 'vs' + qry + '_' + str(n) + 'kb')
	# Parsing gff and fasta
	subprocess.call('cp ' + dir_path + '/frag_assemblies/' + ref + 'vs' + qry + '/fixed/' + qry + '.' + str(n) + 'kb.coding_gene.gff ./', shell=True)
	subprocess.call('cp -s ' + dir_path + '/data_source/genomes ' + sp_dict[qry] + '.fasta ./', shell=True)
	subprocess.call('python ' + dir_path + '/bin/fasta_process_forSynChr.py ' + qry + '.' + str(n) + 'kb.coding_gene.gff ' + sp_dict[qry] + '.fasta A.', shell=True)
	subprocess.call('mv ForSynChr.' + sp_dict[qry] + '.fasta A_' + qry + '.fasta', shell=True)
	subprocess.call('mv A_' + qry + '.fasta 00rawGenom/A_' + qry + '/', shell=True)
	subprocess.call('cp ' + dir_path + '/data_source/gffs/' + ref + '.coding_gene.gff ./', shell=True)
	subprocess.call('cp -s ' + dir_path + '/data_source/genomes ' + sp_dict[ref] + '.fasta ./', shell=True)
	subprocess.call('python ' + dir_path + '/bin/fasta_process_forSynChr.py ' + ref + '.coding_gene.gff ' + sp_dict[ref] + '.fasta B.', shell=True)
	subprocess.call('mv ForSynChr.' + sp_dict[ref] + '.fasta B_' + ref + '.fasta', shell=True)
	subprocess.call('mv B_' + ref + '.fasta 00rawGenom/B_' + ref + '/', shell=True)
	# to directory in CHROnicle/Programs/0Convert2InputF
	os.chdir(dir_path + '/raw_process/SyC/CHROnicle/Programs/0Convert2InputF')
	subprocess.call('./ConvertFasta.py ' + ref + 'vs' + qry + '_' + str(n) + 'kb A_' + qry + ' A_' + qry + ' 1 3 4 5 6 0', shell=True)
	subprocess.call('./ConvertFasta.py ' + ref + 'vs' + qry + '_' + str(n) + 'kb B_' + ref + ' B_' + ref + ' 1 3 4 5 6 0', shell=True)
	# to directory in CHROnicle/Programs/1SynChro
	# run SyC
	os.chdir(dir_path + '/raw_process/SyC/CHROnicle/Programs/1SynChro')
	subprocess.call('./SynChro.py ' + ref + 'vs' + qry + '_' + str(n) + 'kb 0 6', shell=True)
	# to output directory
	os.chdir(dir_path + '/raw_process/SyC/CHROnicle/' + ref + 'vs' + qry + '_' + str(n) + 'kb/11Blocks/Delta6/OrthBlocks')
	subprocess.call('python ' + dir_path + '/bin/SyC_out_transform.py ' + dir_path + '/frag_assemblies/' + ref + 'vs' + qry + '/fixed/' + qry + '.' + str(n) + 'kb.coding_gene.gff ' + dir_path + '/data_source/gffs/' + ref + '.coding_gene.gff A_' + qry + '.B_' + ref + '.orth.synt.start_end', shell=True)
	# transforming output format and making synteny gff
	subprocess.call('python ' + dir_path + '/bin/synteny_gff.py transformed.A_' + qry + '.B_' + ref + '.orth.synt.start_end A', shell=True)
	subprocess.call('cat A.transformed.A_' + qry + '.B_' + ref + '.orth.synt.start_end.int* > pre.' + str(n) + 'kb.synteny.gff', shell=True)
	subprocess.call('python ' + dir_path + '/bin/gff_sorting.py pre.' + str(n) + 'kb.synteny.gff > qry.' + str(n) + 'kb.synteny.gff', shell=True)
	subprocess.call(dir_path + '/bin/bedtools2/bin/bedtools merge -i qry.' + str(n) + 'kb.synteny.gff -c 4 -o count > qry.' + str(n) + 'kb.merge.bed', shell=True)
	#subprocess.call('python /mnt/nas1/dl/bin/python/bed2gff.py qry.' + str(n) + 'kb.merge.bed', shell=True)

	subprocess.call('python ' + dir_path + '/bin/synteny_gff.py transformed.A_' + qry + '.B_' + ref + '.orth.synt.start_end B', shell=True)
	subprocess.call('cat B.transformed.A_' + qry + '.B_' + ref + '.orth.synt.start_end.int* > pre.' + str(n) + 'kb.synteny.gff', shell=True)
	subprocess.call('python ' + dir_path + '/bin/gff_sorting.py pre.' + str(n) + 'kb.synteny.gff > ref.' + str(n) + 'kb.synteny.gff', shell=True)
	subprocess.call(dir_path + '/bin/bedtools2/bin/bedtools merge -i ref.' + str(n) + 'kb.synteny.gff -c 4 -o count > ref.' + str(n) + 'kb.merge.bed', shell=True)
	#subprocess.call('python /mnt/nas1/dl/bin/python/bed2gff.py ref.' + str(n) + 'kb.merge.bed', shell=True)

	# extract result, compute synteny coverage
	qry_len = subprocess.check_output("awk '{print $3-$2}' qry." + str(n) + "kb.merge.bed | paste -sd+ | bc", shell=True)
	ref_len = subprocess.check_output("awk '{print $3-$2}' ref." + str(n) + "kb.merge.bed | paste -sd+ | bc", shell=True)
	# output
	out_f.write(str(run) + '\t' + "%.4f" %(float(ref_len)/float(ref_genome_len)) + '\t' + "%.4f" %(float(qry_len)/float(qry_genome_len)) + '\t' + str(n) + '\n')
	run += 1

print "All done!"
# the spent time
elapsed = time.time() - startTime
print 'It spends', elapsed, 'seconds'

# last_20170827



