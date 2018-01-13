% NOTE Run the following code on a production machine,
%   taking less than 8 hours

%% neural network model for handwritten digits

%   Train handwritten digits using neural network model
%   Data from MNIST, 5000 samples, each 400 features, classify to 10 classes [1, 10]
%   Using architecture [400, 25, 10], input layer 400 elements; 1 hidden layer with 25 eflements; output layer 10 elements
%   Run 3 times for optmization. Run 1: optimize sample number; Run 2:
%   optimize regulating rate; Run 3: compute Theta and test on test set

%% Load data
close all;
clear;
clc;

addpath('./lib/');
addpath('./data_handwritten_digits/');

load('handwrittenDigits.mat');
if ~exist('X', 'var') || ~exist('y', 'var')
    fprintf('ERR, X or y not contained in mat file\n');
    return;
end
XRaw = X;
yRaw = y;

%% Preperation
%   shuffle data set
%   divide into training set (60%), cross validation set (20%) and test set (20%)
%   initial parameters

[XTotal, yTotal] = shuffle(XRaw, yRaw);

[X, y, XCV, yCV, XTest, yTest] = split(XTotal, yTotal);

[sampleNumber, featureNumber] = size(X);
classNumber = 10;
architecturePara = [400, 25, 10];
maxIter = 400;
ThetaCellInitial = randThetaCell(architecturePara);

%% Optimize sample number (takes < 5h)
sampleNumberOpt = sampleNumberVsCost(X, y, XCV, yCV, ThetaCellInitial, 0, maxIter, architecturePara, 2950:1:3000);
X = X(1:sampleNumberOpt, :);
y = y(1:sampleNumberOpt, :);

%% Optimize regulating rate (lambda)
regulatingRateOpt = regulatingRateVsCost(X, y, XCV, yCV, ThetaCellInitial, 0:1:10, maxIter, architecturePara);
regulatingRate = regulatingRateOpt;

%% Compute Theta
maxIter = 4000;
ThetaCell = train(X, y, ThetaCellInitial, regulatingRate, maxIter, architecturePara);

%% Accuracy
accuracyTrain = accuracy(predict(ThetaCell, X), y);
accuracyCV = accuracy(predict(ThetaCell, XCV), yCV);
accuracyTest = accuracy(predict(ThetaCell, XTest), yTest);
fprintf('train accuracy %.2f\n', accuracyTrain);
fprintf('cross validation accuracy %.2f\n', accuracyCV);
fprintf('test accuracy %.2f\n', accuracyTest);

%% Clean
rmpath('./lib/');
rmpath('./data_handwritten_digits/');
