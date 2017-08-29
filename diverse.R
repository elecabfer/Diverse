####select rows with no negative values:
foldchangematrix<-as.matrix(foldchange)
bool<-apply(foldchangematrix[,1:5], 1, function(x) all(x>0.0000001)) #también se puede usar any()
#Rachel's: check if the minium (min) value of the row is negative

bool<-!bool #Change FALSE to TRUE
matrixpositives<-foldchangematrix[bool,]
