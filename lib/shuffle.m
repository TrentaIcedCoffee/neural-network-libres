function [XShuffled, yShuffled] = shuffle(X, y)
%SHUFFLE Shuffle (X, y) accordinately

[sampleNumber, featureNumber] = size(X);
XShuffled = zeros(sampleNumber, featureNumber);
yShuffled = zeros(sampleNumber, 1);

randVec = randperm(sampleNumber);
XShuffled = X(randVec, :);
yShuffled = y(randVec, :);

end

