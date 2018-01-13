function Y = yToY(y, classNumber)
%YTOY Convert y has size (sampleNumber, 1) to Y has size (sampleNumber, classNumber)
%   call yToY when solving multi-class classification

sampleNumber = size(y, 1);
I = eye(classNumber);
Y = zeros(sampleNumber, classNumber);

for i = 1:sampleNumber
  Y(i, :) = I(y(i), :);
end

end
