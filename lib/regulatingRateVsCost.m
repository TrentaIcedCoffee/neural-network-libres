function regulatingRateOpt = regulatingRateVsCost(X, y, XCV, yCV, ThetaCellInitial, intervalRegulatingRate, maxIter, architecturePara)
%REGULATINGRATEOPT Plot map: regulatingRate -> cost, returns the most optimized regulatingRate
%   NOTE spots was set to 2 for debug, set to 100 for production
%   regulatingRate has range [minRegulatingRate, maxRegulatingRate]
%   use (XCV, yCV), cross validation data set for optimization

regulatingRateOpt = 0;

costTrain = zeros(length(intervalRegulatingRate), 1);
costCV = zeros(length(intervalRegulatingRate), 1);
for i = 1:length(intervalRegulatingRate)
    regulatingRate = intervalRegulatingRate(i);
    ThetaCell = train(X, y, ThetaCellInitial, regulatingRate, maxIter, architecturePara);
    % set regulatingRate to 0 when compute error
    costTrain(i) = costFunction(architecturePara, ThetaCell, X, y, 0);
    costCV(i) = costFunction(architecturePara, ThetaCell, XCV, yCV, 0);
end
    
[~, regulatingRateOptIndex] = min(costCV, [], 1);
regulatingRateOpt = intervalRegulatingRate(regulatingRateOptIndex);

figure
plot(intervalRegulatingRate, costTrain, intervalRegulatingRate, costCV);
title('Regulating Rate VS. Cost')
legend('Train', 'Cross Validation');
xlabel('Regulating Rate');
ylabel('Cost');
drawnow;

end