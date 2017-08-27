# Run in Rstudio

library(ggplot2)
# for percent scale in y axis
library(scales)
# data input
pre_data <- read.table("/Users/dangliu/Desktop/JT_lab/Synteny/CEvsCE/test2.input.txt", header = F)
names(pre_data) <- c("ref", "qry", "N50", "Program")
#get median
#median(subset(pre_data$qry,pre_data$Program=="DAG"&pre_data$N50=="1Mb"))
data <- data.frame(pre_data[3:4], stack(pre_data[1:2]))
names(data) <- c("N50", "Program", "Cov", "Type")
# Use only query
data <- data[data$Type=='qry',]
#get delta
data[data$Program=='DAG',]$Cov <- 0.9997 - data[data$Program=='DAG',]$Cov
data[data$Program=='iAD',]$Cov <- 0.9993 - data[data$Program=='iAD',]$Cov
data[data$Program=='MCS',]$Cov <- 0.9997 - data[data$Program=='MCS',]$Cov
data[data$Program=='SyC',]$Cov <- 0.9997 - data[data$Program=='SyC',]$Cov
#data$N50 <- factor(data$N50, 
#                    levels = c('1Mb','500kb', '200kb', '100kb'),ordered = TRUE)
data$N50 <- factor(data$N50, 
                   levels = c('100kb', '200kb', '500kb', '1Mb'),ordered = TRUE)
p <- ggplot(data, aes(x=N50, y=Cov*100))
# plotting type
p <- p + geom_boxplot(outlier.size=0.6, outlier.shape=16, notch=FALSE, aes(fill = Program), width=1, lwd=0.3)

# x, y scales and styles
# boxplot.stats$stats gives the 5 point boundry of box
# coord_cartesian let us zoom in without chaning scale ratio
# theme_classic() remove grey backgroud
#sts <- boxplot.stats(data$Cov*100)$statss
#p <- p + coord_cartesian(ylim = c(0,max(sts)*1.05))
p <- p + scale_y_continuous(breaks=c(2,5,10,20), limits =c(0,20))
p <- p + labs(x = "N50", y = "Error rate (%)") + theme_classic()
p <- p + theme(axis.line.x = element_line(color="black", size = 0.5, linetype = 1),
               axis.line.y = element_line(color="black", size = 0.5, linetype = 1))
#p <- p + annotate("segment", x=-Inf, xend=Inf, y=-Inf, yend=-Inf, size=1) 
#p <- p + annotate("segment", x=-Inf, xend=-Inf, y=-Inf, yend=Inf, size=1)
# title setting
#p <- p + ggtitle(expression(paste(italic("C. elegans")," vs. fragmented ",italic("C. elegans"))))
p <- p + theme(plot.title = element_text(size=rel(1.5), face="bold"), panel.background = element_blank())
# Change colors
#p + scale_fill_manual(values=c("#33CCCC", "#FF9999"))
p <- p + scale_fill_manual(values=c("#FF0033", "#FF9966", "#009900", "#33CCCC"))
# partitions plot into panels
#p + facet_grid(Type ~ .)
#p <- p + facet_wrap( ~ Type, nrow = 1) + theme(strip.background = element_rect(fill = "grey"), strip.text.x = element_text(face = "bold", size = 12))
#p <- p + facet_wrap( ~ Type, nrow = 1, scales = "free") + theme(strip.background = element_rect(fill = "grey"), strip.text.x = element_text(face = "bold", size = 12))
# add horizontal line (DAG>iAD>MCS>SyC)
p <- p + geom_hline(aes(yintercept=5), colour="grey", linetype="solid")
p <- p + geom_hline(aes(yintercept=2), colour="grey", linetype="dashed")
p
