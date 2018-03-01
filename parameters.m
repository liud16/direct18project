e2 = edge(I1seg2,'Canny');
figure
imshow(e2);
i1bw = imbinarize(I1seg2);
figure
imshow(i1bw);
e3 = edge(I1seg1,'Canny');
figure
imshow(e3);
i1bw1 = imbinarize(I1seg1);
figure
imshow(i1bw1);
n_or = sum(sum(i1bw1));
n_dis = sum(sum(i1bw));
order_disorder_ratio = n_or/n_dis;
pep = n_or + n_dis;
per_coverage_pep = 100*pep/(512*512);
per_o_cov = 100-100*n_dis/(512*512);