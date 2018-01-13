function ThetaCell = randThetaCell(architecturePara)
%RANDTHETACELL Create a random ThetaCell used as iteration initial
%   ThetaCell(i) considers bias term, has size (elementNumber(i + 1), elementNumber(i) + 1)
%   ThetaCell(i) maps hypothesis(i) -> hypothesis(i +1), considering bias term of layer i

ThetaCell = cell(1, length(architecturePara) - 1);

for i = 1:length(architecturePara) - 1
    ThetaCell(i) = {rand(architecturePara(i + 1), architecturePara(i) + 1)};
end

end
