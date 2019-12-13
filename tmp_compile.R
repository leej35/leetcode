library(readxl)
library(ggplot2)
# install.packages("gridExtra")
library(gridExtra)
library(grid)
library(stringr)

# W_ALL <- read_excel("research/notes/Thesis-Experiment/W_all_m4x8_h1.xlsx")
W_ALL <- read_excel("research/notes/Thesis-Experiment/W_all_m2_x20_v2.xlsx")

# W_ALL <- read_excel("research/notes/Thesis-Experiment/sim_v1.xlsx")
# W_ALL <- read_excel("research/notes/Thesis-Experiment/tipas_v1.xlsx")
# base_path = "/Users/visionary/research/notes/Thesis-Experiment/plots/sim_data_v8_split1/"
base_path = "/Users/visionary/research/notes/Thesis-Experiment/plots/w_m2x20_h128_v2/"


system(paste("mkdir -p ", base_path, sep=''))
# Filter out things
W_ALL = W_ALL[which(!W_ALL$`model-name`=='LSTM-PP-v12'),];
W_ALL = W_ALL[which(!W_ALL$`model-name`=='LSTM-PP-vbv-v12'),];
# W_ALL = W_ALL[which(!W_ALL$`model-name`=='LSTM-PP-v12-add-v4'),];
# W_ALL = W_ALL[which(!W_ALL$`model-name`=='logistic_count'),];

W_ALL = W_ALL[which(!W_ALL$hidden_dim==256),];


# W_ALL = W_ALL[which(!W_ALL$`window-hr-y`==6),];


clean_names <- function(input_w){
  colnames(input_w) = gsub("final_test: ", "", colnames(input_w))
  colnames(input_w) = gsub("(macro)", "", colnames(input_w))
  colnames(input_w) = gsub("\\(", "", colnames(input_w))
  colnames(input_w) = gsub("\\)", "", colnames(input_w))
  colnames(input_w) = gsub("accmicro", "acc", colnames(input_w))
  colnames(input_w) = gsub("second_occur", "occur_second", colnames(input_w))
  colnames(input_w) = gsub("first_occur", "occur_first", colnames(input_w))
  input_w$`model-name` = str_replace_all(input_w$`model-name`,"-v12", "")
  input_w$`model-name` = str_replace_all(input_w$`model-name`,"LSTM-PP", "Proposed")
  input_w$`model-name` = str_replace_all(input_w$`model-name`,"logistic_", "LR-")
  input_w$`model-name` = str_replace_all(input_w$`model-name`,"MyLayerLSTM", "LSTM")
  input_w$`model-name` = str_replace_all(input_w$`model-name`,"binary", "Binary")
  input_w$`model-name` = str_replace_all(input_w$`model-name`,"LR-last", "Markov")
  input_w$`model-name` = str_replace_all(input_w$`model-name`,"count", "Count")
  input_w$`model-name` = str_replace_all(input_w$`model-name`,"-add", "")
  input_w$`model-name` = str_replace_all(input_w$`model-name`,"-v4", "")
  
  
  return(input_w)
}



data = clean_names(W_ALL)
# data$`model-name` = paste(data$`model-name`, data$hidden_dim, sep='-')
data = data[order(data$`model-name`),]

data_w1 = data[which(data$`window-hr-y`==1),];
data_w3 = data[which(data$`window-hr-y`==3),];
data_w6 = data[which(data$`window-hr-y`==6),];
data_w12 = data[which(data$`window-hr-y`==12),];
data_w24 = data[which(data$`window-hr-y`==24),];



func_plot <- function(datax, title, metric_col, show_legend, show_label){
  #`model-name`, aes(x 
  px = ggplot(datax, aes(x=factor(`model-name`, level = c('LR-Binary', 'LR-Count', 'Markov', 'LSTM', 'LSTM-Attn', 'LSTM-RB', 'LSTM-RB-cat', 'Proposed', 'Proposed-concat', 'Proposed-concat-rbcat', 'Proposed-concat-norb')) ,y=metric_col, fill=`model-name`))  + geom_point(show.legend=show_legend, shape=4, size = 0.85, aes(colour = factor(`model-name`))) + labs(title=title, x="",y = "")
  # px = ggplot(datax, aes(x=factor(`model-name`) ,y=metric_col, fill=`model-name`))  + geom_point(show.legend=show_legend, shape=4, size = 0.85, aes(colour = factor(`model-name`))) + labs(title=paste(metric_name,"w=", w, "", sep=""), x="",y = "") 
  px = px + stat_summary(fun.y=mean, geom="point", shape=23, size=2)
  px = px + theme(axis.text.x=element_text(angle=90, hjust=1, vjust=0.5))
  if (show_legend){
    px = px + theme(legend.position="left") 
  }else{
    px = px + theme(legend.position="none") 
  }
  if (!show_label){
    px = px +
      theme(axis.title.x=element_blank(),
          )
  }
  px = px +
    theme(axis.text.x=element_blank(),
          axis.ticks.x=element_blank())
  px = px +theme(plot.title = element_text(size=9))
  
  return(px)
}





# https://cran.r-project.org/web/packages/egg/vignettes/Ecosystem.html
grid_arrange_shared_legend <-
  function(...,
           show_legend = FALSE,
           ncol = length(list(...)),
           nrow = 1,
           position = c("bottom", "right")) {
    
    plots <- list(...)
    position <- match.arg(position)
    g <-
      ggplotGrob(plots[[1]] + theme(legend.position = position, legend.title=element_blank(), legend.direction = "horizontal"))$grobs
    legend <- g[[which(sapply(g, function(x)
      x$name) == "guide-box")]]
    lheight <- sum(legend$height)
    lwidth <- sum(legend$width)
    gl <- lapply(plots, function(x)
      x + theme(legend.position = "none"))
    gl <- c(gl, ncol = ncol, nrow = nrow)
    
    if(show_legend){
      combined <- switch(
        position,
        "bottom" = arrangeGrob(
          do.call(arrangeGrob, gl),
          legend,
          ncol = 1,
          heights = unit.c(unit(1, "npc") - lheight, lheight)
        ),
        "right" = arrangeGrob(
          do.call(arrangeGrob, gl),
          legend,
          ncol = 2,
          widths = unit.c(unit(1, "npc") - lwidth, lwidth)
        )
      )
      
    }else{
      combined <- switch(
        position,
        "bottom" = arrangeGrob(
          do.call(arrangeGrob, gl),
          ncol = 1,
          heights = unit.c(unit(1, "npc"))
        ),
        "right" = arrangeGrob(
          do.call(arrangeGrob, gl),
          ncol = 2,
          widths = unit.c(unit(1, "npc"))
        )
      )
      
    }
    
    # grid.newpage()
    grid.draw(combined)
    
    # return gtable invisibly
    invisible(combined)
    
  }



# #-------
# target_cols = target_cols[30:142]
# 
# 
# target_cols = target_cols[-25]
# target_cols = target_cols[-24]
# target_cols = target_cols[-23]
# target_cols = target_cols[-22]
# target_cols = target_cols[-21]
# print(target_cols)
#------
# target_cols = target_cols[32:43]
print(colnames(data_w24))
target_cols = colnames(data_w24)[30:43]


print(target_cols)


add_axis_title=TRUE

for (target_col in target_cols){
  
  if(is.na.data.frame(data_w6[target_col])){
    next
  }
  if(is.na.data.frame(data_w12[target_col])){
    next
  }
  if(is.na.data.frame(data_w24[target_col])){
    next
  }

  if(is.na.data.frame(data_w3[target_col])){
    next
  }
  if(is.na.data.frame(data_w1[target_col])){
    next
  }

    
  f_path = paste(base_path, target_col, ".pdf", sep="")
  f_path = str_replace_all(f_path, "  ", " ")
  f_path = str_replace_all(f_path, " ", "_")
  print(f_path)
  pdf(f_path, width=3.80*(1.8), height=2.75)
  
  
  label = paste(target_col, " ", sep=" ")
  label = str_replace(label, "  ", " ")
  label = str_replace(label, " ", "\n")
  label = paste(label, "\n", sep="")
  
  label = ""
  
  title = paste(label,"", sep="")
  p1 = func_plot(data_w1, title, data_w1[target_col], FALSE, FALSE)
  
  title = paste(label,"w=3", sep="")
  p3 = func_plot(data_w3, title, data_w3[target_col], FALSE, FALSE)
  title = paste(label,"w=6", sep="")
  p6 = func_plot(data_w6, title, data_w6[target_col], FALSE, FALSE)
  title = paste(label,"w=12", sep="")
  p12 = func_plot(data_w12, title, data_w12[target_col], FALSE, FALSE)
  title = paste(label,"w=24", sep="")
  p24 = func_plot(data_w24, title, data_w24[target_col], FALSE, FALSE)

   
  if(add_axis_title){
    p1 = p1 + theme(axis.text.x = element_text(size=rel(0.8), angle = 90))
    p3 = p3 + theme(axis.text.x = element_text(size=rel(0.8), angle = 90))
    p6 = p6 + theme(axis.text.x = element_text(size=rel(0.8), angle = 90))
    p12 = p12 + theme(axis.text.x = element_text(size=rel(0.8), angle = 90))
    p24 = p24 + theme(axis.text.x = element_text(size=rel(0.8), angle = 90))
  }
  #
  grid_arrange_shared_legend(p1,p3, p6, p12, p24, show_legend = !add_axis_title)
  # grid_arrange_shared_legend(p1, show_legend = !add_axis_title) 
  
    dev.off() 
}

# clean 
while(1){dev.off()}


# ---------------------------------------------------------------------------------------------------------
# summary into csv

library(data.table)
summ_stats <- function(data_x){
  dt_x <- data.table(data_x)
  dt_w_name <- setnames(dt_x[, sapply(.SD, function(x) list(mean=round(mean(x), 3), sd=round(sd(x), 3))), by=`model-name`], c("model-name", sapply(names(dt_x)[-1], paste0, c(".mean", ".SD"))))

    return(dt_w_name)
}

sum_stats_w6 = summ_stats(data_w6)[, -c(2:55)] 
sum_stats_w12 = summ_stats(data_w12)[, -c(2:55)]
sum_stats_w24 = summ_stats(data_w24)[, -c(2:55)]

write.csv(sum_stats_w6, paste(base_path, "/stat_w6_excl_fwindow.csv", sep=""))
write.csv(sum_stats_w12, paste(base_path, "/stat_w12_excl_fwindow.csv", sep=""))
write.csv(sum_stats_w24, paste(base_path, "/stat_w24_excl_fwindow.csv", sep=""))



# ---------------------------------------------------------------------------------------------------------
# of the same time window

print_all_by_hour_auprc <- function(data_w, w_hr){
  pdf(paste(base_path, "/auprc_overall_",w_hr,"_dots.pdf", sep=""), width=20.15, height=2.80)
  p24_overall = func_plot(data_w, paste(w_hr, " (overall)",sep=""), "", data_w$`auprc`, FALSE, FALSE)
  p24_startone = func_plot(data_w, paste(w_hr, " (start one)",sep=""), "", data_w$`auprc  start_one`, FALSE, FALSE)
  p24_startzero = func_plot(data_w, paste(w_hr, " (start zero)",sep=""), "", data_w$`auprc  start_zero`, FALSE, FALSE)
  p24_first_occur = func_plot(data_w, paste(w_hr, " (occur first)",sep=""), "", data_w$`auprc  occur_first`, FALSE, FALSE)
  p24_second_occur = func_plot(data_w, paste(w_hr, " (occur second)",sep=""), "", data_w$`auprc  occur_second`, FALSE, FALSE)
  p24_later_occur = func_plot(data_w, paste(w_hr, " (occur later)",sep=""), "", data_w$`auprc  later_occur`, FALSE, FALSE)
  grid_arrange_shared_legend(p24_overall, p24_startone, p24_startzero, p24_first_occur, p24_second_occur, p24_later_occur, show_legend = !add_axis_title)
  dev.off()
}

print_all_by_hour_auroc <- function(data_w, w_hr){
  pdf(paste(base_path, "/auroc_overall_",w_hr,"_dots.pdf", sep=""), width=20.15, height=2.80)
  p24_overall = func_plot(data_w, paste(w_hr, " (overall)",sep=""), "", data_w$`auroc`, FALSE, FALSE)
  p24_startone = func_plot(data_w, paste(w_hr, " (start one)",sep=""), "", data_w$`auroc  start_one`, FALSE, FALSE)
  p24_startzero = func_plot(data_w, paste(w_hr, " (start zero)",sep=""), "", data_w$`auroc  start_zero`, FALSE, FALSE)
  p24_first_occur = func_plot(data_w, paste(w_hr, " (occur first)",sep=""), "", data_w$`auroc  occur_first`, FALSE, FALSE)
  p24_second_occur = func_plot(data_w, paste(w_hr, " (occur second)",sep=""), "", data_w$`auroc  occur_second`, FALSE, FALSE)
  p24_later_occur = func_plot(data_w, paste(w_hr, " (occur later)",sep=""), "", data_w$`auroc  later_occur`, FALSE, FALSE)
  grid_arrange_shared_legend(p24_overall, p24_startone, p24_startzero, p24_first_occur, p24_second_occur, p24_later_occur, show_legend = !add_axis_title)
  dev.off()
}



print_all_by_hour_auprc(data_w24, 24)
print_all_by_hour_auprc(data_w12, 12)
print_all_by_hour_auprc(data_w6, 6)


print_all_by_hour_auroc(data_w24, 24)
print_all_by_hour_auroc(data_w12, 12)
print_all_by_hour_auroc(data_w6, 6)



# ---------------------------------------------------------------------------------------------------------


# OVERALL AUPRC 
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_overall.pdf", width=9.15, height=2.80)
#p3 = func_plot(data_w3, "3", "", data_w3$`auprc`, FALSE, FALSE)
p6 = func_plot(data_w6, "6", "", data_w6$`auprc`, FALSE, FALSE)
p12 = func_plot(data_w12, "12", "", data_w12$`auprc`, FALSE, FALSE)
p24 = func_plot(data_w24, "24", "", data_w24$`auprc`, FALSE, FALSE)
# grid_arrange_shared_legend(p6, p12, p24, show_legend = TRUE)
grid_arrange_shared_legend(p6, p12, p24, show_legend = TRUE)
dev.off()


## ADHOC :: AUPRC

pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_overall_24_dots.pdf", width=20.15, height=2.80)
p24_overall = func_plot(data_w24, "24 (overall)", "", data_w24$`auprc`, FALSE, FALSE)
p24_drug = func_plot(data_w24, "24 (drug)", "", data_w24$`auprc  drug`, FALSE, FALSE)
p24_chart = func_plot(data_w24, "24 (chart)", "", data_w24$`auprc  chart`, FALSE, FALSE)
p24_lab = func_plot(data_w24, "24 (lab)", "", data_w24$`auprc  lab`, FALSE, FALSE)
p24_proc = func_plot(data_w24, "24 (proc)", "", data_w24$`auprc  proc`, FALSE, FALSE)
p24_startone = func_plot(data_w24, "24 (start one)", "", data_w24$`auprc  start_one`, FALSE, FALSE)
p24_startzero = func_plot(data_w24, "24 (start zero)", "", data_w24$`auprc  start_zero`, FALSE, FALSE)
p24_first_occur = func_plot(data_w24, "24 (occur first)", "", data_w24$`auprc  first_occur`, FALSE, FALSE)
p24_second_occur = func_plot(data_w24, "24 (occur second)", "", data_w24$`auprc  second_occur`, FALSE, FALSE)
p24_later_occur = func_plot(data_w24, "24 (occr later)", "", data_w24$`auprc  later_occur`, FALSE, FALSE)
grid_arrange_shared_legend(p24_overall, p24_drug, p24_chart, p24_lab, p24_proc, p24_startone, p24_startzero, p24_first_occur, p24_second_occur, p24_later_occur, show_legend = TRUE)
dev.off()

pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_overall_12.pdf", width=20.15, height=2.80)
p12_overall = func_plot(data_w12, "12 (overall)", "", data_w12$`auprc`, FALSE, FALSE)
p12_drug = func_plot(data_w12, "12 (drug)", "", data_w12$`auprc  drug`, FALSE, FALSE)
p12_chart = func_plot(data_w12, "12 (chart)", "", data_w12$`auprc  chart`, FALSE, FALSE)
p12_lab = func_plot(data_w12, "12 (lab)", "", data_w12$`auprc  lab`, FALSE, FALSE)
p12_proc = func_plot(data_w12, "12 (proc)", "", data_w12$`auprc  proc`, FALSE, FALSE)
p12_startone = func_plot(data_w12, "12 (start one)", "", data_w12$`auprc  start_one`, FALSE, FALSE)
p12_startzero = func_plot(data_w12, "12 (start zero)", "", data_w12$`auprc  start_zero`, FALSE, FALSE)
p12_first_occur = func_plot(data_w12, "12 (occur first)", "", data_w12$`auprc  first_occur`, FALSE, FALSE)
p12_second_occur = func_plot(data_w12, "12 (occur second)", "", data_w12$`auprc  second_occur`, FALSE, FALSE)
p12_later_occur = func_plot(data_w12, "12 (occr later)", "", data_w12$`auprc  later_occur`, FALSE, FALSE)
grid_arrange_shared_legend(p12_overall, p12_drug, p12_chart, p12_lab, p12_proc, p12_startone, p12_startzero, p12_first_occur, p12_second_occur, p12_later_occur, show_legend = TRUE)
dev.off()


pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_overall_6.pdf", width=20.15, height=2.80)
p6_overall = func_plot(data_w6, "6 (overall)", "", data_w6$`auprc`, FALSE, FALSE)
p6_drug = func_plot(data_w6, "6 (drug)", "", data_w6$`auprc  drug`, FALSE, FALSE)
p6_chart = func_plot(data_w6, "6 (chart)", "", data_w6$`auprc  chart`, FALSE, FALSE)
p6_lab = func_plot(data_w6, "6 (lab)", "", data_w6$`auprc  lab`, FALSE, FALSE)
p6_proc = func_plot(data_w6, "6 (proc)", "", data_w6$`auprc  proc`, FALSE, FALSE)
p6_startone = func_plot(data_w6, "6 (start one)", "", data_w6$`auprc  start_one`, FALSE, FALSE)
p6_startzero = func_plot(data_w6, "6 (start zero)", "", data_w6$`auprc  start_zero`, FALSE, FALSE)
p6_first_occur = func_plot(data_w6, "6 (occur first)", "", data_w6$`auprc  first_occur`, FALSE, FALSE)
p6_second_occur = func_plot(data_w6, "6 (occur second)", "", data_w6$`auprc  second_occur`, FALSE, FALSE)
p6_later_occur = func_plot(data_w6, "6 (occr later)", "", data_w6$`auprc  later_occur`, FALSE, FALSE)
grid_arrange_shared_legend(p6_overall, p6_drug, p6_chart, p6_lab, p6_proc, p6_startone, p6_startzero, p6_first_occur, p6_second_occur, p6_later_occur, show_legend = TRUE)
dev.off()




## ADHOC :: AUROC
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auroc_overall_24.pdf", width=20.15, height=2.80)
p24_overall = func_plot(data_w24, "24 (overall)", "", data_w24$`auroc`, FALSE, FALSE)
p24_drug = func_plot(data_w24, "24 (drug)", "", data_w24$`auroc  drug`, FALSE, FALSE)
p24_chart = func_plot(data_w24, "24 (chart)", "", data_w24$`auroc  chart`, FALSE, FALSE)
p24_lab = func_plot(data_w24, "24 (lab)", "", data_w24$`auroc  lab`, FALSE, FALSE)
p24_proc = func_plot(data_w24, "24 (proc)", "", data_w24$`auroc  proc`, FALSE, FALSE)
p24_startone = func_plot(data_w24, "24 (start one)", "", data_w24$`auroc  start_one`, FALSE, FALSE)
p24_startzero = func_plot(data_w24, "24 (start zero)", "", data_w24$`auroc  start_zero`, FALSE, FALSE)
p24_first_occur = func_plot(data_w24, "24 (occur first)", "", data_w24$`auroc  first_occur`, FALSE, FALSE)
p24_second_occur = func_plot(data_w24, "24 (occur second)", "", data_w24$`auroc  second_occur`, FALSE, FALSE)
p24_later_occur = func_plot(data_w24, "24 (occr later)", "", data_w24$`auroc  later_occur`, FALSE, FALSE)
grid_arrange_shared_legend(p24_overall, p24_drug, p24_chart, p24_lab, p24_proc, p24_startone, p24_startzero, p24_first_occur, p24_second_occur, p24_later_occur, show_legend = TRUE)
dev.off()


pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auroc_overall_12.pdf", width=20.15, height=2.80)
p12_overall = func_plot(data_w12, "12 (overall)", "", data_w12$`auroc`, FALSE, FALSE)
p12_drug = func_plot(data_w12, "12 (drug)", "", data_w12$`auroc  drug`, FALSE, FALSE)
p12_chart = func_plot(data_w12, "12 (chart)", "", data_w12$`auroc  chart`, FALSE, FALSE)
p12_lab = func_plot(data_w12, "12 (lab)", "", data_w12$`auroc  lab`, FALSE, FALSE)
p12_proc = func_plot(data_w12, "12 (proc)", "", data_w12$`auroc  proc`, FALSE, FALSE)
p12_startone = func_plot(data_w12, "12 (start one)", "", data_w12$`auroc  start_one`, FALSE, FALSE)
p12_startzero = func_plot(data_w12, "12 (start zero)", "", data_w12$`auroc  start_zero`, FALSE, FALSE)
p12_first_occur = func_plot(data_w12, "12 (occur first)", "", data_w12$`auroc  first_occur`, FALSE, FALSE)
p12_second_occur = func_plot(data_w12, "12 (occur second)", "", data_w12$`auroc  second_occur`, FALSE, FALSE)
p12_later_occur = func_plot(data_w12, "12 (occr later)", "", data_w12$`auroc  later_occur`, FALSE, FALSE)
grid_arrange_shared_legend(p12_overall, p12_drug, p12_chart, p12_lab, p12_proc, p12_startone, p12_startzero, p12_first_occur, p12_second_occur, p12_later_occur, show_legend = TRUE)
dev.off()


pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auroc_overall_6.pdf", width=20.15, height=2.80)
p6_overall = func_plot(data_w6, "6 (overall)", "", data_w6$`auroc`, FALSE, FALSE)
p6_drug = func_plot(data_w6, "6 (drug)", "", data_w6$`auroc  drug`, FALSE, FALSE)
p6_chart = func_plot(data_w6, "6 (chart)", "", data_w6$`auroc  chart`, FALSE, FALSE)
p6_lab = func_plot(data_w6, "6 (lab)", "", data_w6$`auroc  lab`, FALSE, FALSE)
p6_proc = func_plot(data_w6, "6 (proc)", "", data_w6$`auroc  proc`, FALSE, FALSE)
p6_startone = func_plot(data_w6, "6 (start one)", "", data_w6$`auroc  start_one`, FALSE, FALSE)
p6_startzero = func_plot(data_w6, "6 (start zero)", "", data_w6$`auroc  start_zero`, FALSE, FALSE)
p6_first_occur = func_plot(data_w6, "6 (occur first)", "", data_w6$`auroc  first_occur`, FALSE, FALSE)
p6_second_occur = func_plot(data_w6, "6 (occur second)", "", data_w6$`auroc  second_occur`, FALSE, FALSE)
p6_later_occur = func_plot(data_w6, "6 (occr later)", "", data_w6$`auroc  later_occur`, FALSE, FALSE)
grid_arrange_shared_legend(p6_overall, p6_drug, p6_chart, p6_lab, p6_proc, p6_startone, p6_startzero, p6_first_occur, p6_second_occur, p6_later_occur, show_legend = TRUE)
dev.off()



#p_grid = grid.arrange(p6, p12, p24, nrow = 1,      
#                      top = textGrob("AUPRC",gp=gpar(fontsize=15,font=2)))

# OVERALL AUROC 
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auroc_overall.pdf", width=9.15, height=2.80)

p3 = func_plot(data_w3, "3", "", data_w3$`auroc`, FALSE, FALSE)
p6 = func_plot(data_w6, "6", "", data_w6$`auroc`, FALSE, FALSE)
p12 = func_plot(data_w12, "12", "", data_w12$`auroc`, FALSE, FALSE)
p24 = func_plot(data_w24, "24", "", data_w24$`auroc`, FALSE, FALSE)
#p_grid = grid.arrange(p6, p12, p24, nrow = 1,      
#                      top = textGrob("AUROC",gp=gpar(fontsize=15,font=2)))
grid_arrange_shared_legend(p6, p12, p24, show_legend = TRUE)
dev.off()


# AUPRC - Category - Drug 
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_category_drug.pdf", width=9.15, height=2.18)
p3 = func_plot(data_w3, "3", "", data_w3$`auprc  drug`, FALSE, FALSE)
p6 = func_plot(data_w6, "6", "", data_w6$`auprc  drug`, FALSE, FALSE)
p12 = func_plot(data_w12, "12", "", data_w12$`auprc  drug`, FALSE, FALSE)
p24 = func_plot(data_w24, "24", "", data_w24$`auprc  drug`, FALSE, FALSE)
# p_grid_drug = grid.arrange(p6, p12, p24, nrow = 1,      
# top = textGrob("AUPRC: Drug",gp=gpar(fontsize=15,font=2)))
grid_arrange_shared_legend(p6, p12, p24)

dev.off()

# AUPRC - Category - Lab 
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_category_lab.pdf", width=9.15, height=2.18)
p3 = func_plot(data_w3, "3", "", data_w3$`auprc  lab`, FALSE, FALSE)
p6 = func_plot(data_w6, "6", "", data_w6$`auprc  lab`, FALSE, FALSE)
p12 = func_plot(data_w12, "12", "", data_w12$`auprc  lab`, FALSE, FALSE)
p24 = func_plot(data_w24, "24", "", data_w24$`auprc  lab`, FALSE, FALSE)
# p_grid_lab = grid.arrange(p6, p12, p24, nrow = 1,      
# top = textGrob("AUPRC: Lab",gp=gpar(fontsize=15,font=2)))
grid_arrange_shared_legend(p6, p12, p24)

dev.off()

# AUPRC - Category - Chart 
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_category_chart.pdf", width=9.15, height=2.18)
p3 = func_plot(data_w3, "3", "", data_w3$`auprc  chart`, FALSE, FALSE)
p6 = func_plot(data_w6, "6", "", data_w6$`auprc  chart`, FALSE, FALSE)
p12 = func_plot(data_w12, "12", "", data_w12$`auprc  chart`, FALSE, FALSE)
p24 = func_plot(data_w24, "24", "", data_w24$`auprc  chart`, FALSE, FALSE)
# p_grid_chart = grid.arrange(p6, p12, p24, nrow = 1,      
#                       top = textGrob("AUPRC: Chart",gp=gpar(fontsize=15,font=2)))
grid_arrange_shared_legend(p6, p12, p24)
dev.off()

# AUPRC - Category - Proc 
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_category_proc.pdf", width=9.15, height=2.8)
p3 = func_plot(data_w3, "3", "", data_w3$`auprc  proc`, FALSE, FALSE)
p6 = func_plot(data_w6, "6", "", data_w6$`auprc  proc`, FALSE, FALSE)
p12 = func_plot(data_w12, "12", "", data_w12$`auprc  proc`, FALSE, FALSE)
p24 = func_plot(data_w24, "24", "", data_w24$`auprc  proc`, FALSE, FALSE)
# p_grid_proc = grid.arrange(p6, p12, p24, nrow = 1,      
#                       top = textGrob("AUPRC: Procedure",gp=gpar(fontsize=15,font=2)))
grid_arrange_shared_legend(p6, p12, p24, show_legend = TRUE)
dev.off()







# AUPRC - Start - One 
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_start_one.pdf", width=9.15, height=2.18)
p3 = func_plot(data_w3, "3", "", data_w3$`auprc  start_one`, FALSE, FALSE)
p6 = func_plot(data_w6, "6", "", data_w6$`auprc  start_one`, FALSE, FALSE)
p12 = func_plot(data_w12, "12", "", data_w12$`auprc  start_one`, FALSE, FALSE)
p24 = func_plot(data_w24, "24", "", data_w24$`auprc  start_one`, FALSE, FALSE)
# p_grid_drug = grid.arrange(p6, p12, p24, nrow = 1,      
#                            top = textGrob("AUPRC: Repetitive",gp=gpar(fontsize=15,font=2)))
grid_arrange_shared_legend(p6, p12, p24)

dev.off()


# AUPRC - Start - Zero 
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_start_zero.pdf", width=9.15, height=2.8)
p3 = func_plot(data_w3, "3", "", data_w3$`auprc  start_zero`, FALSE, FALSE)
p6 = func_plot(data_w6, "6", "", data_w6$`auprc  start_zero`, FALSE, FALSE)
p12 = func_plot(data_w12, "12", "", data_w12$`auprc  start_zero`, FALSE, FALSE)
p24 = func_plot(data_w24, "24", "", data_w24$`auprc  start_zero`, FALSE, FALSE)
# p_grid_drug = grid.arrange(p6, p12, p24, nrow = 1,      
#                            top = textGrob("AUPRC: Nonrepetitive",gp=gpar(fontsize=15,font=2)))
grid_arrange_shared_legend(p6, p12, p24, show_legend = TRUE)

dev.off()




# AUPRC - Occur - First 
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_occur_first.pdf", width=9.15, height=2.18)
p3 = func_plot(data_w3, "3", "", data_w3$`auprc  first_occur`, FALSE, FALSE)
p6 = func_plot(data_w6, "6", "", data_w6$`auprc  first_occur`, FALSE, FALSE)
p12 = func_plot(data_w12, "12", "", data_w12$`auprc  first_occur`, FALSE, FALSE)
p24 = func_plot(data_w24, "24", "", data_w24$`auprc  first_occur`, FALSE, FALSE)
# p_grid_drug = grid.arrange(p6, p12, p24, nrow = 1,      
#                            top = textGrob("AUPRC: First occurs",gp=gpar(fontsize=15,font=2)))
grid_arrange_shared_legend(p6, p12, p24)

dev.off()


# AUPRC - Occur - Second 
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_occur_second.pdf", width=9.15, height=2.18)
p3 = func_plot(data_w3, "3", "", data_w3$`auprc  second_occur`, FALSE, FALSE)
p6 = func_plot(data_w6, "6", "", data_w6$`auprc  second_occur`, FALSE, FALSE)
p12 = func_plot(data_w12, "12", "", data_w12$`auprc  second_occur`, FALSE, FALSE)
p24 = func_plot(data_w24, "24", "", data_w24$`auprc  second_occur`, FALSE, FALSE)
# p_grid_drug = grid.arrange(p6, p12, p24, nrow = 1,      
#                            top = textGrob("AUPRC: Second occurs",gp=gpar(fontsize=15,font=2)))
grid_arrange_shared_legend(p6, p12, p24)

dev.off()


# AUPRC - Occur - Third 
pdf("/Users/visionary/research/notes/Thesis-Experiment/plots/auprc_occur_later.pdf", width=9.15, height=2.8)
p3 = func_plot(data_w3, "3", "", data_w3$`auprc  later_occur`, FALSE, FALSE)
p6 = func_plot(data_w6, "6", "", data_w6$`auprc  later_occur`, FALSE, FALSE)
p12 = func_plot(data_w12, "12", "", data_w12$`auprc  later_occur`, FALSE, FALSE)
p24 = func_plot(data_w24, "24", "", data_w24$`auprc  later_occur`, FALSE, FALSE)
# p_grid_drug = grid.arrange(p6, p12, p24, nrow = 1,      
#                            top = textGrob("AUPRC: Third and later occurs",gp=gpar(fontsize=15,font=2)))
grid_arrange_shared_legend(p6, p12, p24, show_legend = TRUE)

dev.off()


