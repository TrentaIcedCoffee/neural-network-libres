function displayData(x)
%DISPLAYDATA Display 2D grey scale data
%   x has size (400, 1)

x = reshape(x, [20, 20]);

colormap(gray);
imagesc(x);
axis off;
drawnow;

end
