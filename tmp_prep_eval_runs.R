library(readxl)
library(glue)
str.rfind <- function(s, char) { rev(grep(char, unlist(strsplit(s, NULL)), fixed=T))[1]}
printf <- function(...) invisible(print(sprintf(...)))


data <- read_excel("research/notes/Thesis-Experiment/W_all_m4x8_h1.xlsx")

data = data[order(data$`window-hr-y`, data$`model-name`, data$split_id),]

cmds = ''
for (exp_key in unique(data$`Experiment key`)){
  row = data[which(data$`Experiment key`==exp_key),];
  
  w_hr = row$`window-hr-y`
  
  # skip any rows
  if(w_hr == 6){
    next
  }
  
  split = max(row$`split-id`, row$`split_id`)
  model_name = row$`model-name`
  if(!is.na(row$`weight-decay`)){
    w_decay = row$`weight-decay`
  }else if(!is.na(row$weight_decay)){
    w_decay = row$weight_decay
  }else{
    w_decay = 0
  }
  h_dim = row$hidden_dim
  model_prefix = row$`model-prefix`
  
  last_slash_idx = str.rfind(model_prefix, '/')
  # model_path = substr(model_prefix,0, last_slash_idx)
  
  command = glue("bash run_sci.bash {w_hr} {model_name} {split} '--skip-hypertuning --weight-decay {w_decay} --eval-only --load-model-from {model_prefix}_final.model';")
  # printf(command)
  cmds=paste(cmds, command)
}



out <- capture.output(summary(my_very_time_consuming_regression))

cat("My title", out, file="summary_of_my_very_time_consuming_regression.txt", sep="n", append=TRUE)

