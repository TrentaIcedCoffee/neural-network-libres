%% Debug for neural_network

% this file is used to debug the following files
%   split.m
%   yToY.m
%   sigmoid.m
%   sigmoidGradient.m
%   forwardPropergate.m
%   backwardPropergate.m
%   cellToLongAssVec.m
%   longAssVecToCell.m
%   costFunction.m
%   costFuncitonIter.m
%   train.m (ignored)
%   predict.m
%   accuracy.m
%   sampleNumberVsCost.m
%   regulatingRateVsCost.m

%% Initialization
close all;
clear;
clc;

addpath('./lib/');
addpath('./data_debug/');

load('data.mat');
load('expect.mat');

%% Debug split.m
[XRun, yRun, XCVRun, yCVRun, XTestRun, yTestRun] = split(XTotal, yTotal);
if ~isApprox(XRun, XExpect) || ...
    ~isApprox(yRun, yExpect) || ...
    ~isApprox(XCVRun, XCVExpect) || ...
    ~isApprox(yCVRun, yCVExpect) || ...
    ~isApprox(XTestRun, XTestExpect) || ...
    ~isApprox(yTestRun, yTestExpect)
    fprintf('split.m ERR\n');
    return;
end
fprintf('split.m ok\n');

%% Debug yToY.m
YRun = yToY(y, classNumber);
if ~isApprox(YRun, YExpect)
    fprintf('yToY.m ERR\n');
    return;
end
fprintf('yToY.m ok\n');

%% Debug sigmoid.m
sigmoidRun = sigmoid(point);
if sigmoidRun ~= sigmoidExpect
    fprintf('sigmoid.m ERR\n');
    return;
end
fprintf('sigmoid.m ok\n');

%% Debug sigmoidGradient.m
sigmoidGradientRun = sigmoidGradient(point);
if sigmoidGradientRun ~= sigmoidGradientExpect
    fprintf('sigmoidGradient.m ERR\n');
    return;
end
fprintf('sigmoidGradient.m ok\n');

%% Debug forwardPropergate.m
[hypoMatRun, zCellRun, aCellRun] = forwardPropergate(ThetaCell, X);
if ~isApprox(hypoMatRun, hypoMatExpect) || ~isApprox(zCellRun, zCellExpect) || ~isApprox(aCellRun, aCellExpect)
    fprintf('forwardPropergate.m ERR\n');
    return;
end
fprintf('forwardPropergate.m ok\n');

%% Debug backwardPropergate.m
gradientCellRun = backwardPropergate(regulatingRate, hypoMat, Y, ThetaCell, zCell, aCell);
if ~isApprox(gradientCellRun, gradientCellExpect)
    fprintf('backwardPropergate.m ERR\n');
    return;
end
fprintf('backwardPropergate.m ok\n');

%% Debug cellToLongAssVec.m
ThetaVecRun = cellToLongAssVec(ThetaCell);
if ~isApprox(ThetaVecRun, ThetaVecExpect)
    fprintf('cellToLongAssVec.m ERR\n');
    return;
end
fprintf('cellToLongAssVec.m ok\n');

%% Debug longAssVecToCell.m
ThetaCellRun = longAssVecToCell(ThetaVec, architecturePara);
if ~isApprox(ThetaCellRun, ThetaCellExpect)
    fprintf('longAssVecToCell.m ERR\n');
    return;
end
fprintf('longAssVecToCell.m ok\n');

%% Debug costFunction.m
[costRun, gradientCellRun] = costFunction(architecturePara, ThetaCell, X, y, regulatingRate);
if ~isApprox(costRun, costExpect) || ~isApprox(gradientCellRun, gradientCellExpect)
    fprintf('costFunction.m ERR\n');
    return;
end
fprintf('costFunction.m ok\n');

%% Debug costFunctionIter.m
[costRun, gradientVecRun] = costFunctionIter(architecturePara, ThetaVec, X, y, regulatingRate);
if ~isApprox(costRun, costExpect) || ~isApprox(gradientVecRun, gradientVecExpect)
    fprintf('costFunctionIter.m ERR\n');
    return;
end
fprintf('costFunctionIter.m ok\n');

%% Debug train.m
% This section is commented due to high difference on computations from different computers
% Ignoring debug of train is safe,
% since sampleNumberVsCost.m and
% regulatingRateVsCost.m cover train.m

% ThetaCellTrainedRun = train(X, y, ThetaCellInitial, regulatingRate, maxIter, architecturePara);
% if ~isApprox(ThetaCellTrainedRun, ThetaCellTrainedExpect)
%     fprintf('train.m ERR\n');
%     return;
% end
% fprintf('train.m ok\n');

%% Debug predict.m
predRun = predict(ThetaCell, X);
if ~isApprox(predRun, predExpect)
    fprintf('predict.m ERR\n');
    return;
end
fprintf('predict.m ok\n');

%% Debug accuracy.m
accuracyRun = accuracy(pred, y);
if ~isApprox(accuracyRun, accuracyExpect)
    fprintf('accuracy.m ERR\n');
    return;
end
fprintf('accuracy.m ok\n');

%% Debug sampleNumberVsCost.m
sampleNumberOptRun = sampleNumberVsCost(X, y, XCV, yCV, ThetaCellInitial, regulatingRate, 200, architecturePara, 2998:1:3000);
if ~isApprox(sampleNumberOptRun, sampleNumberOptExpect)
    fprintf('sampleNumberVsCost.m ERR\n');
    return;
end
fprintf('sampleNumberVsCost.m ok\n');

%% Debug regulatingRateVsCost.m
regulatingRateOptRun = regulatingRateVsCost(X, y, XCV, yCV, ThetaCellInitial, 0:5:10, maxIter, architecturePara);
if ~isApprox(regulatingRateOptRun, regulatingRateOptExpect)
    fprintf('regulatingRateVsCost.m ERR\n');
    return;
end
fprintf('regulatingRateVsCost.m ok\n');

%% Summary
fprintf('all ok\n');

%% Clean
rmpath('./lib/');
rmpath('./data_debug/');
