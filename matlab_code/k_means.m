imshowpair(I1_flat_rescaled,feature2DImage,'montage');
L1 = kmeans(X,2,'Replicates',5);
L1 = reshape(L1,[numRows,numCols]);
figure
imshow(label2rgb(L1));
I1seg1 = zeros(size(I1_flat_rescaled),'like',I1_flat_rescaled);
I1seg2 = zeros(size(I1_flat_rescaled),'like',I1_flat_rescaled);
BW = L1 == 1;
BW = repmat(BW,[1 1 1]);
I1seg1(BW) = I1_flat_rescaled(BW);
I1seg2(~BW) = I1_flat_rescaled(~BW);
figure
imshowpair(I1seg2,I1seg1,'montage');