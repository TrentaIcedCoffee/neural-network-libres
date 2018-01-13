function gradient = sigmoidGradient(x)
%SIGMOIDGRADIENT Compute derivative of sigmoid function on x

gradient = zeros(size(x));

gradient = sigmoid(x) .* (1 - sigmoid(x));

end
