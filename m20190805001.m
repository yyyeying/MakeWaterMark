picture_cover = load_pic('test2.jpg');
picture_mark = load_pic('watermark.bmp');
picture_marked = visible_watermark(picture_cover, picture_mark, '1');
imwrite(picture_marked, 'marked1.jpg');
picture_marked = visible_watermark(picture_cover, picture_mark, '2');
imwrite(picture_marked, 'marked2.jpg');
picture_marked = visible_watermark(picture_cover, picture_mark, '3');
imwrite(picture_marked, 'marked3.jpg');