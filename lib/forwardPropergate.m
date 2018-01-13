function [hypoMat, zCell, aCell] = forwardPropergate(ThetaCell, X)
%FORWARDPROPERGATE Run forward propergate and record history z, a
%   classNumber = size(cell2mat(ThetaCell(end)), 1)
%   hypoMat has size(samples, classNumber)
%   max value in hypoMat(i, :) gives pridiction
%   zCell, aCell has length layerNumber
%   zCell(1) is dummy cell
%   z is raw hypothesis, a is sigmoid hypothesis with bias term

[m n] = size(X);
layerNumber = size(ThetaCell, 2) + 1;
classNumber = size(cell2mat(ThetaCell(end)), 1);
hypoMat = zeros(m, classNumber);
zCell = cell(1, layerNumber);
aCell = cell(1, layerNumber);

for layer = 1:layerNumber
    if layer == 1
        aCell(layer) = {[ones(size(X, 1), 1) X]};
    else
        aCell(layer) = {[ones(size(cell2mat(zCell(layer)), 1), 1) sigmoid(cell2mat(zCell(layer)))]};
    end
    if layer ~= layerNumber
        zCell(layer + 1) = {cell2mat(aCell(layer)) * (cell2mat(ThetaCell(layer))')};
    end
end
hypoMatTemp = cell2mat(aCell(end));
hypoMat = hypoMatTemp(:, 2:end);

end
