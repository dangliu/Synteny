#!/usr/bin/python

# script to run k times for computing synteny coverage between Genome and N50 = n kb fragmented genome

usage = """

Run k times for computing synteny coverage between ref Genome and N50 = n kb fragmented qry genome,
usage:

python Run_k_times_iAD.py k n ref qry


Written by Dang, Academia sinica, July 26, 2017.


"""

import sys, re
import os
import subprocess
import time

if __name__ == "__main__":
	if len(sys.argv) < 5:
		print usage
		sys.exit( 0 ) 


# script path
dir_path = os.path.dirname(os.path.realpath(__file__))

# start time
startTime = time.time()

k = sys.argv[1]
n = sys.argv[2]
ref = sys.argv[3]
qry = sys.argv[4]
sp_list = ['CE', 'CBG', 'SR', 'SS']
if (ref not in sp_list or qry not in sp_list):
	print "please choose CE, CBG, SR or SS as species input"
	sys.exit( 0 )
ref_genome_len = subprocess.check_output("awk '{print $2}' ./data_source/genomes/" + ref + ".ref.fa.len.txt | paste -sd+ | bc", shell=True)
qry_genome_len = subprocess.check_output("awk '{print $2}' ./data_source/genomes/" + qry + ".ref.fa.len.txt | paste -sd+ | bc", shell=True)
run = 1
out_f = open(dir_path + '/SynCov/SynCov_iAD.' + str(n) + 'kb.' + ref + 'vs' + qry + '.txt', 'a')
out_f.write('run\tref\tqry\tN50\n')

for i in range(int(k)):
	print 'Run ' + str(run) + ' is running...'
	# to directory Genome
	os.chdir(dir_path + '/frag_assemblies/' + ref + 'vs' + qry + '/For_iAD')
	# Fragment Genome and make gene gff
	subprocess.call('cp -s ' + dir_path + '/data_source/genomes/' + qry + '.ref.fa.len.txt ./', shell=True)
	subprocess.call('python ' + dir_path + '/bin/Genome_cut.py ' + qry + '.ref.fa.len.txt ' + str(n) + '> cut.log', shell=True)
	#subprocess.call('../bin/bedtools2/bin/fastaFromBed -fi ../data_source/genomes/' + qry + '.genome.fa -bed ' + qry + '.ref.fa.len.txt.CutInto' + str(n) + 'kb.gff -fo ' + qry + '.CutInto' + str(n) + 'kb.fromGff.fa -name', shell=True)
	#subprocess.call('python ../bin/fasta_length.py ' + qry + '.CutInto' + str(n) + 'kb.fromGff.fa > ' + qry + '.CutInto' + str(n) + 'kb.fromGff.fa.len.txt', shell=True)	
	subprocess.call('python ' + dir_path + '/bin/GeneIntoFrag.py ' + qry + '.ref.fa.len.txt.CutInto' + str(n) + 'kb.gff ' + dir_path + '/data_source/gffs/' + qry + '.coding_gene.gff > ' + qry + '.' + str(n) + 'kb.coding_gene.gff', shell=True)
	# to directory iAD/RefvsQry
	os.chdir(dir_path + '/raw_process/iAD/' + ref + 'vs' + qry)
	subprocess.call('cp -s ' + dir_path + '/data_source/blasts/' + ref + 'vs' + qry + '.txt ./', shell=True)
	subprocess.call('python ' + dir_path + '/bin/blast_file_process_foriAD.py ' + ref + 'vs' + qry + '.txt', shell=True)
	subprocess.call('cp out_' + ref + 'vs' + qry + '.txt ./' + str(n) + 'kb.blast.txt', shell=True)
	subprocess.call('cp -s ' + dir_path + '/data_source/gffs/' + ref + '.coding_gene.gff ./', shell=True)
	subprocess.call('cp -s ' + dir_path + '/frag_assemblies/' + ref + 'vs' + qry + '/For_iAD/' + qry + '.' + str(n) + 'kb.coding_gene.gff ./', shell=True)
	# to sub directory for gff parsing
	subprocess.call('cp -s ' + dir_path + '/bin/gffs/gff_parse_foriAD.py ./', shell=True)
	subprocess.call('mkdir ' + qry + '_A_' + str(n) + 'kb', shell=True)
	subprocess.call('mkdir ' + ref + '_B', shell=True)
	os.chdir(dir_path + '/raw_process/iAD/' + ref + 'vs' + qry + '/' + ref + '_B')
	subprocess.call('python gff_parse_foriAD.py ../' + ref + '.coding_gene.gff  B.', shell=True)
	os.chdir(dir_path + '/raw_process/iAD/' + ref + 'vs' + qry + '/' + qry + '_A_' + str(n) + 'kb')
	subprocess.call('python gff_parse_foriAD.py ../' + qry + '.' + str(n) + 'kb.coding_gene.gff  A.', shell=True)
	# back to directory iAD/CEvsCE
	os.chdir(dir_path + '/raw_process/iAD/' + ref + 'vs' + qry)
	# make initial file
	out_intermediate = open(str(n) + 'kb.ini', 'w')
	out_intermediate.write('genome=  ' + qry + '_A_' + str(n) + 'kb\n')
	f = open(qry + '.' + str(n) + 'kb.coding_gene.gff.scf_list.txt')
	line = f.readline()
	while (line):
		out_intermediate.write(line)
		line = f.readline()
	f.close()
	out_intermediate.write('\n')
	out_intermediate.write('genome=  ' + ref + '_B')
	f = open(ref + '.coding_gene.gff.scf_list.txt')
	line = f.readline()
	while (line):
		out_intermediate.write(line)
		line = f.readline()
	f.close()
	out_intermediate.write('\n')
	out_intermediate.write('blast_table= ' + str(n) + 'kb.blast.txt\n')
	out_intermediate.write('\n')
	out_intermediate.write('output_path= ' + str(n) + 'kb_output\n')
	out_intermediate.write('\n')
	out_intermediate.write('cluster_type=colinear\nalignment_method=gg2\nmax_gaps_in_alignment=10\ntandem_gap=5\ngap_size=10\ncluster_gap=10\nq_value=0.9\nprob_cutoff=0.001\nanchor_points=5\nlevel_2_only=false\nnumber_of_threads=8\nvisualizeGHM=false\nvisualizeAlignment=false\nwrite_stats=true')
	out_intermediate.close()
	# run i-adhore
	subprocess.call(dir_path + '/bin/i-adhore-3.0.01/bin/i-adhore ' + str(n) + 'kb.ini >log 2> err', shell=True)
	# to sub directory
	os.chdir(dir_path + '/raw_process/iAD/' + ref + 'vs' + qry + '/' + str(n) + 'kb_output')
	subprocess.call('python ' + dir_path + '/bin/iAD_out_transform.py ' + dir_path + '/frag_assemblies/' + ref + 'vs' + qry + '/For_iAD/' + qry + '.' + str(n) + 'kb.coding_gene.gff ' + dir_path + '/data_source/gffs/' + ref + '.coding_gene.gff segments.txt', shell=True)
	subprocess.call('python ' + dir_path + '/bin/synteny_gff.py transformed.segments.txt A', shell=True)
	subprocess.call('cat A.transformed.segments.txt.int* > pre.' + str(n) + 'kb.synteny.gff', shell=True)
	subprocess.call('python ' + dir_path + '/bin/gff_sorting.py pre.' + str(n) + 'kb.synteny.gff > qry.' + str(n) + 'kb.synteny.gff', shell=True)
	subprocess.call(dir_path + '/bin/bedtools2/bin/bedtools merge -i qry.' + str(n) + 'kb.synteny.gff -c 4 -o count > qry.' + str(n) + 'kb.merge.bed', shell=True)
	#subprocess.call('python /mnt/nas1/dl/bin/python/bed2gff.py qry.' + str(n) + 'kb.merge.bed', shell=True)

	subprocess.call('python ' + dir_path + '/bin/synteny_gff.py transformed.segments.txt B', shell=True)
	subprocess.call('cat B.transformed.segments.txt.int* > pre.' + str(n) + 'kb.synteny.gff', shell=True)
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

# last_201700804            



