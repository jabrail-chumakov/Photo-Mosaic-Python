%% Part 1.1
I1 = uint8(100 * ones(1000,1000));
imshow(uint8(I1),[0 255]);

%% Part 1.2
u = repelem([0 255],1,[4 4]);
B = repmat(u,[1000 128]);
imshow(uint8(B),[0 255]);

%% Part 1.3
y = [1:1000];
x = y;
[x,y] = meshgrid(x,y);
Ixy = x./2;
imshow(uint8(Ixy),[0 255]);
 
%% Part 1.4
y = [1:1000];
x = y;
[x, y] = meshgrid(x, y);
I = 255 * exp(-((x-524).^2 + (y-524).^2)/(200^2));
imshow(uint8(I), [0 255]);
 
%% Part 1.5
CI = zeros(1000,1000,3);
CI(1:1000,1:500,1) = 1;   
CI(1:500,1:1000,2) = 1;   
imshow(CI);
