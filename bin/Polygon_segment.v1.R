## Run in Rstudio

## inputs
#t<- read.table('/Users/dangliu/Desktop/JT_lab/Synteny/allmaps/seg_case/CEvsCBG/Tag.trans.DAG.allmaps.out.link')
#t2<- read.table('/Users/dangliu/Desktop/JT_lab/Synteny/allmaps/seg_case/CEvsCBG/Tag.trans.DAG.original.out.link')
#t<- read.table('/Users/dangliu/Desktop/JT_lab/Synteny/allmaps/seg_case/CEvsCBG/Tag.trans.iAD.allmaps.out.link')
#t2<- read.table('/Users/dangliu/Desktop/JT_lab/Synteny/allmaps/seg_case/CEvsCBG/Tag.trans.iAD.original.out.link')
#t<- read.table('/Users/dangliu/Desktop/JT_lab/Synteny/allmaps/seg_case/CEvsCBG/Tag.trans.MCS.allmaps.out.link')
#t2<- read.table('/Users/dangliu/Desktop/JT_lab/Synteny/allmaps/seg_case/CEvsCBG/Tag.trans.MCS.original.out.link')
t<- read.table('/Users/dangliu/Desktop/JT_lab/Synteny/allmaps/seg_case/CEvsCBG/Tag.trans.SyC.allmaps.out.link')
t2<- read.table('/Users/dangliu/Desktop/JT_lab/Synteny/allmaps/seg_case/CEvsCBG/Tag.trans.SyC.original.out.link')
names(t) <- c("A_chr", "A_start_g", "A_start", "A_end_g", "A_end", "B_chr", "B_start_g", "B_start", "B_end_g", "B_end")
names(t2) <- c("C_chr", "C_start_g", "C_start", "C_end_g", "C_end", "B_chr", "B_start_g", "B_start", "B_end_g", "B_end")

## chrI
#B.scaffolds<- c('CE.I')
#A.scaffolds<- c('CBG.allmaps.I')
#C.scaffolds<- c('CBG.I')
## chrII (flip)
#B.scaffolds<- c('CE.II')
#A.scaffolds<- c('CBG.allmaps.II')
#C.scaffolds<- c('CBG.II')
## chr III
#B.scaffolds<- c('CE.III')
#A.scaffolds<- c('CBG.allmaps.III')
#C.scaffolds<- c('CBG.III')
## chr IV (flip)
#B.scaffolds<- c('CE.IV')
#A.scaffolds<- c('CBG.allmaps.IV')
#C.scaffolds<- c('CBG.IV')
## chr V
#B.scaffolds<- c('CE.V')
#A.scaffolds<- c('CBG.allmaps.V')
#C.scaffolds<- c('CBG.V')
## chr X
B.scaffolds<- c('CE.X')
A.scaffolds<- c('CBG.allmaps.X')
C.scaffolds<- c('CBG.X')

A.l<- read.table('/Users/dangliu/Desktop/JT_lab/Synteny/allmaps/seg_case/CEvsCBG/Tag.briggsae.allmaps.len.txt', header= FALSE, sep= "\t")
B.l<- read.table('/Users/dangliu/Desktop/JT_lab/Synteny/allmaps/seg_case/CEvsCBG/tag.elegans.len.txt', header= FALSE, sep= "\t")
C.l<- read.table('/Users/dangliu/Desktop/JT_lab/Synteny/allmaps/seg_case/CEvsCBG/tag.briggsae.len.txt', header= FALSE, sep= "\t")


colnames(A.l)<- c('scf', 'length')
rownames(A.l)<- A.l$scf
A.l$scf<- NULL
colnames(B.l)<- c('scf', 'length')
rownames(B.l)<- B.l$scf
B.l$scf<- NULL
colnames(C.l)<- c('scf', 'length')
rownames(C.l)<- C.l$scf
C.l$scf<- NULL


# extract chr use %in% to match
sub.t<- t[t$A_chr%in%A.scaffolds, ]
sub.t<- sub.t[sub.t$B_chr%in%B.scaffolds, ]
sub.t2<- t2[t2$B_chr%in%B.scaffolds, ]
sub.t2<- sub.t2[sub.t2$C_chr%in%C.scaffolds, ]
## compute the line dimensions
# if only one scf in chr, no need for for loop
gap<- 120000
panel.gap<- 0.3

## C
lines.y1<- c(0*panel.gap)
lines.y2<- c(0*panel.gap)
lines.x1<- c(0)
lines.x2<- c(C.l[C.scaffolds[1], 'length'])
scaffolds<- c(C.scaffolds[1])
#for (i in 2:length(C.scaffolds)){
#  lines.y1<- c(lines.y1, 0*panel.gap)
#  lines.y2<- c(lines.y2, 0*panel.gap)
#  lines.x1<- c(lines.x1, lines.x1[length(lines.x1)]+C.l[C.scaffolds[i-1], 'length']+gap)
#  lines.x2<- c(lines.x2, lines.x2[length(lines.x2)]+gap+D.l[C.scaffolds[i], 'length'])
#  scaffolds<- c(scaffolds, C.scaffolds[i])
#}
## B
lines.y1<- c(lines.y1, 1*panel.gap)
lines.y2<- c(lines.y2, 1*panel.gap)
lines.x1<- c(lines.x1, 0)
lines.x2<- c(lines.x2, B.l[B.scaffolds[1], 'length'])
scaffolds<- c(scaffolds, B.scaffolds[1])
#for (i in 2:length(B.scaffolds)){
#  lines.y1<- c(lines.y1, 1*panel.gap)
#  lines.y2<- c(lines.y2, 1*panel.gap)
#  lines.x1<- c(lines.x1, lines.x1[length(lines.x1)]+B.l[B.scaffolds[i-1], 'length']+gap)
#  lines.x2<- c(lines.x2, lines.x2[length(lines.x2)]+gap+B.l[B.scaffolds[i], 'length'])
#  scaffolds<- c(scaffolds, B.scaffolds[i])
#}
## A
lines.y1<- c(lines.y1, 2*panel.gap)
lines.y2<- c(lines.y2, 2*panel.gap)
lines.x1<- c(lines.x1, 0)
lines.x2<- c(lines.x2, A.l[A.scaffolds[1], 'length'])
scaffolds<- c(scaffolds, A.scaffolds[1])
#for (i in 2:length(A.scaffolds)){
#  lines.y1<- c(lines.y1, 2*panel.gap)
#  lines.y2<- c(lines.y2, 2*panel.gap)
#  lines.x1<- c(lines.x1, lines.x1[length(lines.x1)]+A.l[A.scaffolds[i-1], 'length']+gap)
#  lines.x2<- c(lines.x2, lines.x2[length(lines.x2)]+gap+A.l[A.scaffolds[i], 'length'])
#  scaffolds<- c(scaffolds, A.scaffolds[i])
#}


## start plotting
rep.gap<- 0.05
plot<- plot(lines.x2, lines.y2, type="n", bty="n", xlim= c(min(lines.x1), max(lines.x2)), axes=F, ylab='', xlab= '', ylim= c(min(lines.y1)-rep.gap, max(lines.y1)+rep.gap))
segments(lines.x1, lines.y1, lines.x2, lines.y2, col='grey')

## localize the genes
coord<- cbind(lines.y1, lines.y2, lines.x1, lines.x2)
rownames(coord)<- scaffolds
coord<- as.data.frame(coord)

## segments and polygons

#C(middle_1)vsB(middle_2)
for (i in 1:length(rownames(sub.t2))){
  B.s<- as.character(sub.t2[i,]$B_chr)
  C.s<- as.character(sub.t2[i,]$C_chr)
  if (C.s == "CBG.IV") {
    segments(coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_start),
             as.numeric(coord[B.s, ]$lines.y1)+0.02, 
             coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_start),
             as.numeric(coord[B.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    segments(coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_end),
             as.numeric(coord[B.s, ]$lines.y1)+0.02, 
             coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_end),
             as.numeric(coord[B.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    x <- c(coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_start), coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_end), coord[C.s, ]$lines.x1+(C.l["CBG.IV", 'length']-as.numeric(sub.t2[i,]$C_end)), coord[C.s, ]$lines.x1+(C.l["CBG.IV", 'length']-as.numeric(sub.t2[i,]$C_start)))
    y <- c(as.numeric(coord[B.s, ]$lines.y1)-0.02, as.numeric(coord[B.s, ]$lines.y1)-0.02, as.numeric(coord[C.s, ]$lines.y1)+0.02, as.numeric(coord[C.s, ]$lines.y1)+0.02)
    #calculate color based on orient, if sp34_start-sp34_end < 0, which means invertion
    c <- ifelse(x[2]-x[1]<0, "indianred1","dodgerblue3")
    polygon(x, y, density = NULL, angle = 45,
            border = adjustcolor('black', alpha.f=0.5), col = adjustcolor(c, alpha.f=0.7),
            fillOddEven = FALSE)
    
    segments(coord[C.s, ]$lines.x1+(C.l["CBG.IV", 'length']-as.numeric(sub.t2[i,]$C_start)),
             as.numeric(coord[C.s, ]$lines.y1)+0.02, 
             coord[C.s, ]$lines.x1+(C.l["CBG.IV", 'length']-as.numeric(sub.t2[i,]$C_start)),
             as.numeric(coord[C.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    segments(coord[C.s, ]$lines.x1+(C.l["CBG.IV", 'length']-as.numeric(sub.t2[i,]$C_end)),
             as.numeric(coord[C.s, ]$lines.y1)+0.02, 
             coord[C.s, ]$lines.x1+(C.l["CBG.IV", 'length']-as.numeric(sub.t2[i,]$C_end)),
             as.numeric(coord[C.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
  }
  else {
    segments(coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_start),
             as.numeric(coord[B.s, ]$lines.y1)+0.02, 
             coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_start),
             as.numeric(coord[B.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    segments(coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_end),
             as.numeric(coord[B.s, ]$lines.y1)+0.02, 
             coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_end),
             as.numeric(coord[B.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    x <- c(coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_start), coord[B.s, ]$lines.x1+as.numeric(sub.t2[i,]$B_end), coord[C.s, ]$lines.x1+as.numeric(sub.t2[i,]$C_end), coord[C.s, ]$lines.x1+as.numeric(sub.t2[i,]$C_start))
    y <- c(as.numeric(coord[B.s, ]$lines.y1)-0.02, as.numeric(coord[B.s, ]$lines.y1)-0.02, as.numeric(coord[C.s, ]$lines.y1)+0.02, as.numeric(coord[C.s, ]$lines.y1)+0.02)
    #calculate color based on orient, if sp34_start-sp34_end < 0, which means invertion
    c <- ifelse(x[2]-x[1]>0, "indianred1","dodgerblue3")
    polygon(x, y, density = NULL, angle = 45,
            border = adjustcolor('black', alpha.f=0.5), col = adjustcolor(c, alpha.f=0.7),
            fillOddEven = FALSE)
    
    segments(coord[C.s, ]$lines.x1+as.numeric(sub.t2[i,]$C_start),
             as.numeric(coord[C.s, ]$lines.y1)+0.02, 
             coord[C.s, ]$lines.x1+as.numeric(sub.t2[i,]$C_start),
             as.numeric(coord[C.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    segments(coord[C.s, ]$lines.x1+as.numeric(sub.t2[i,]$C_end),
             as.numeric(coord[C.s, ]$lines.y1)+0.02, 
             coord[C.s, ]$lines.x1+as.numeric(sub.t2[i,]$C_end),
             as.numeric(coord[C.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
  }
}


#A(top)vsB(middle_2)
for (i in 1:length(rownames(sub.t))){
  B.s<- as.character(sub.t[i,]$B_chr)
  A.s<- as.character(sub.t[i,]$A_chr)
  if (A.s == "PLAF.scaff0007") {
    segments(coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_start),
             as.numeric(coord[B.s, ]$lines.y1)+0.02, 
             coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_start),
             as.numeric(coord[B.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    segments(coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_end),
             as.numeric(coord[B.s, ]$lines.y1)+0.02, 
             coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_end),
             as.numeric(coord[B.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    x <- c(coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_start), coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_end), coord[A.s, ]$lines.x1+(A.l["PLAF.scaff0007", 'length']-as.numeric(sub.t[i,]$A_end)), coord[A.s, ]$lines.x1+(A.l["PLAF.scaff0007", 'length']-as.numeric(sub.t[i,]$A_start)))
    y <- c(as.numeric(coord[B.s, ]$lines.y1)+0.02, as.numeric(coord[B.s, ]$lines.y1)+0.02, as.numeric(coord[A.s, ]$lines.y1)-0.02, as.numeric(coord[A.s, ]$lines.y1)-0.02)
    #calculate color based on orient, if sp34_start-sp34_end < 0, which means invertion
    c <- ifelse(x[2]-x[1]<0, "indianred1","dodgerblue3")
    polygon(x, y, density = NULL, angle = 45,
            border = adjustcolor('black', alpha.f=0.5), col = adjustcolor(c, alpha.f=0.7),
            fillOddEven = FALSE)
    
    segments(coord[A.s, ]$lines.x1+(A.l["PLAF.scaff0007", 'length']-as.numeric(sub.t[i,]$A_start)),
             as.numeric(coord[A.s, ]$lines.y1)+0.02, 
             coord[A.s, ]$lines.x1+(A.l["PLAF.scaff0007", 'length']-as.numeric(sub.t[i,]$A_start)),
             as.numeric(coord[A.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    segments(coord[A.s, ]$lines.x1+(A.l["PLAF.scaff0007", 'length']-as.numeric(sub.t[i,]$A_end)),
             as.numeric(coord[A.s, ]$lines.y1)+0.02, 
             coord[A.s, ]$lines.x1+(A.l["PLAF.scaff0007", 'length']-as.numeric(sub.t[i,]$A_end)),
             as.numeric(coord[A.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
  }
  else {
    segments(coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_start),
             as.numeric(coord[B.s, ]$lines.y1)+0.02, 
             coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_start),
             as.numeric(coord[B.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    segments(coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_end),
             as.numeric(coord[B.s, ]$lines.y1)+0.02, 
             coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_end),
             as.numeric(coord[B.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    x <- c(coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_start), coord[B.s, ]$lines.x1+as.numeric(sub.t[i,]$B_end), coord[A.s, ]$lines.x1+as.numeric(sub.t[i,]$A_end), coord[A.s, ]$lines.x1+as.numeric(sub.t[i,]$A_start))
    y <- c(as.numeric(coord[B.s, ]$lines.y1)+0.02, as.numeric(coord[B.s, ]$lines.y1)+0.02, as.numeric(coord[A.s, ]$lines.y1)-0.02, as.numeric(coord[A.s, ]$lines.y1)-0.02)
    #calculate color based on orient, if sp34_start-sp34_end < 0, which means invertion
    c <- ifelse(x[2]-x[1]>0, "indianred1","dodgerblue3")
    polygon(x, y, density = NULL, angle = 45,
            border = adjustcolor('black', alpha.f=0.5), col = adjustcolor(c, alpha.f=0.7),
            fillOddEven = FALSE)
    
    segments(coord[A.s, ]$lines.x1+as.numeric(sub.t[i,]$A_start),
             as.numeric(coord[A.s, ]$lines.y1)+0.02, 
             coord[A.s, ]$lines.x1+as.numeric(sub.t[i,]$A_start),
             as.numeric(coord[A.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
    segments(coord[A.s, ]$lines.x1+as.numeric(sub.t[i,]$A_end),
             as.numeric(coord[A.s, ]$lines.y1)+0.02, 
             coord[A.s, ]$lines.x1+as.numeric(sub.t[i,]$A_end),
             as.numeric(coord[A.s, ]$lines.y1)-0.02, 
             col=adjustcolor('black', alpha.f=0.7))
  }
}

## labeling  
label.x<- c(0,0,0)
label.y<- c(0, 1, 2)*panel.gap
labels<- c('CBG', 'CE','CBG.allmaps')
text(label.x, label.y, labels=labels, pos= 2, srt= 0, cex= 0.75)
for (scaffold in rownames(coord)){
  text(coord[scaffold,'lines.x1'], coord[scaffold,'lines.y1']+0.04, labels= scaffold, adj= 0, cex= 0.75)
}
# 20170514
