picture_1 = load_pic('lena.bmp');
picture_1 = double(picture_1);
picture_2 = load_pic('spreading_QIM.jpg');
picture_2 = double(picture_2);
psnr = calc_psnr(picture_1, picture_2)