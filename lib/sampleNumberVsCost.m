function sampleNumberOpt = sampleNumberVsCost(X, y, XCV, yCV, ThetaCellInitial, regulatingRate, maxIter, architecturePara, intervalSampleNumber)
%SAMPLENUMBERVSCOST Plot map: sampleNumber -> cost, return the most optimized sampleNumber
%   use (XCV, yCV), cross validation data set for optimization

sampleNumberOpt = 0;

costTrain = zeros(length(intervalSampleNumber), 1);
costCV = zeros(length(intervalSampleNumber), 1);

for i = 1:length(intervalSampleNumber)
    sampleNumber = intervalSampleNumber(i);
    ThetaCell = train(X(1:sampleNumber, :), ...
                        y(1:sampleNumber), ...
                        ThetaCellInitial, ...
                        regulatingRate, ...
                        maxIter, ...
                        architecturePara);
    costTrain(i) = costFunction(architecturePara, ThetaCell, X(1:sampleNumber, :), y(1:sampleNumber, :), 0);
    costCV(i) = costFunction(architecturePara, ThetaCell, XCV, yCV, 0);
end

[~, indexSampleNumberOpt] = min(costCV, [], 1);
sampleNumberOpt = intervalSampleNumber(indexSampleNumberOpt);

figure
plot(intervalSampleNumber, costTrain, intervalSampleNumber, costCV);
title('Sample Number VS. Cost')
legend('Train', 'Cross Validation');
xlabel('Sample Number');
ylabel('Cost');
drawnow;

end
