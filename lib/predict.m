function y = predict(ThetaCell, X)
%PREDICT Predict y using trained ThetaCell
%   y has size(sampleNumber, 1);

[m n] = size(X);
hypoCell = cell(1, length(ThetaCell) + 1); % NOTE history hypothesis, leave for possible uses in future
y = zeros(m, 1);

hypoCell(1) = {X}; % hypoCell has length layerNumber, hypoCell(1) is X
for layer = 2:length(ThetaCell) + 1
    mat = cell2mat(hypoCell(layer - 1));
    Theta = cell2mat(ThetaCell(layer - 1));
    hypoCell(layer) = {sigmoid([ones(m, 1) mat] * Theta')};
end
[~, y] = max(cell2mat(hypoCell(end)), [], 2);

end