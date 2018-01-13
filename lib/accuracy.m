function accuracy = accuracy(predict, y)
%ACCURACY Compute accuracy with denominator 100
%   predict, y has same size (sampleNumber, 1)

accuracy = 0;

accuracy = mean(double(predict == y)) * 100;

end
