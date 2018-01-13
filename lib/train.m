function ThetaCell = train(X, y, ThetaCellInitial, regulatingRate, maxIter, architecturePara)
%TRAIN Train neural-network and returns a trained ThetaCell
%   apply fmincg for gradient descent

ThetaCell = ThetaCellInitial;

ThetaVecInitial = cellToLongAssVec(ThetaCellInitial);

options = optimset('MaxIter', maxIter, 'GradObj', 'on');
costFunctionIterUse = @(pThetaVec) costFunctionIter(architecturePara, pThetaVec, X, y, regulatingRate);
ThetaVec = fmincg(costFunctionIterUse, ThetaVecInitial, options);

ThetaCell = longAssVecToCell(ThetaVec, architecturePara);

end