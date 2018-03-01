I1 = mat2gray(table2array(tdjgrbp51um1hr3rd020717(1:512,1:512)));
bw1 = imopen(I1,strel('rectangle',[10,512]));
I1_flat = I1-bw1;
m0 = min(min(I1_flat));
m1 = max(max(I1_flat));
I1_flat_rescaled = mat2gray(I1_flat,[m0 m1]);
E1 = edge(I1_flat_rescaled,'Canny');
figure
imshow(I1_flat_rescaled);
figure
imshow(E1);
figure, imshow(I1);