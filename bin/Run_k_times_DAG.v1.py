#!/usr/bin/python

# script to run k times for computing synteny coverage between Genome and N50 = n kb fragmented genome

usage = """

Run k times for computing synteny coverage between ref Genome and N50 = n kb fragmented qry genome,
usage:

python Run_k_times_DAG.py k n ref qry


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
out_f = open(dir_path + '/SynCov/SynCov_DAG.' + str(n) + 'kb.' + ref + 'vs' + qry + '.txt', 'a')
out_f.write('run\tref\tqry\tN50\n')

for i in range(int(k)):
	print 'Run ' + str(run) + ' is running...'
	# to directory Genome
	os.chdir(dir_path + '/frag_assemblies/' + ref + 'vs' + qry + '/For_DAG')
	# Fragment Genome and make gene gff
	subprocess.call('cp -s ' + dir_path + '/data_source/genomes/' + qry + '.ref.fa.len.txt ./', shell=True)
	subprocess.call('python ' + dir_path + '/bin/Genome_cut.py ' + qry + '.ref.fa.len.txt ' + str(n) + '> cut.log', shell=True)
	#subprocess.call('../bin/bedtools2/bin/fastaFromBed -fi ../data_source/genomes/' + qry + '.genome.fa -bed ' + qry + '.ref.fa.len.txt.CutInto' + str(n) + 'kb.gff -fo ' + qry + '.CutInto' + str(n) + 'kb.fromGff.fa -name', shell=True)
	#subprocess.call('python ../bin/fasta_length.py ' + qry + '.CutInto' + str(n) + 'kb.fromGff.fa > ' + qry + '.CutInto' + str(n) + 'kb.fromGff.fa.len.txt', shell=True)	
	subprocess.call('python ' + dir_path + '/bin/GeneIntoFrag.py ' + qry + '.ref.fa.len.txt.CutInto' + str(n) + 'kb.gff ' + dir_path + '/data_source/gffs/' + qry + '.coding_gene.gff > ' + qry + '.' + str(n) + 'kb.coding_gene.gff', shell=True)
	# to directory DAG/RefvsQry
	os.chdir(dir_path + '/raw_process/DAG/' + ref + 'vs' + qry)
	# run DAG, make synteny gff and make merge gff
	subprocess.call('cp -s ' + dir_path + '/data_source/blasts/' + ref + 'vs' + qry + '.txt ./', shell=True)
	subprocess.call('python ' + dir_path + '/bin/blast_file_process_forDAG.py ' + ref + 'vs' + qry + '.txt', shell=True)
	subprocess.call('cp out_' + ref + 'vs' + qry + '.txt ./' + str(n) + 'kb.blast.txt', shell=True)
	subprocess.call('python ' + dir_path + '/bin/match_forDAG.py ' + dir_path + '/frag_assemblies/' + ref + 'vs' + qry + '/For_DAG/' + qry + '.' + str(n) + 'kb.coding_gene.gff ' + dir_path + '/data_source/gffs/' + ref + '.coding_gene.gff ' + str(n) + 'kb.blast.txt', shell=True)
	# run_process include:
	subprocess.call('perl ' + dir_path + '/bin/DAGCHAINER/accessory_scripts/filter_repetitive_matches.pl 5 < ' + str(n) + 'kb.blast.txt.match_file > ' + str(n) + 'kb.blast.txt.match_file.filtered', shell=True)
	subprocess.call(dir_path + '/bin/DAGCHAINER/run_DAG_chainer.pl -i  ' + str(n) + 'kb.blast.txt.match_file.filtered -Z 12 -D 10 -g 1 -A 5 > DAG.log', shell=True)
	subprocess.call('python ' + dir_path + '/bin/DAG_out_transform.py ' + dir_path + '/frag_assemblies/' + ref + 'vs' + qry + '/For_DAG/' + qry + '.' + str(n) + 'kb.coding_gene.gff ' + dir_path + '/data_source/gffs/' + ref + '.coding_gene.gff ' + str(n) + 'kb.blast.txt.match_file.filtered.aligncoords', shell=True)
	
	subprocess.call('python ' + dir_path + '/bin/synteny_gff.py transformed.' + str(n) + 'kb.blast.txt.match_file.filtered.aligncoords A', shell=True)
	subprocess.call('cat A.transformed.' + str(n) + 'kb.blast.txt.match_file.filtered.aligncoords.int* > pre.' + str(n) + 'kb.synteny.gff', shell=True)
	subprocess.call('python ' + dir_path + '/bin/gff_sorting.py pre.' + str(n) + 'kb.synteny.gff > qry.' + str(n) + 'kb.synteny.gff', shell=True)
	subprocess.call(dir_path + '/bin/bedtools2/bin/bedtools merge -i qry.' + str(n) + 'kb.synteny.gff -c 4 -o count > qry.' + str(n) + 'kb.merge.bed', shell=True)
	subprocess.call('python ' + dir_path + '/bin/bed2gff.py qry.' + str(n) + 'kb.merge.bed', shell=True)

	subprocess.call('python ' + dir_path + '/bin/synteny_gff.py transformed.' + str(n) + 'kb.blast.txt.match_file.filtered.aligncoords B', shell=True)
	subprocess.call('cat B.transformed.' + str(n) + 'kb.blast.txt.match_file.filtered.aligncoords.int* > pre.' + str(n) + 'kb.synteny.gff', shell=True)
	subprocess.call('python ' + dir_path + '/bin/gff_sorting.py pre.' + str(n) + 'kb.synteny.gff > ref.' + str(n) + 'kb.synteny.gff', shell=True)
	subprocess.call(dir_path + '/bin/bedtools2/bin/bedtools merge -i ref.' + str(n) + 'kb.synteny.gff -c 4 -o count > ref.' + str(n) + 'kb.merge.bed', shell=True)
	subprocess.call('python ' + dir_path + '/bin/bed2gff.py ref.' + str(n) + 'kb.merge.bed', shell=True)

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

# last_20170804




