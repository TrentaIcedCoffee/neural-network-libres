function [X, y, XCV, yCV, XTest, yTest] = split(XTotal, yTotal)
%SPLIT Split data into three categories, train, cross validation and test
%   divide as [0.6, 0.2, 0.2]

[totalNumber, ~] = size(XTotal);
X = [];
y = [];
XCV = [];
yCV = [];
XTest = [];
yTest = [];

sampleNumber = floor(0.6 * totalNumber);
cvNumber = floor(0.2 * totalNumber);
testNumber = size(XTotal, 1) - sampleNumber - cvNumber;

X = XTotal(1:sampleNumber, :);
y = yTotal(1:sampleNumber, :);
XCV = XTotal(1 + sampleNumber:sampleNumber + cvNumber, :);
yCV = yTotal(1 + sampleNumber:sampleNumber + cvNumber, :);
XTest = XTotal(1 + sampleNumber + cvNumber:end, :);
yTest = yTotal(1 + sampleNumber + cvNumber:end, :);

end