# Synteny

## prerequisite:
## Species data source
- species data source can be downloaded from WormBase ftp://ftp.wormbase.org/pub/wormbase/
- WS255 for C. elegans and C. briggsae
- WBPS8 for S. ratti and S. stercoralis
## Programs to be downloaded and inatalled in /bin 
- BEDtools https://github.com/arq5x/bedtools2/releases/download/v2.26.0/bedtools-2.26.0.tar.gz
- DAGchainer https://downloads.sourceforge.net/project/dagchainer/dagchainer/DAGchainer-r02062008/DAGchainer_r02-06-2008.tar.gz
- i-ADHoRe http://bioinformatics.psb.ugent.be/webtools/i-adhore/licensing/
- MCScanX http://chibba.pgml.uga.edu/mcscan2/MCScanX.zip
- SynChro http://www.lcqb.upmc.fr/CHROnicle/telechargements/CHROnicle.zip
- Orthofinder https://github.com/davidemms/OrthoFinder/releases/download/1.1.2/OrthoFinder-1.1.2.tar.gz
- Circos http://circos.ca/distribution/circos-0.69-4.tgz
## Process for the figures
1. Figure 2.
- un-fragmented
	- raw data
	- synteny process
	- synteny coverage
	- extract data
	- circos

- 1Mb
	- fragmentation process once
	- synteny process
	- synteny coverage
	- extract data
	- circos

- 100kb
	- fragmentation process once
	- synteny process
	- synteny coverage
	- extract data
	- circos

2. Figure 4.
- CEvsCE
	- fragmentation process & synteny coverage extraction
	- R box plot

- CEvsCBG
	- fragmentation process & synteny coverage extraction
	- R box plot

- SRvsSR
	- fragmentation process & synteny coverage extraction
	- R box plot

- SRvsSS
	- fragmentation process & synteny coverage extraction
	- R box plot

3. Figure 5.
- CEvsCBG
	- fragmentation process & GO extraction
	- R pheatmap

4. Figure 6.
- CEvsCBG
	- fragmentation once
	- ALLMAPs
	- synteny (original and ALLMAPs)
	- synteny coverage
	- R dot plot 

- SRvsSS
	- fragmentation once
	- ALLMAPs
	- synteny (original and ALLMAPs)
	- synteny coverage
	- R dot plot

5. Figure 7.
- CEvsCBG
	- fragmentation once
	- ALLMAPs
	- synteny (original and ALLMAPs)
	- data extraction
	- R segment & polygon
