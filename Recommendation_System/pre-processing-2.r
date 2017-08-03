# Authors: 
# 1. Anuraag Motiwale - asmotiwa
# 2. Abhishek Singh - aksingh5
# 3. Parag Nakhwa - psnakhwa

review_nc <- read.csv("review_nc.csv", header = TRUE)
review_ncs <- data.frame(review_nc[,ncol(review_nc)], review_nc[, 2], review_nc[, 7])
write.table(review_ncs, "model_data.csv", sep = ",")
