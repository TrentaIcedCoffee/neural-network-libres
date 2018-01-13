function vec = cellToLongAssVec(pCell)
%CELLTOLONGASSVEC Convert ThetaCell, gradientCell to ThetaVec, gradientVec just for iteration
%   NOTE apply only for iteration use like below
%   ThetaCell -> ThetaVec, gradientCell -> gradientVec
%   TODO can we do better? So we don't need this function
%   ThetaCell has elementNumber
%   gradientVec has size (elementNumber, 1)

vec = [];
for i = 1:length(pCell)
    mat = cell2mat(pCell(i));
    vec = [vec; mat(:)];
end

end
