function pCell = longAssVecToCell(vec, architecturePara)
%LONGASSVECTOCELL Convert ThetaVec, gradientVec to ThetaCell, gradientCell just for iteration
%   NOTE only apply this function for iteration uses as below
%   ThetaVec -> ThetaCell, gradientVec -> gradientCell
%   TODO can we do better? So we don't need this function
%   pCell has element (elementNumber)
%   vec has size (elementNumber, 1)

pCell = cell(1, length(architecturePara) - 1);

startIndex = 1;
for i = 1:length(architecturePara) - 1
    mat = vec(startIndex:startIndex + architecturePara(i + 1) * (architecturePara(i) + 1) - 1);
    pCell(i) = {reshape(mat, architecturePara(i + 1), architecturePara(i) + 1)};
    startIndex = startIndex + architecturePara(i + 1) * (architecturePara(i) + 1);
end

end