function [cost, gradientVec] = costFunctionIter(architecturePara, ThetaVec, X, y, regulatingRate)
%COSTFUNCTIONITER Compute cost and gradient for iteration use
%   Wrapper of costFunction, use long-ass vec for gradient and Theta

cost = 0;
gradientVec = [];

ThetaCell = longAssVecToCell(ThetaVec, architecturePara);
[cost, gradientCell] = costFunction(architecturePara,  ThetaCell, X, y, regulatingRate);
gradientVec = cellToLongAssVec(gradientCell);

end
