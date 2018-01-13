function result = isApprox(a, b)
%ISAPPROX Returns if a is equal b with tolerance
%   tolerance set to 1%
%   result is true if a is in [0.99 * b, 1.01 * b] (positive)
%   result is true if a is in [1.01 * b, 0.99 * b] (negative)
%   handle only matrix and cell comparison

result = false;
tolerance = 0.01;

if (class(a) ~= class(b))
    result = false;
    return;
end

sizeA = size(a);
sizeB = size(b);
if ~isequal(sizeA, sizeB)
    result = false;
    return;
end

vecA = a(:);
vecB = b(:);
vecBMin = zeros(length(vecB), 1);
vecBMax = zeros(length(vecB), 1);

if isfloat(a)
    indexPositive = find(vecB > 0);
    indexNegative = find(vecB < 0);
    vecBMin(indexPositive) = (1 - tolerance) * vecB(indexPositive);
    vecBMin(indexNegative) = (1 + tolerance) * vecB(indexNegative);
    vecBMax(indexPositive) = (1 + tolerance) * vecB(indexPositive);
    vecBMax(indexNegative) = (1 - tolerance) * vecB(indexNegative);
    
    result = all(vecBMin <= vecA) && all(vecA <= vecBMax);
elseif iscell(a)
    for i = 1:length(vecA)
        result = result || isApprox(cell2mat(vecA(i)), cell2mat(vecB(i)));
        if result == false;
            return;
        end
    end
else
    return;
end

end