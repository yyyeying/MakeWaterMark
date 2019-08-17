function psnr = calc_psnr(picture_a, picture_b)
disp("[Matlab function] calc_psnr");
[width, height, channel] = size(picture_a);
if channel == 3
    picture_a = rgb_to_gray(picture_a);
    picture_b = rgb_to_gray(picture_b);
end
mse = 0.0;
for i = 1:width
    for j = 1:height
       p2 = (picture_a(i,j) - picture_b(i,j))^2;
       mse = mse + p2;
    end
end
mse;
mse = mse / (width * height);
psnr = 10 * log10((255^2 / double(mse)));
end