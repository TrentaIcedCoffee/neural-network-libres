function [cost, gradientCell] = costFunction(architecturePara, ThetaCell, X, y, regulatingRate)
%COSTFUNCTION Compute cost and gradient for develope use
%   for iteration use, go costFunctionIter, wrapped for iteration use

[m n] = size(X);
classNumber = architecturePara(end);
Y = yToY(y, classNumber);
cost = 0;
gradientCell = cell(1, length(architecturePara) - 1);

% forward propergate for hypothesis
[hypoMat, zCell, aCell] = forwardPropergate(ThetaCell, X);
% penalty for regulation
penalty = 0;
for i = 1:length(ThetaCell)
    ThetaMat = cell2mat(ThetaCell(i));
    penalty = penalty + sum(sum(ThetaMat(:, 2:end) .^ 2));
end
penalty = (regulatingRate / (2 * m)) * penalty;
% compute cost
cost = (-1 / m) * sum(sum(Y .* log(hypoMat) + (1 - Y) .* log(1 - hypoMat))) + penalty;
% compute gradient, convert it to a 'long-ass' vec with size(~, 1) for iteration
gradientCell = backwardPropergate(regulatingRate, hypoMat, Y, ThetaCell, zCell, aCell);

end
