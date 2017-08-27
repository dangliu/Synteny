# Run in Rstudio

library('reshape2')
library('pheatmap')
library('RColorBrewer')

## input file should include three columns: 
## scaffold of specie1, scaffold of specie2, counts
## Their names are not necessarily labeled, as they will be added with this script
file<-'/Users/dangliu/Desktop/JT_lab/Synteny/GO_test/qry.100kb.BeforeAfter.1-1.txt'
#file<-'/Users/dangliu/Desktop/JT_lab/C.sp/1to1/c_angaria-c_sp34.1-1.txt'
#file<-'/Users/dangliu/Desktop/JT_lab/C.sp/1to1/c_angaria-c_briggsae.1-1.txt'
df<- read.table(file, header = FALSE, sep='\t')
colnames(df)<- c('scaf1', 'scaf2', 'counts')
df.mat<- dcast(df, scaf1~scaf2)
rownames(df.mat)<- df.mat[,'scaf1']
df.mat$scaf1<-NULL
df.mat<-as.matrix(df.mat)

## filters for removing rows or columns with too few counts
row.min<-0 # number is arbitrary
col.min<-0
df.mat<-df.mat[,colSums(df.mat)>col.min]
df.mat<-df.mat[rowSums(df.mat)>row.min,]
## order row and column
cn <- c('B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B14','B15','B16','B17','B25','B26')
rn <- c('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A>10')
## normalization
norm.df.mat<- df.mat
n<-0
while (n<nrow(df.mat)) {# normalize by row
  n<- n+1
  norm.df.mat[n,]<-norm.df.mat[n,]/max(norm.df.mat[n,])
}
res <- pheatmap(
#   filename= '', ## the plot cannot be saved with ggsave
#   change the color of cells, border, or add labels
    color = colorRampPalette((brewer.pal(n = 4, name ="Reds")))(100),
    fontsize_number = 12,
    fontsize_row = 12,
    fontsize_col = 12,
    cellwidth = 30,
    cellheight = 30,
    as.matrix(norm.df.mat[cn,rn]),
    display_numbers = as.matrix(df.mat[cn,rn]),
    cluster_rows = FALSE, cluster_cols = FALSE
)

#scf.clust <- cbind(norm.df.mat, 
#                      cluster = cutree(res$tree_row, 
#                                       k = 6))
#View(scf.clust)

#write.table(scf.clust, file="/Users/dangliu/Desktop/JT_lab/C.sp/cluster/c_angaria-c_elegans.cluster.txt", sep="\t")
#write.table(scf.clust, file="/Users/dangliu/Desktop/JT_lab/C.sp/cluster/c_angaria-c_sp34.cluster.txt", sep="\t")
#write.table(scf.clust, file="/Users/dangliu/Desktop/JT_lab/C.sp/cluster/c_angaria-c_briggsae.cluster.txt", sep="\t")

#last_v20161214
