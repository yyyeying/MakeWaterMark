picture_cover = load_pic('lena.bmp');
picture_mark = load_pic('watermark.bmp');
%picture_cover = imresize(picture_cover, [128,128], 'bilinear');
picture_mark = imresize(picture_mark, [128,128], 'bilinear');
picture_marked = visible_watermark_DCT2(picture_cover, picture_mark);
imwrite(picture_marked, 'marked_DCT.jpg');
