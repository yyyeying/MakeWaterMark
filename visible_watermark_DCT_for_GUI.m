function picture = visible_watermark_DCT_for_GUI(cover, watermark)
picture_cover = load_pic(cover);
picture_mark = load_pic(watermark);
picture_marked = visible_watermark_DCT2(picture_cover, picture_mark);
picture = 'cache/marked_DCT.jpg'
imwrite(picture_marked, picture);
end